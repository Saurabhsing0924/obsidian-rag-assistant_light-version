# Obsidian Vault RAG Assistant

Built this for a GenAI internship build sprint. The idea is simple — point it at your Obsidian vault, ask questions in plain English, get answers that are actually grounded in your notes (not hallucinated).

## Live Links

- Frontend: [https://vault-rag-assistant.lovable.app/]
- Backend: https://obsidian-rag-assistant.onrender.com
- Demo video: [your Loom link](https://your-loom-link.com)

## What it does

You have a folder of markdown notes (an Obsidian vault). You type a question. It finds the most relevant parts of those notes and asks an LLM to answer using *only* that context. Every answer comes with a citation to which file it came from.

That's it. No magic.

## How it works (honestly)

I originally planned to use vector embeddings (OpenAI's `text-embedding-3-small` + ChromaDB) for retrieval. Built it locally, worked great. Then tried to deploy on Render's free tier and kept hitting OOM — PyTorch + the embedding model just doesn't fit in 512MB.

Tried `fastembed` (ONNX-based, lighter). Still borderline.

So I made a pragmatic call: my vault is 14 short notes, ~14 chunks total. I pre-computed the chunks into a JSON file and used simple keyword overlap for retrieval. It's not "real" RAG in the vector-search sense, but for this scale it works fine and the server boots in under 2 seconds with zero model loading.

If the vault grows past ~200 chunks, I'd switch back to embeddings. For now, this is the right tradeoff.

The LLM part uses Groq's free tier (`openai/gpt-oss-20b`). It's fast (~1000 tok/s) and doesn't need a credit card.

## Stack

- **Frontend:** Lovable (React + Tailwind). I prompted it, it generated the UI. Took 10 minutes.
- **Backend:** FastAPI, Python 3.12
- **Retrieval:** Keyword matching on pre-computed chunks (`chunks.json`)
- **LLM:** Groq API
- **Hosting:** Render (backend) + Lovable (frontend). Both free tier.

## Running it locally

```bash
git clone https://github.com/Saurabhsing0924/obsidian-rag-assistant_light-version
cd obsidian-rag-assistant_light-version

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# You need a free Groq API key from console.groq.com
set GROQ_API_KEY=gsk-your-key-here

uvicorn main:app --reload --port 8000   