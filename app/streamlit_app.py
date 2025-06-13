# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="Credit Analysis AI", layout="centered")
st.title("📊 Credit Risk Analyzer")

st.markdown("Upload a PDF credit document (e.g., bank statement, tax return) to summarize financial health.")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Processing document securely..."):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
        response = requests.post("http://localhost:8000/upload", files=files)

    if response.status_code == 200:
        summary = response.json().get("summary", "No summary returned.")
        st.subheader("AI Credit Summary")
        st.write(summary)
    else:
        st.error("Error processing file. Please try again.")