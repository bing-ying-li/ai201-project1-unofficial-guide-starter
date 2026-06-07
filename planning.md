# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

Domain: University CS Professor and Course Reviews

This guide focuses on student experiences with computer science courses and professors at the University of Hawaii. Information about teaching quality, workload, grading style, and course difficulty is often scattered across Rate My Professors, Reddit discussions, and unofficial student forums. Bringing these sources together makes it easier for students to make informed decisions when planning their schedules and selecting instructors.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| #   | Source                               | Description                                      | URL or location                                                                                                                                                                                                        |
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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| #   | Question                                                     | Expected answer                                                                                                                                                                                                                                                                                                                                     |
| --- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Which ICS professors receive the highest student ratings?    | Henri Casanova                                                                                                                                                                                                                                                                                                                                      |
| 2   | How does ICS 211 compare to ICS 111?                         | CS 111 focuses on fundamental programming concepts and is intended for beginners, while ICS 211 builds on those skills and introduces object-oriented programming and data structures. Most students consider ICS 211 more challenging because it requires larger programming projects and a deeper understanding of software design concepts.      |
| 3   | What do students say about the workload in ICS 311?          | Students generally describe ICS 311 as one of the most challenging and time-consuming courses in the UH Mānoa Computer Science curriculum. Many report spending substantial time on mathematical proofs, algorithm analysis, quizzes, and homework assignments, and often recommend taking a lighter overall course load while enrolled in ICS 311. |
| 4   | Which professors are considered good for beginners?          | Henri Casanova is frequently praised for clear explanations and genuine concern for student learning. One student described him as "one of the best ICS professors" and noted that he takes time to explain concepts thoroughly.                                                                                                                    |
| 5   | What programming languages are commonly used in ICS courses? | Programming languages in UH ICS courses commonly include Java, Python, JavaScript, SQL, C, and C++. Introductory programming courses typically emphasize Java, while upper-level courses use different languages depending on the topic, such as web development, databases, systems programming, or artificial intelligence.                       |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
