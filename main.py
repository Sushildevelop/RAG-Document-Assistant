
import streamlit as st
from document_loader import load_document,load_pdf
import tempfile
from rag import simple_rag
st.title("📄 ManagESG")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])


# document_text = load_document("sample.pdf")

document_text=None
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    document_text = load_pdf(temp_file_path)
    st.success("PDF uploaded and processed successfully!")

    with st.expander("📄 Preview Extracted Text"):
        st.text(document_text) 


question = st.text_input("Ask a question based on document")

# if question:
#     answer = simple_rag(question, document_text)
#     st.subheader("Answer")
#     st.write(answer)

if question and document_text:
    with st.spinner("Thinking..."):
        answer = simple_rag(question, document_text)
        st.subheader("Answer")
        st.write(answer)