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

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| #   | Source                               | Type                                             | URL or file path                                                                                                                                                                                                       |
| --- | ------------------------------------ | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | UH ICS Department Homepage           | Official information about faculty and programs. | https://www.ics.hawaii.edu/                                                                                                                                                                                            |
| 2   | UH ICS Course Catalog                | Official descriptions of ICS courses.            | https://catalog.manoa.hawaii.edu/content.php?catoid=4&navoid=949                                                                                                                                                       |
| 3   | UH Computer Science Program          | Degree requirements and program overview.        | https://catalog.manoa.hawaii.edu/preview_program.php?catoid=4&poid=1687&returnto=1018                                                                                                                                  |
| 4   | Rate My Professors – iCarleton Moore | Student reviews of Professor Carleton Moore      | https://www.ratemyprofessors.com/professor/1898989                                                                                                                                                                     |
| 5   | Rate My Professors – Peter Sadowski  | Student reviews of Professor Peter Sadowski      | https://www.ratemyprofessors.com/professor/2639726                                                                                                                                                                     |
| 6   | Rate My Professors – Depeng Li       | Student reviews of Professor Depeng Li           | https://www.ratemyprofessors.com/professor/1979395                                                                                                                                                                     |
| 7   | Rate My Professors – Henri Casanova  | Student reviews of Professor Henri Casanova      | https://www.ratemyprofessors.com/professor/1070112                                                                                                                                                                     |
| 8   | ICS 111 Course Information           | Introduction to Computer Science course.         | https://catalog.manoa.hawaii.edu/search_advanced.php?cur_cat_oid=4&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=33&filter%5Bkeyword%5D=ics+111&filter%5Bexact_match%5D=1  |
| 9   | ICS 211 Course Information           | Data Structures course description.              | https://catalog.manoa.hawaii.edu/search_advanced.php?cur_cat_oid=4&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=33&filter%5Bkeyword%5D=ICS+211+&filter%5Bexact_match%5D=1 |
| 10  | ICS 311 Course Information           | Algorithms course description and requirements.  | https://catalog.manoa.hawaii.edu/search_advanced.php?cur_cat_oid=4&search_database=Search&search_db=Search&cpage=1&ecpage=1&ppage=1&spage=1&tpage=1&location=33&filter%5Bkeyword%5D=ICS+311&filter%5Bexact_match%5D=1  |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| #   | Question                                                     | Expected answer                                                                                                                                                                                                                                                                                                                                     | System response (summarized) | Retrieval quality | Response accuracy |
| --- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------- | ----------------- |
| 1   | 1                                                            | Which ICS professors receive the highest student ratings?                                                                                                                                                                                                                                                                                           | Henri Casanova               |
| 2   | How does ICS 211 compare to ICS 111?                         | CS 111 focuses on fundamental programming concepts and is intended for beginners, while ICS 211 builds on those skills and introduces object-oriented programming and data structures. Most students consider ICS 211 more challenging because it requires larger programming projects and a deeper understanding of software design concepts.      |
| 3   | What do students say about the workload in ICS 311?          | Students generally describe ICS 311 as one of the most challenging and time-consuming courses in the UH Mānoa Computer Science curriculum. Many report spending substantial time on mathematical proofs, algorithm analysis, quizzes, and homework assignments, and often recommend taking a lighter overall course load while enrolled in ICS 311. |
| 4   | Which professors are considered good for beginners?          | Henri Casanova is frequently praised for clear explanations and genuine concern for student learning. One student described him as "one of the best ICS professors" and noted that he takes time to explain concepts thoroughly.                                                                                                                    |
| 5   | What programming languages are commonly used in ICS courses? | Programming languages in UH ICS courses commonly include Java, Python, JavaScript, SQL, C, and C++. Introductory programming courses typically emphasize Java, while upper-level courses use different languages depending on the topic, such as web development, databases, systems programming, or artificial intelligence.                       |

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

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

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

- _What I gave the AI:_
- _What it produced:_
- _What I changed or overrode:_

**Instance 2**

- _What I gave the AI:_
- _What it produced:_
- _What I changed or overrode:_
