import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
import sys
import os
from pathlib import Path

# get current working directory
project_dir = Path(__file__).resolve().parents[1]
# get the absolute path of the project directory
project_dir = os.path.abspath(project_dir)
# add the project directory to sys.path
sys.path.append(project_dir)
from backend.app import LLM_COMPANY, get_context_retriever_chain, get_conversational_rag_chain, get_response, get_vectorstore_from_pdf, get_vectorstore_from_url, user_input


# app config
st.set_page_config(page_title="Chat with documents", page_icon=":shark:", layout="wide")
st.title("Chat with documents")


# sidebar
with st.sidebar:
    st.header("Settings")
    input_type = st.selectbox("Select input type", ["Website URL", "PDF"], key="input_type")
    if input_type == "Website URL":
        website_url = st.text_input("Website URL")
        pdf_docs = None
    else:
        website_url = None
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)

if (website_url is None or website_url == "") and (pdf_docs is None or len(pdf_docs) == 0):
    st.info("Please enter a website URL or upload a PDF file.")
else:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I'm your document assistant. How can I help you?")
        ]
    if "vector_store" not in st.session_state:
        # vector_store = get_vectorstore_from_url(website_url)
        if website_url is not None and website_url != "":
            vector_store = get_vectorstore_from_url(website_url)
        elif pdf_docs is not None and len(pdf_docs) > 0:
            vector_store = get_vectorstore_from_pdf(pdf_docs)
        else:
            vector_store = None
        st.session_state.vector_store = vector_store
    
    # retriever_chain = get_context_retriever_chain(st.session_state.vector_store)
    # conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    
    # user input
    user_query = st.chat_input("Type your question here...")
    if user_query is not None and user_query != "":
        if "openai" in LLM_COMPANY:
            response = get_response(st.session_state.vector_store,
                                    st.session_state.chat_history,
                                    user_query)
        elif "google" in LLM_COMPANY:
            response = user_input(st.session_state.vector_store,
                                    st.session_state.chat_history,
                                    user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))


    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        if isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
