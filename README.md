# README.md
# 📊 Secure Credit Risk AI App

This project uses AI to automate credit analysis for commercial finance in the trucking industry. It allows users to securely upload PDF financial documents (e.g. tax returns, bank statements, credit reports), which are encrypted, processed by a GPT-based LLM, and summarized for risk review.

---

## 🔧 Features

- 🔐 Secure document handling with encryption (AES via Fernet)
- 🤖 LLM-powered document analysis using LangChain + OpenAI GPT
- 📄 PDF ingestion and summarization
- 🖥️ Streamlit front-end to upload and view summaries
- ⚙️ FastAPI backend for processing and storage

---

## 📁 Project Structure

```
your-project/
├── app/
│   ├── main.py              # FastAPI backend
│   ├── processor.py         # LangChain + OpenAI logic
│   ├── security.py          # File encryption utilities
│   ├── streamlit_app.py     # Streamlit UI
│   └── requirements.txt     # Dependencies
├── uploads/                 # Encrypted file storage
├── .env                     # Environment variables (API key)
├── venv/                    # Python virtual environment
└── README.md                # This file
```

---

## 🚀 Getting Started

### 1. Clone the repository and navigate to it

```bash
git clone https://github.com/your-user/secure-credit-ai.git
cd secure-credit-ai
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
cd app
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

Create a `.env` file in the root of the project (**not** inside `/app`) with this content:

```
OPENAI_API_KEY=your-api-key-here
```

> 🔒 Your key will be loaded automatically via `python-dotenv`.

---

## ▶️ Running the App

### 1. Start the FastAPI backend

In the `app/` directory:

```bash
uvicorn main:app --reload
```

### 2. Start the Streamlit frontend (in a second terminal)

Also from the `app/` directory:

```bash
streamlit run streamlit_app.py
```

### 3. Open the browser:

Visit [http://localhost:8501](http://localhost:8501) and upload a PDF to analyze.

---

## 🔐 Security Notes

- Uploaded files are encrypted using AES (`cryptography.Fernet`) before storage.
- Files are decrypted temporarily only for analysis.
- You should enable HTTPS, authentication, and access control before deploying.

---

## 🧪 Testing API (Optional)

FastAPI's Swagger docs available at:
[http://localhost:8000/docs](http://localhost:8000/docs)

You can test the `/upload` route directly with PDF files.

---

## 📌 Requirements

- Python 3.8+
- OpenAI API Key (GPT-4 or GPT-3.5)
- OS: Windows, macOS, or Linux

---

## 🛠 Future Enhancements (Optional Ideas)

- User authentication (e.g., OAuth, JWT)
- Persistent storage (PostgreSQL, S3, etc.)
- Deal tracking dashboard
- Built-in scoring & approval workflows

---

## 📄 License

This project is for internal use or testing only. Not for redistribution.

---

## 🤝 Credits

Built with:
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://platform.openai.com/)
- [cryptography](https://cryptography.io/)
