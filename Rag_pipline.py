import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage
import fitz
from dotenv import load_dotenv
load_dotenv()

os.environ['LANCHAIN_TRACING_V2'] = 'true'  
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')

groq_api_key = os.getenv('GROQ_API_KEY')

class Rag():
    def __init__(self):
        self.model = ChatGroq(model='llama-3.3-70b-versatile', api_key=groq_api_key)
        self.embeddings = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2')
        self.splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
        self.vectordb = Chroma(embedding_function=self.embeddings, persist_directory='Rag_store')
        
    def ingest(self, pdf_bytes_list):
        all_chunks = []

        for pdf_bytes in pdf_bytes_list:
            pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

            # Convert pages to Document objects
            docs = [
                Document(
                    page_content=page.get_text(),
                    metadata={"page": page.number}
                )
            for page in pdf]

            chunks = self.splitter.split_documents(docs)
            all_chunks.extend(chunks)

        # Add all chunks to vector db
        self.vectordb.add_documents(all_chunks)
        
        return len(all_chunks)
    
    def chat(self, messages : str, session_id : str):
        
        retriever = self.vectordb.as_retriever()
        
        system_message = """ 
            You are a helpful and a intelligent assistent. Answer the question based on the provided
            context only. If you do not know the answer, reply with ' i don't know'.Make the answer beautiful
            by using emojis.
            
            {context}
        """
        
        prompt = ChatPromptTemplate.from_messages(
            [
                ('system',system_message),
                MessagesPlaceholder(variable_name='messages')
            ]
        )
        
        def extract_query(messages):
            return messages[-1].content

        # building chain
        chain = {
            "context": RunnableLambda(extract_query) | retriever,
            "messages": RunnablePassthrough()
        } | prompt | self.model 
        
        # building sessin history
        store = {}
        def get_session_history(session_id : str)->BaseChatMessageHistory:
            if session_id not in store:
                store[session_id] = ChatMessageHistory()
            return store[session_id]
        
        message_hist_chain = RunnableWithMessageHistory(chain,get_session_history)
        
        response = message_hist_chain.invoke(
            {"messages": messages},
            config={"configurable": {"session_id": session_id}},
        )
        
        return response.content    
    
    
        
            
        
        
        
        
        
        
        
    
        
        
    