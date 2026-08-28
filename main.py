from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os, json, re
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pre-computed chunks (no model needed)
with open("chunks.json", "r") as f:
    CHUNKS = json.load(f)

# Groq client
groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


def simple_retrieve(question: str, top_k: int = 5) -> list[dict]:
    """Keyword-based retrieval. Works for small vaults (< 100 chunks)."""
    question_words = set(re.findall(r'\w+', question.lower()))
    scored = []
    for chunk in CHUNKS:
        chunk_words = set(re.findall(r'\w+', chunk["text"].lower()))
        overlap = len(question_words & chunk_words)
        scored.append((overlap, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scored[:top_k]]


class QueryRequest(BaseModel):
    question: str
    top_k: int = 5


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@app.get("/api/health")
def health():
    return {"status": "ok", "chunks_indexed": len(CHUNKS)}


@app.post("/api/query", response_model=QueryResponse)
def query(req: QueryRequest):
    question = req.question
    top_k = req.top_k

    # 1. Retrieve (keyword matching, no model)
    results = simple_retrieve(question, top_k)

    # 2. Build context
    context_parts = []
    for i, chunk in enumerate(results):
        context_parts.append(f"[Source {i+1}: {chunk['source']}]\n{chunk['text']}")
    context = "\n\n---\n\n".join(context_parts)

    # 3. Generate answer via Groq
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
    sources = list(set(c["source"] for c in results))

    return QueryResponse(answer=answer, sources=sources)


@app.post("/api/reindex")
def reindex():
    return {"status": "ok", "detail": "Reindex locally: run python ingest.py then push chunks.json"}   