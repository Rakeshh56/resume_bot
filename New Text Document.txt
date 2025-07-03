#  Resume Screener Bot using LangChain

This project is an AI-powered resume screening tool that analyzes a candidate's resume against a job description and provides a match percentage, matched/missing skills, and a recommendation.

---

##  How LLM is Used

This app uses a **large language model (LLM)** to evaluate the similarity and relevance between a resume and a job description.

- We use **LangChain** to create a structured prompt that asks the LLM to:
  - Compare the resume with the job description
  - Calculate a **match percentage**
  - Identify **matched** and **missing skills**
  - Provide a **recommendation** on candidate fit

- The model used is `google/flan-t5-base`, loaded using HuggingFace's `transformers` and integrated via LangChain's `HuggingFacePipeline`.

- The entire chain is saved using `pickle` and reused in the Streamlit frontend.

---

### Example Prompt Template:

```text
You are an expert recruiter. Compare the following resume with the job description.

Resume:
{resume}

Job Description:
{jd}

Answer:
1. Match percentage (0-100)?
2. List top matched skills.
3. List missing/weak skills.
4. Is this candidate a good fit? Why?
