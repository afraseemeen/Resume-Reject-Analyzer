import streamlit as st

st.set_page_config(
    page_title="Resume Rejection Analyzer",
    page_icon=" ",
    layout="wide",)
st.write(
         "Find Potential Weaknesses in Your Resume"
         "and improve its matching with job descriptions."
)
st.info(
    "This tool analyzes your resume and provides feedback on how well" \
    "it matches with job descriptions."
)
resume = st.file_uploader(
                          "Upload your resume (PDF or DOCX)", 
type=["pdf", "docx"])
job_description = st.text_area(
    "Enter the job description",
    heigth= 200,
    placeholder="Paste the job description here..."
)
if st.button("Analyze Resume", type="primary"):
    if resume is None:
        st.error("Please upload your resume.")
    elif not job_description.strip():
        st.error("Please enter the job description.")
    else:
        st.success("Resume analysis completed successfully!")
        st.write("Resume file:", resume.name)
        st.write("Job description:", len(job_description))
        st.write(" Next , we will add resume text extraction" \
"Skill matching and improvemnt suggestions based on the analysis.")
