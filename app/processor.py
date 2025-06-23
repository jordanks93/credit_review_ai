# processor.py
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from security import decrypt_file

# Load environment variables from .env file if present
load_dotenv()

# Confirm API key is available
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not set in environment or .env file")

llm = ChatOpenAI(temperature=0, openai_api_key=api_key)

def process_document(encrypted_path):
    decrypted_path = decrypt_file(encrypted_path)
    loader = PyPDFLoader(decrypted_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=chunks, question="Can you give me a detailed credit risk analysis on this credit package from the perspective of a commercial credit analyst that will be presenting this deal to the CEO?")
    return response