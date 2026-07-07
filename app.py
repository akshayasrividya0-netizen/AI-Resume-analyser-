import streamlit as st

st.title("AI Resume Analyzer")

st.write("Welcome to AI Resume Analyzer")

resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

job = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume and job:
        st.success("Resume uploaded successfully!")
        st.write("Job Description:")
        st.write(job)
    else:
        st.warning("Please upload a resume and enter a job description.")
