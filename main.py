from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
from fastembed import TextEmbedding
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Initialize ---
CHROMA_PATH = "./chroma_db"
chroma = chromadb.PersistentClient(path=CHROMA_PATH)
col = chroma.get_or_create_collection("vault", metadata={"hnsw:space": "cosine"})

groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)  


# --- Request/Response models ---
class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


# --- Endpoints ---
@app.get("/api/health")
def health():
    return {"status": "ok", "chunks_indexed": col.count()}


@app.post("/api/query", response_model=QueryResponse)
def query(req: QueryRequest): 
    question = req.question
    top_k = req.top_k

    q_vec = list(embedder.embed([question]))[0].tolist()

    results = col.query(
        query_embeddings=[q_vec],
        n_results=top_k,
    )

    chunks = results["documents"][0]
    metadatas = results["metadatas"][0]

    context_parts = []
    for i, (chunk, meta) in enumerate(zip(chunks, metadatas)):
        context_parts.append(f"[Source {i+1}: {meta['source']}]\n{chunk}")

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""You are a knowledge assistant. Answer the user's question using ONLY the provided context from their notes.

Rules:
- If the answer is in the context, give a clear, specific answer.
- Cite sources inline like [1], [2] referring to the source numbers.
- If the answer is NOT in the context, say: "I couldn't find that in the vault."
- Be concise. 2-4 sentences max unless the question requires more detail.

Context:
{context}

Question: {question}"""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500,
    )

    answer = response.choices[0].message.content
    sources = list(set(m["source"] for m in metadatas))

    return QueryResponse(answer=answer, sources=sources)


@app.post("/api/reindex")
def reindex():
    from ingest import build_index
    build_index()
    return {"status": "ok"}   