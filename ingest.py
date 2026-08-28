import os
import re
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer

# --- Configuration ---
VAULT_DIR = "./vault"
CHROMA_PATH = "./chroma_db"
CHUNK_SIZE = 220      # words per chunk
CHUNK_OVERLAP = 40    # overlapping words between chunks

# --- Initialize clients ---
embedder = SentenceTransformer("all-MiniLM-L6-v2")
chroma = chromadb.PersistentClient(path=CHROMA_PATH)
col = chroma.get_or_create_collection("vault", metadata={"hnsw:space": "cosine"})   

def clean_markdown(text: str) -> str:
    """Remove frontmatter, wikilinks, and code blocks from markdown."""
    # Strip YAML frontmatter (---\n...\n---)
    text = re.sub(r'^---.*?---', '', text, flags=re.DOTALL)
    # Flatten [[wikilinks]] → keep display text
    text = re.sub(r'\[\[([^\]|]+)(\|([^\]]+))?\]\]', r'\3\1', text)
    # Strip code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    return text.strip()


def chunk_text(text: str):
    """Split text into overlapping word windows."""
    words = text.split()
    step = CHUNK_SIZE - CHUNK_OVERLAP
    for i in range(0, len(words), step):
        window = words[i:i + CHUNK_SIZE]
        if window:
            yield " ".join(window)


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed texts using local model (free, no API needed)."""
    vectors = embedder.encode(texts, show_progress_bar=True)
    return [v.tolist() for v in vectors]   


def build_index():
    """Walk vault, chunk, embed, and store in ChromaDB."""
    total_chunks = 0
    total_files = 0

    for root, _, files in os.walk(VAULT_DIR):
        for f in files:
            if not f.endswith('.md'):
                continue

            path = os.path.join(root, f)
            rel_path = os.path.relpath(path, VAULT_DIR)

            with open(path, 'r', encoding='utf-8') as fh:
                text = clean_markdown(fh.read())

            if not text:
                continue

            chunks = list(chunk_text(text))
            if not chunks:
                continue

            # Embed in batches of 100 to avoid rate limits
            vectors = []
            for i in range(0, len(chunks), 100):
                batch = chunks[i:i+100]
                vectors.extend(embed_texts(batch))

            ids = [f"{rel_path}::{i}" for i in range(len(chunks))]
            metadatas = [{"source": rel_path} for _ in chunks]

            col.upsert(
                ids=ids,
                embeddings=vectors,
                documents=chunks,
                metadatas=metadatas
            )

            total_chunks += len(chunks)
            total_files += 1
            print(f"  ✓ {rel_path} → {len(chunks)} chunks")

    print(f"\n✅ Done! Indexed {total_chunks} chunks from {total_files} files.")


if __name__ == "__main__":
    print("🔍 Building index from vault...\n")
    build_index()   