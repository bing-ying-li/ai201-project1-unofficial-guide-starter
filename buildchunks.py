from pathlib import Path
import json
import re
import random

DATA_DIR = Path("data")
OUTPUT_DIR = Path("chunkdata")
OUTPUT_FILE = OUTPUT_DIR / "chunks.json"

CHUNK_SIZE = 450
OVERLAP = 50


# =========================
# 1. CLEAN TEXT
# =========================
def clean_text(text):
    text = text.replace("\r\n", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# =========================
# 2. PROFESSOR NAME
# =========================
def get_professor_name(file_path):
    name = file_path.stem
    name = name.replace("_", " ").replace("-", " ")
    return name.title()


# =========================
# 3. SPLIT RMP REVIEWS
# =========================
def split_rmp_reviews(text):
    """
    Split RateMyProfessor-style reviews.
    Each review starts with "Quality X.X"
    """

    reviews = re.split(r"(?=Quality\s*\d+\.\d+)", text)

    cleaned = []
    for r in reviews:
        r = r.strip()

        # remove junk
        if len(r.split()) < 30:
            continue

        cleaned.append(r)

    return cleaned


# =========================
# 4. SPLIT COURSE CATALOG
# =========================
def split_courses(text):
    """
    Split ICS course catalog into individual courses
    """
    parts = re.split(r"(?=ICS\s\d{3}\s-)", text)
    return [p.strip() for p in parts if len(p.split()) > 10]


# =========================
# 5. SAFE CHUNKING
# =========================
def split_long_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    words = text.split()

    if len(words) <= chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end]).strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# =========================
# 6. LOAD FILES
# =========================
def load_documents():
    documents = []

    for file_path in sorted(DATA_DIR.glob("*.txt")):
        text = file_path.read_text(encoding="utf-8")
        text = clean_text(text)

        if not text:
            continue

        documents.append({
            "source": str(file_path),
            "text": text
        })

    return documents


# =========================
# 7. BUILD CHUNKS
# =========================
def build_chunks(documents):
    final_chunks = []

    for doc in documents:
        file_path = Path(doc["source"])
        text = doc["text"]

        professor = get_professor_name(file_path)

        # detect course vs reviews more safely
        is_course = re.search(r"ICS\s\d{3}\s-", text) is not None

        if is_course:
            records = split_courses(text)
        else:
            records = split_rmp_reviews(text)

        if not records:
            records = [text]

        for i, record in enumerate(records):

            record = record.strip()

            # filter tiny junk
            if len(record.split()) < 30:
                continue

            # remove UI / boilerplate noise
            bad_patterns = [
                "Print (opens",
                "opens a new window",
                "Click to expand",
                "Course Description"
            ]

            if any(p in record for p in bad_patterns):
                continue

            sub_chunks = split_long_text(record)

            for j, chunk in enumerate(sub_chunks):

                final_chunks.append({
                    "id": f"{file_path.stem}_{i}_{j}",
                    "text": chunk,
                    "source": str(file_path),
                    "professor": professor,
                    "record_index": i,
                    "chunk_index": j,
                    "word_count": len(chunk.split())
                })

    return final_chunks


# =========================
# 8. SAVE OUTPUT
# =========================
def save_chunks(chunks):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)


# =========================
# 9. DEBUG: PRINT SAMPLES
# =========================
def print_random_chunks(chunks, n=5):
    sample = random.sample(chunks, min(n, len(chunks)))

    print("\n====================")
    print("RANDOM CHUNK CHECK")
    print("====================\n")

    for i, c in enumerate(sample):
        print(f"--- CHUNK {i} ---")
        print("ID:", c["id"])
        print("Professor:", c["professor"])
        print("Source:", c["source"])
        print("Word count:", c["word_count"])
        print("\nTEXT:\n")
        print(c["text"][:800])
        print("\n------------------\n")


# =========================
# 10. RUN PIPELINE
# =========================
def main():
    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    chunks = build_chunks(documents)

    # final safety filter
    chunks = [c for c in chunks if c["text"].strip()]

    print(f"Total chunks: {len(chunks)}")

    save_chunks(chunks)

    print_random_chunks(chunks, 5)

    print(f"\nSaved → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()