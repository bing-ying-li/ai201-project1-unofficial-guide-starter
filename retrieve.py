from pathlib import Path
import json
import os

import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

# ======================
# LOAD ENV
# ======================
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ======================
# CONFIG
# ======================
CHUNKS_FILE = Path("chunkdata/chunks.json")
CHROMA_DIR = Path("data/chroma_db")

COLLECTION_NAME = "uhm_cs_professor_reviews"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

TOP_K = 5
GROQ_MODEL = "llama-3.1-8b-instant"

# ======================
# INIT MODELS
# ======================
embed_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
client_llm = Groq(api_key=GROQ_API_KEY)

# ======================
# LOAD CHUNKS
# ======================
def load_chunks():
    if not CHUNKS_FILE.exists():
        raise FileNotFoundError(f"{CHUNKS_FILE} not found")
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
# ======================
# BUILD VECTOR DB
# ======================
def build_vector_store():
    chunks = load_chunks()

    texts = [c["text"] for c in chunks]
    ids = [c["id"] for c in chunks]

    metadatas = []
    for c in chunks:
        text = c["text"].lower()

        if "ranking" in text or "would take again" in text or "quality" in text:
            chunk_type = "review"
        elif "credits:" in text:
            chunk_type = "course"
        else:
            chunk_type = "other"

        metadatas.append({
            "professor": c.get("professor", ""),
            "source": c.get("source", ""),
            "type": chunk_type
        })

    print("Creating embeddings...")
    
    embeddings = embed_model.encode(texts, normalize_embeddings=True).tolist()

    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print("Vector DB ready:", collection.count(), "chunks")

# ======================
# GET COLLECTION
# ======================
def get_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    return client.get_collection(name=COLLECTION_NAME)

# ======================
# RETRIEVE
# ======================
def retrieve(query, top_k=TOP_K):
    collection = get_collection()

    q_emb = embed_model.encode([query], normalize_embeddings=True).tolist()

    results = collection.query(
        query_embeddings=q_emb,
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    output = []
    for i in range(len(results["documents"][0])):
        output.append({
            "text": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return output

# ======================
# SMART ROUTER
# ======================
def smart_retrieve(query):
    q = query.lower()

    if "professor" in q or "rating" in q or "rate" in q:
        return retrieve(query)

    if "workload" in q or "students say" in q:
        return retrieve(query)

    return retrieve(query)

# ======================
# LLM (GROQ) ANSWER
# ======================
def generate_answer(query, results):
    context = "\n\n".join([
        f"[Professor: {r['metadata'].get('professor','')}] {r['text']}"
        for r in results
    ])

    prompt = f"""
You are an AI assistant for ICS course and professor Q&A.

Use ONLY the context below.

Context:
{context}

Question:
{query}

Rules:
- Be concise
- If professor-related, list names clearly
- If comparing courses, explain differences simply
- If workload, summarize student opinions
- Do NOT guess beyond context

Answer:
"""

    response = client_llm.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# ======================
# FULL PIPELINE
# ======================
def ask(query):
    results = smart_retrieve(query)
    answer = generate_answer(query, results)

    print("\n" + "=" * 80)
    print("QUESTION:", query)
    print("=" * 80)
    print(answer)

def evaluate_retrieval():
    test_queries = [
        "Which ICS professors receive the highest ratings?",
        "How does ICS 211 compare to ICS 111?",
        "What do students say about workload in ICS 311?",
        "Which professors are good for beginners?",
        "What programming languages are used in ICS courses?"
    ]

    for query in test_queries:
        print("\n" + "=" * 90)
        print("QUERY:", query)
        print("=" * 90)

        results = retrieve(query)

        for i, r in enumerate(results):
            print(f"\nRank {i+1}")
            print(f"DISTANCE: {r['distance']:.4f}")
            print(f"PROF: {r['metadata'].get('professor','')}")
            print(f"TEXT:\n{r['text'][:500]}")
            print("-" * 80)

        # simple judgment
        best = results[0]

        print("\n🔍 QUICK ANALYSIS:")
        if best["distance"] < 0.35:
            print("GOOD retrieval (strong semantic match)")
        elif best["distance"] < 0.6:
            print("OK retrieval (some relevance but weak)")
        else:
            print("BAD retrieval (likely irrelevant)")
# ======================
# MAIN
# ======================
if __name__ == "__main__":
    build_vector_store()
    evaluate_retrieval()
    test_queries = [
        "Which ICS professors receive the highest ratings?",
        "How does ICS 211 compare to ICS 111?",
        "What do students say about workload in ICS 311?",
        "Which professors are good for beginners?",
        "What programming languages are used in ICS courses?"
    ]
    for q in test_queries:
        ask(q)
