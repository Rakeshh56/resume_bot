import os
import streamlit as st
import pickle
import fitz  # PyMuPDF

# ------------------ PDF Parser ------------------ #
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# ------------------ Load Pickled LangChain Chain ------------------ #
with open("resume_chain.pkl", "rb") as f:
    chain = pickle.load(f)

# ------------------ Streamlit UI ------------------ #
st.set_page_config(page_title="Resume Screener Bot", layout="centered")
st.title("🤖 Resume Screener Bot")
st.markdown("Upload your resume and tell us about your dream job to see how well you match!")

# Upload resume
resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type="pdf")

# Enter job description or role
job_desc = st.text_area("💼 Paste Job Description / Role You Want")

# Analyze Button
if st.button("🧠 Analyze Resume"):
    if resume_file is None or not job_desc.strip():
        st.warning("Please upload your resume and enter job details.")
    else:
        with st.spinner("Reading and analyzing your resume..."):
            # Save uploaded resume temporarily
            temp_path = "uploaded_resume.pdf"
            with open(temp_path, "wb") as f:
                f.write(resume_file.read())

            # Extract text
            resume_text = extract_text_from_pdf(temp_path)

            # ✅ Delete temp file
            os.remove(temp_path)

            # Run through LLM chain
            result = chain.run(resume=resume_text, jd=job_desc)

            st.success("✅ Analysis Complete")
            st.subheader("🔍 Your Resume Analysis:")
            st.markdown(result)
