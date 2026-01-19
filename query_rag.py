from pinecone_client import index
from embedding_function_chunks import get_embedding
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def query_rag(question:str, top_k:int=5, namespace="pdf")->str:
    """
    1. Embed the question
    2. Query Pinecone for top_k similar chunks
    3. Retrieve top chunks
    4. Pass to Gemini LLM
    """
    query_embedding=get_embedding(question)
    results=index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
        namespace=namespace
    )
    # Combine top chunks
    context = "\n".join([
        f"[Page {m.metadata['page']}] {m.metadata['text']}"
        for m in results.matches
    ])

    #pass to gemini llm
    api_key=os.getenv("GOOGLE_API_KEY")
    llm=ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        google_api_key=api_key,
    )
    prompt=f"""
    You are a helpful assistant.
    Answer only using the document below.
    Document:
    {context}

    Question:
    {question}
    """
    response = llm.invoke(prompt)
    return response.content


