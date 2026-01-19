from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

def simple_rag(question: str, document_text: str) -> str:
    """
    Naive RAG using Gemini:
    - Entire document is passed to LLM
    - No retrieval
    """

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    prompt = f"""
    You are a helpful assistant.
    Answer ONLY using the document below.

    Document:
    {document_text}

    Question:
    {question}
    """

    response = llm.invoke(prompt)
    return response.content
