Sure!
Here’s your README text in one plain .txt file format — copy-paste into README.txt (or README.md if you prefer):

⸻

📄 ChatMyDocs — Multi-PDF AI Chatbot

Unlock insights from your documents with intelligent, context-aware Q&A.

⸻

🌟 Overview

ChatMyDocs is an AI-powered assistant that lets users upload multiple PDFs and ask natural language questions.
The system extracts content, stores it in a vector database, retrieves relevant chunks, and answers using a Large Language Model.

Built with:
• FastAPI
• Streamlit
• LangChain
• ChromaDB
• HuggingFace Embeddings
• Groq Llama 3

⸻

✨ Features
• Upload multiple PDFs
• Automatic text extraction, chunking, and embedding
• Stores embeddings in a persistent Chroma database
• Ask questions based ONLY on your documents
• Session memory remembers chat history per user
• Simple web UI using Streamlit
• Clean modular architecture (frontend + backend + RAG engine)

⸻

🧱 Tech Stack

Frontend: Streamlit
Backend API: FastAPI
RAG Framework: LangChain
LLM: Groq (Llama 3.3)
Embeddings: HuggingFace MiniLM
Vector Store: ChromaDB
Session Memory: RunnableWithMessageHistory

⸻

📦 Installation
	1.	Clone repository
git clone https://github.com/Gagan-Mk/ChatMyDocs.git
cd ChatMyDocs
	2.	Create virtual environment
python3 -m venv venv
source venv/bin/activate
	3.	Install dependencies
pip install -r requirements.txt
	4.	Add API keys
Create .env file with:
GROQ_API_KEY=your_key
HF_TOKEN=your_huggingface_key
LANGCHAIN_API_KEY=your_key
LANGCHAIN_PROJECT=ChatMyDocs

⸻

▶️ Run Locally

Start FastAPI backend:
uvicorn Main:app –reload

Start Streamlit UI:
streamlit run app.py

Visit API docs:
http://127.0.0.1:8000/docs

⸻

🧠 How It Works
	1.	User uploads PDF files in Streamlit
	2.	Backend extracts text and splits it into chunks
	3.	Embeddings are generated and stored in Chroma
	4.	User sends query + session ID
	5.	Retriever selects top chunks
	6.	Llama model generates grounded answer
	7.	Memory preserves conversation flow

⸻

🗂 Project Structure
ChatMyDocs/
├── app.py (Streamlit UI)
├── Main.py (FastAPI backend)
├── Rag_pipline.py (RAG logic)
├── Rag_store/ (Local vector database)
├── requirements.txt
└── README.txt

⸻

👨‍💻 Author
Gagan MK
PES University

