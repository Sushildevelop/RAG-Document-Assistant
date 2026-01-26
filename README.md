# 🧠 RAG-Document-Assistant  

A powerful Retrieval-Augmented Generation (RAG) system that allows users to upload documents and chat with them using semantic search, embeddings, chunking, and LLM-based answers.

This project is designed from **beginner setup to advanced production-level RAG architecture**.

---

## 🚀 Features

- 📂 Upload files (PDF, TXT, DOCX, CSV, etc.)
- ✂️ Intelligent text chunking
- 🔢 Embedding generation
- 🧬 Vector database storage
- 🔍 Semantic search
- 🤖 LLM-based answer generation
- 📊 Metadata-based filtering
- 🗃️ Multi-document support
- 🔄 Re-indexing & caching
- ⚡ FastAPI backend ready
- 🌐 Frontend-ready APIs

---

## 🏗️ RAG Architecture Overview

```text
User Query
   ↓
Semantic Search (Vector DB)
   ↓
Top-k Relevant Chunks
   ↓
LLM Prompt + Context
   ↓
Final Answer


🛠️ Tech Stack
Layer	Tech
Backend	Python, FastAPI
LLM	OpenAI / Claude / Gemini / Local LLM
Embeddings	OpenAI / SentenceTransformers
Vector DB	FAISS / Chroma / Weaviate / Pinecone
Parsing	PyPDF, LangChain, Unstructured
Storage	Local / S3
Frontend	React / Next.js

📦 Project Structure
bash
Copy code
RAG-Document-Assistant/
│
├── app/
│   ├── api/            # FastAPI routes
│   ├── services/       # RAG logic
│   ├── embeddings/     # Embedding models
│   ├── vectorstore/    # FAISS/Chroma logic
│   ├── loaders/        # File parsers
│   ├── chunking/       # Text splitters
│   ├── prompts/        # Prompt templates
│   └── config.py
│
├── data/
│   ├── uploads/
│   └── vector_db/
│
├── requirements.txt
└── README.md


⚙️ Installation
bash
Copy code
git clone https://github.com/yourname/RAG-Document-Assistant.git
cd RAG-Document-Assistant

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
🔑 Environment Variables
Create .env

env
Copy code
OPENAI_API_KEY=your_api_key
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-4o-mini
📂 Step 1: Document Loading
python
Copy code
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("file.pdf")
docs = loader.load()


✂️ Step 2: Chunking Strategy
Why chunking?
LLMs cannot process long documents directly. Chunking improves retrieval accuracy.

python
Copy code
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = splitter.split_documents(docs)
Best Practices:

chunk_size: 300–800 tokens

chunk_overlap: 10–20%

Smaller chunks = better precision

Larger chunks = better context

🔢 Step 3: Embeddings
Embeddings convert text → vectors.

python
Copy code
from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
Alternatives:

SentenceTransformers

BAAI/bge-large

all-MiniLM-L6-v2

🧬 Step 4: Vector Store
FAISS Example:

python
Copy code
from langchain.vectorstores import FAISS

db = FAISS.from_documents(chunks, embeddings)
db.save_local("data/vector_db")
Chroma Example:

python
Copy code
from langchain.vectorstores import Chroma

db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma")
🔍 Step 5: Semantic Search
python
Copy code
query = "Explain transformer architecture"
docs = db.similarity_search(query, k=4)
Advanced:

python
Copy code
db.similarity_search_with_score(query)


🤖 Step 6: RAG Answer Generation
python
Copy code
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(temperature=0)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

qa.run("What is attention mechanism?")


🧠 Prompt Engineering (Advanced)
python
Copy code
SYSTEM_PROMPT = """
You are a document assistant.
Use only the given context.
If answer not found, say 'Not in documents'.
"""

🧩 Advanced RAG Concepts
Concept	Description
Hybrid Search	Keyword + vector search
Re-ranking	Improve result accuracy
Metadata filtering	Filter by file, date, category
Context compression	Reduce irrelevant tokens
Agentic RAG	Tool-using RAG system
Streaming responses	Real-time UI updates
Multi-Vector Retrieval	Tables, code, images

🧠 Chunk Optimization Techniques
Semantic chunking

Sliding window chunking

Markdown header chunking

Title-aware chunking

🗂️ Metadata Example
python
Copy code
doc.metadata = {
  "source": "report.pdf",
  "page": 3,
  "category": "finance"
}
Then:

python
Copy code
db.similarity_search(query, filter={"category": "finance"})


⚡ Performance Tips
Cache embeddings

Batch processing

Async FastAPI routes

Use GPU for embedding

Index compression (HNSW, IVF)

🌐 API Example
python
Copy code
POST /upload
POST /chat
GET  /documents
DELETE /documents/{id}

🛡️ Security
File validation

Size limits

Auth middleware

Rate limiting

Prompt injection protection

📈 Future Enhancements
UI Dashboard

Drag & drop uploads

RAG evaluation metrics

Agentic workflows

OCR for scanned PDFs

Multilingual embeddings

venv- source .venv/bin/activate
