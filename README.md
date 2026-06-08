# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section _after_ you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

     This retrieval-augmented generation (RAG) system focuses on University of Hawaiʻi at Mānoa Information and Computer Sciences (ICS) courses and professors.

     The goal is to help students answer questions about:

     - Professor teaching styles
     - Course difficulty
     - Workload expectations
     - Student experiences
     - Programming languages used in ICS courses
     - Degree requirements

     This information is valuable because official university resources provide course descriptions and degree requirements, but they do not capture student experiences, teaching quality, workload, or advice from previous students. Student reviews often contain information that is difficult to find through official channels.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| #   | Source                              | Type                                             | URL or file path                                                                                                                                                                                                  |
| --- | ----------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | UH ICS Department Homepage          | Official information about faculty and programs. | https://www.ics.hawaii.edu/people/                                                                                                                                                                                |
| 2   | UH ICS Course Catalog               | Official descriptions of ICS courses.            | https://catalog.manoa.hawaii.edu/search_advanced.php?cur_cat_oid=4&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=33&filter%5Bkeyword%5D=ics&filter%5Bexact_match%5D=1 |
| 3   | UH Computer Science Program         | Degree requirements and program overview.        | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1687&returnto=1018                                                                                                                             |
| 4   | Rate My Professors – Carleton Moore | Student reviews of Professor Carleton Moore      | https://www.ratemyprofessors.com/professor/1898989                                                                                                                                                                |
| 5   | Rate My Professors – Peter Sadowski | Student reviews of Professor Peter Sadowski      | https://www.ratemyprofessors.com/professor/2639726                                                                                                                                                                |
| 6   | Rate My Professors – Depeng Li      | Student reviews of Professor Depeng Li           | https://www.ratemyprofessors.com/professor/1979395                                                                                                                                                                |
| 7   | Rate My Professors – Henri Casanova | Student reviews of Professor Henri Casanova      | https://www.ratemyprofessors.com/professor/1070112                                                                                                                                                                |
| 8   | Rate My Professors - David Conner   | Student reviews of Professor David Conner        | https://www.ratemyprofessors.com/professor/3006226                                                                                                                                                                |
| 9   | Rate My Professors - Jason Leigh    | Student reviews of Professor Jason Leigh         | https://www.ratemyprofessors.com/professor/1950937                                                                                                                                                                |
| 10  | Rate My Professors - Dusko Pavlovic | Student reviews of Professor Dusko Pavlovic      | https://www.ratemyprofessors.com/professor/2342816                                                                                                                                                                |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 450

**Overlap:** 50

**Why these choices fit your documents:** The document collection contains UH ICS course descriptions, degree requirement information, faculty information, and Rate My Professors reviews. These documents are generally short and information-dense, so a chunk size of 450 characters keeps related information together while still allowing accurate semantic retrieval.

An overlap of 50 characters was used to preserve context between adjacent chunks. This helps prevent important information, such as professor ratings, course names, or review comments, from being split across chunk boundaries and becoming difficult to retrieve.

Before chunking, documents were cleaned by removing HTML tags, normalizing whitespace, and converting content into plain text while preserving important information such as professor names, course numbers, ratings, and review text.

**Final chunk count:** 198

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** SentenceTransformer("all-MiniLM-L6-v2")

**Production tradeoff reflection:** If this system were deployed for real users, I would consider several tradeoffs when selecting an embedding model. A larger model could improve retrieval accuracy and better understand complex questions, but it would also increase latency and computational costs. I would also consider multilingual support in case users ask questions in languages other than English. Another factor is whether the model runs locally or through an API service. Local models provide better privacy and lower long-term costs, while API-hosted models are easier to scale and may offer higher-quality embeddings. Since this project focuses on university courses and professor reviews, retrieval accuracy would be my highest priority, followed by response speed and deployment cost.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** The system uses Groq's `llama-3.3-70b-versatile` model with a strict grounding prompt. Retrieved document chunks are inserted into the prompt as context before generation.

**How source attribution is surfaced in the response:**
Source attribution is added programmatically rather than relying on the LLM to generate citations. After retrieval, the system collects the source metadata associated with each retrieved chunk (such as the professor name, course catalog page, or document source) and appends a "Sources" section to the final response.

For example:

Answer:
Henri Casanova received some of the highest student ratings in the dataset, with multiple reviews describing him as one of the best ICS professors and praising his teaching style.

Sources:

- Henri Casanova Rate My Professors Reviews
- UH ICS Faculty Dataset

This guarantees that every answer is accompanied by the documents used during retrieval, even if the LLM does not explicitly mention them in its generated text.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| #   | Question                                                     | Expected answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | System response (summarized)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Retrieval quality  | Response accuracy  |
| --- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ------------------ |
| 1   | Which ICS professors receive the highest student ratings?    | Based on the provided context, Professor Henri Casanova receives a perfect 5.0 quality rating from a student [Source 1]. Additionally, Professor Jason Leigh has an overall quality ranking of 3.8/5 based on 28 ratings [Source 3].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | In comparison, Professor Peter Sadowski has a lower ranking of 2.1/5 based on 19 ratings [Source 4]. Since the sources do not specify the source type as student_review for any of the professors except that the content of [Source 1] and [Source 3] and [Source 4] implies they are student reviews, we can consider [Source 1] and [Source 3] as the sources with the highest student ratings for ICS professors. Therefore, based on the provided context, Professor Henri Casanova and Professor Jason Leigh receive the highest student ratings among the mentioned ICS professors. | Partially relevant | Partially accurate |
| 2   | How does ICS 211 compare to ICS 111?                         | I don't have enough information in the provided documents to answer that.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Off-target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Inaccurate         | Inaccurate         |
| 3   | What do students say about the workload in ICS 311?          | According to [Source 1], a student mentions that ICS 311 is compared to another class (ICS 222) in terms of difficulty, stating that ICS 222 "was the hardest class I've ever taken even when compared to ICS 311". However, there is no direct information about the workload in ICS 311. Therefore, I don't have enough information in the provided documents to answer that.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Partially relevant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Partially accurate | Partially accurate |
| 4   | Which professors are considered good for beginners?          | Based on the provided context, Professor Henri Casanova is consistently praised by students for being a great professor, explaining things simply, and being helpful [Source 1, Source 2, Source 4, Source 5]. He is described as one of the best professors in the department, with classes that are not too hard or easy [Source 4]. Additionally, his lectures are interesting, detailed, and easy to understand [Source 5]. Professor Carleton Moore is also mentioned as a good professor, with easy quizzes and projects [Source 3]. However, the overall praise for Professor Henri Casanova suggests that he may be a good fit for beginners due to his ability to explain complex concepts in a simple manner. It's worth noting that the source types for these professors are unknown, but based on the content, it appears that they may be student reviews. | Relevant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Accurate           |
| 5   | What programming languages are commonly used in ICS courses? | Based on the provided context, the following programming languages are mentioned as being used in ICS courses: 1. LISP [Source 1] 2. Prolog [Source 1] 3. Perl [Source 2] 4. JavaScript [Source 2] 5. PHP [Source 2] 6. Python [Source 2] 7. Shell scripting [Source 2]. Note that these languages are mentioned in the context of specific courses, such as ICS 313, ICS 215, but it can be inferred that they are used in the ICS program. However, without more information, it's difficult to say which languages are most commonly used across all ICS courses.                                                                                                                                                                                                                                                                                                     | Relevant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Accurate           |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:** Which ICS professors receive the highest student ratings?

**What the system returned:** The system returned an answer that correctly identified Professor Henri Casanova as having the highest rating (5.0), but incorrectly inferred that Professor Jason Leigh also had the highest rating without sufficient supporting evidence in the retrieved context.

**Root cause (tied to a specific pipeline stage):** The failure occurred at the generation stage. The retrieval stage returned multiple chunks containing partial professor ratings, but did not provide a complete ranking comparison across all professors. As a result, the model over-generalized from incomplete evidence and hallucinated a comparative conclusion. This is a context aggregation issue where retrieved chunks were individually relevant but collectively insufficient to support a global ranking decision.

**What you would change to fix it:** I would improve retrieval by increasing chunk overlap and ensuring that ranking-related information is stored in a single consolidated chunk or table. Additionally, I would add a post-retrieval filtering step to group all professor rating chunks before passing them to the LLM, reducing the chance of partial evidence being misinterpreted as a complete ranking.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** The spec clearly defined how chunks should be structured and how retrieval context should be grounded in source documents. This helped guide my design of the chunking strategy and ensured that each retrieved passage could be traced back to a specific source. It also helped enforce consistency in how answers should cite or rely on retrieved information instead of hallucinating.

**One way your implementation diverged from the spec, and why:** My implementation diverged in how aggressively I chunked documents. Initially, I used smaller chunks than suggested in the planning document, which improved retrieval precision but sometimes caused loss of context for comparison-based questions. I adjusted this later by increasing chunk size and overlap to better preserve relationships between entities.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- _What I gave the AI:_ I provided my ChromaDB-based RAG pipeline requirements, including a chunking + embedding + retrieval + LLM answering architecture. I also described my dataset (ICS course and professor reviews) and asked for help designing a full vector database pipeline using sentence-transformers and ChromaDB, including metadata tracking for professors and course types.
- _What it produced:_ The AI generated a full RAG pipeline structure including: document embedding with all-MiniLM-L6-v2, vector storage using ChromaDB PersistentClient, cosine similarity search, and a retrieval function that returns top-k relevant chunks. It also suggested adding metadata fields and a simple query-to-context prompt feeding into an LLM (Groq API).
- _What I changed or overrode:_ I significantly expanded the system into a production-style pipeline by adding:
  Persistent ChromaDB storage directory (data/chroma_db)
  Structured metadata tagging (professor, source, type)
  Normalized embeddings (normalize_embeddings=True) for cosine consistency
  A full evaluation function (evaluate_retrieval) to measure retrieval quality using distance thresholds
  A batch test suite of real ICS-related queries to validate performance
  These additions made the system more robust and measurable compared to the initial AI-generated prototype.

**Instance 2**

- _What I gave the AI:_ I provided my LLM prompt design and asked how to improve grounding for a retrieval-augmented generation system using Groq’s llama-3.3-70b-versatile model. I also included sample retrieved chunks and asked how to ensure answers stay strictly within retrieved context.
- _What it produced:_ The AI returned a basic prompt template that injected retrieved context into the model input and instructed it to “use only the context below.” It also suggested formatting retrieved documents as a single concatenated string and using a simple chat completion call via Groq API.
- _What I changed or overrode:_ I strengthened and operationalized the grounding system by:
  Making the prompt stricter with explicit “DO NOT GUESS beyond context” constraint
  Formatting context with professor-level tagging:
  "[Professor: X] text" to improve attribution clarity
  Adding a retrieval routing function (smart_retrieve) to conditionally handle query types (professor ratings, workload, comparisons)
  Implementing a full pipeline function (ask) that integrates retrieval + generation + printing structured output
  Extending evaluation with multiple test queries to verify grounding behavior across different question types
