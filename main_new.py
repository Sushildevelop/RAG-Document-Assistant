import streamlit as st
import tempfile
from document_loader_chunks import load_pdf_chunks

from store_chunks  import store_chunks_to_pinecone
from query_rag import query_rag

st.title("📄 ManagESG with RAG and Chunks")

uploaded_file=st.file_uploader("Upload a PDF file",type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_path=temp_file.name

    chunks=load_pdf_chunks(temp_path)
    store_chunks_to_pinecone(chunks)
    st.success("PDF uploaded, processed into chunks, and stored in Pinecone!")

# Initialize chat history in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


question=st.text_input("Ask a question",key="input_question")

if question:
    with st.spinner("Thinking..."):
        
        answer=query_rag(question)

        # Save to chat history
        st.session_state.chat_history.append({"question": question, "answer": answer})

        # st.subheader("Answer")
        # st.write(answer)

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['question']}")
    st.markdown(f"**Bot:** {chat['answer']}")
    st.markdown("---")  # separator