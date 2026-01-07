import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"
session_id = "gagan"   # later generate real ones

st.title("RAG Chatbot")

# Upload PDFs
files = st.file_uploader("Upload PDFs", accept_multiple_files=True)
if files:
    for f in files:
        res = requests.post(
            f"{API_BASE}/upload",
            files={"files": f.getvalue()}
        )
    st.success("Upload complete!")

# Chat
question = st.chat_input("Ask something")
if question:
    res = requests.get(
        f"{API_BASE}/chat",
        params={"q": question, "session_id": session_id}
    )
    st.write(res.json()["answer"])