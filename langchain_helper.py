import os
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()


llm = GoogleGenerativeAI(model="models/text-bison-001",google_api_key=st.secrets["GOOGLE_API_KEY"], temperature=0)
instructor_embeddings= HuggingFaceInstructEmbeddings()
vectordb_file_path="faiss_index"

def create_vector_db():
    try:
        loader = CSVLoader(file_path='codebasics_faqs.csv', source_column='prompt', encoding='ISO-8859-1')
        docs = loader.load()
    except UnicodeDecodeError:
    # If ISO-8859-1 fails, try cp1252 encoding
        loader = CSVLoader(file_path='codebasics_faqs.csv', source_column='prompt', encoding='cp1252')
        docs = loader.load()
    vectordb=FAISS.from_documents(documents=docs, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    vectordb=FAISS.load_local(vectordb_file_path, embeddings=instructor_embeddings, allow_dangerous_deserialization=True)
    retriever=vectordb.as_retriever(score_threshold=0.7)
    

    prompt_template="""Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT:{context}

    QUESTION:{question}"""

    PROMPT=PromptTemplate(
    template=prompt_template,input_variables=["context","question"]
    )

    chain=RetrievalQA.from_chain_type(
                                llm=llm,
                                chain_type="stuff",
                                retriever=retriever,
                                input_key="query",
                                return_source_documents=True,
                                chain_type_kwargs={"prompt": PROMPT })
    return chain

if __name__=="__main__":
    chain=get_qa_chain()
    #print(chain())