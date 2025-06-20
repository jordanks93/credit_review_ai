# processor.py
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from security import decrypt_file
import tiktoken

# Load environment variables from .env file if present
load_dotenv()

# Confirm API key is available
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not set in environment or .env file")

# Ensure tokenizer is locally cached to avoid online download
try:
    tiktoken.get_encoding("cl100k_base")
except Exception as e:
    raise RuntimeError("Tokenizer not found locally. Run this script once with internet access.") from e

llm = ChatOpenAI(temperature=0, openai_api_key=api_key)

def detect_section_type(text):
    lowered = text.lower()
    if "paynet" in lowered or "credit report" in lowered:
        return "credit_report"
    elif "application" in lowered:
        return "credit_application"
    elif "sales order" in lowered:
        return "sales_order"
    elif "tax" in lowered or "irs" in lowered:
        return "tax_return"
    elif "balance sheet" in lowered or "income statement" in lowered:
        return "financial_statement"
    elif "personal financial" in lowered:
        return "personal_financial"
    return "generic"

def get_prompt_for_section(section_type):
    prompts = {
        "credit_report": "Summarize the credit score, payment history, and red flags.",
        "credit_application": "Summarize the applicant's requested terms, business type, and ownership.",
        "sales_order": "Summarize vehicle details and transaction amount.",
        "tax_return": "Summarize income, expenses, and tax trends.",
        "financial_statement": "Summarize assets, liabilities, revenue, and key ratios.",
        "personal_financial": "Summarize personal net worth and liabilities.",
        "generic": "Summarize the financial health of this business."
    }
    return prompts.get(section_type, prompts["generic"])

def process_document(encrypted_path):
    decrypted_path = decrypt_file(encrypted_path)
    loader = PyPDFLoader(decrypted_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    # Attempt to detect document type from content sample
    joined_text = " ".join([c.page_content[:1000] for c in chunks])
    section_type = detect_section_type(joined_text)
    prompt = get_prompt_for_section(section_type)

    chain = load_qa_chain(llm, chain_type="map_reduce")
    response = chain.run(input_documents=chunks, question=prompt)

    if "unable to provide" in response.lower():
        return "This PDF may be too long or disorganized. Try uploading specific sections separately."

    return response
