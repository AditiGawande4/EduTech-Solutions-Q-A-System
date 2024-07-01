import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("EduTech Q&A 💻")

st.text("Shoot your question about EduTech")
question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
