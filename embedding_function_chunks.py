from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings  # Gemini-compatible
import os
from dotenv import load_dotenv

load_dotenv()

def get_embedding(text:str)->list:
    """
    Get Embedding for a text using Gemini
    """
    api_key=os.getenv("GOOGLE_API_KEY")
    embedding_model=GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=api_key
    )
    vector=embedding_model.embed_query(text)
    return vector
