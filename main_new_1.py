import streamlit as st
import tempfile
from document_loader_chunks import load_pdf_chunks
from store_chunks import store_chunks_to_pinecone
from query_rag import query_rag

st.set_page_config(page_title="📄 ManagESG Chat", page_icon="🤖")

st.title("📄 ManagESG Chat Assistant (RAG)")

# -----------------------------
# PDF Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_path = temp_file.name

    chunks = load_pdf_chunks(temp_path)
    store_chunks_to_pinecone(chunks)
    st.success("PDF uploaded, processed into chunks, and stored in Pinecone!")

# -----------------------------
# Initialize chat history
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Display chat messages
# -----------------------------
for chat in st.session_state.chat_history:
    st.chat_message("user").write(chat["question"])
    st.chat_message("assistant").write(chat["answer"])

# -----------------------------
# Input new question
# -----------------------------
if prompt := st.chat_input("Ask a question"):
    # Display user's message immediately
    st.chat_message("user").write(prompt)

    # Get the RAG answer
    with st.spinner("Thinking..."):
        answer = query_rag(prompt)

    # Display assistant's response
    st.chat_message("assistant").write(answer)

    # Save to session state
    st.session_state.chat_history.append({"question": prompt, "answer": answer})
