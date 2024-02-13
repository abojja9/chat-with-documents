import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
# from langchain_community.vectorstores.chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain 
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader
import logging
logger = logging.getLogger(__name__)


load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # Define the GOOGLE_API_KEY variable
OPENAI_API_KEY = os.environ.get("GOOGLE_API_KEY")  
genai.configure(api_key=GOOGLE_API_KEY)
LLM_COMPANY = os.environ.get("LLM_COMPANY")
FAISS_INDEX_PATH = os.environ.get("FAISS_INDEX_PATH")

if "openai" in LLM_COMPANY:
    EMBEDDINGS =  OpenAIEmbeddings()
    LLM_NAME = ChatOpenAI()
elif "google" in LLM_COMPANY:
    EMBEDDINGS =  GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
    LLM_NAME = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=1000
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore_from_pdf(pdf_docs):
    text = get_pdf_text(pdf_docs)
    chunks = get_text_chunks(text)
    vector_store = get_vectorstore(chunks)
    return vector_store

def get_vectorstore(document_chunks):
    # Check if the FAISS index already exists
    # if os.path.exists(FAISS_INDEX_PATH):
    #     logger.info(f"Loading existing FAISS index from {FAISS_INDEX_PATH}")
    #     vector_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings=EMBEDDINGS)  # Load the existing index
    #     vector_store.add_texts(document_chunks)  # Add the new documents
    # else:
    vector_store = FAISS.from_texts(document_chunks, 
                                            EMBEDDINGS)
    vector_store.save_local(FAISS_INDEX_PATH)
    print("FAISS index created and saved")
    print(vector_store)
    return vector_store

def get_vectorstore_from_url(url):
    # get the text in document
    loader = WebBaseLoader(url)
    document = loader.load()

    # split the document to chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    document_chunks = text_splitter.split_documents(document)
    vector_store = FAISS.from_documents(document_chunks, 
                                            EMBEDDINGS)
    vector_store.save_local(FAISS_INDEX_PATH)
    # vector_store = Chroma.from_documents(
    #     document_chunks, EMBEDDINGS
    # )
    return vector_store


def get_context_retriever_chain(vector_store):
    llm = LLM_NAME
    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        (
            "user",
            "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation",
        ),
    ])
    
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    return retriever_chain


def get_conversational_rag_chain(retriever_chain):
    llm = LLM_NAME
    prompt = ChatPromptTemplate.from_messages([
            (
            "system",
            "Answer the user's questions based on the below context:\n\n{context}"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ])
    
    stuff_documents_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever_chain, stuff_documents_chain)


def get_response(vector_store, chat_history, user_query):
    retriever_chain = get_context_retriever_chain(vector_store)
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    
    response = conversation_rag_chain.invoke({
        "chat_history": chat_history,
        "input": user_query
    })
    
    return response['answer']


def get_conversational_chain_gemini():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.5)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(vector_store, chat_history, user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    # retriever = vector_store.as_retriever()
    new_db = FAISS.load_local("./data_dir/faiss_index", embeddings)
    docs = new_db.similarity_search(user_question, k=9)

    chain = get_conversational_chain_gemini()

    
    response = chain(
        {"input_documents":docs, "question": user_question, "chat_history": chat_history}
        )
    # print(response)
    return response["output_text"]