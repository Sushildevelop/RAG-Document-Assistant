
import fitz

def load_pdf_chunks(file_path:str, chunk_size:int=500)->list:
    """
    Load PDF and split into chunks  
    - Chunk size : number of words per chunk
    """
    doc=fitz.open(file_path)
    chunks=[]
    for page_number, page in enumerate(doc, start=1):
        text=page.get_text()
        if not text.strip():
            continue
        words=text.split()

        # Split page into chunks
        for i in range(0, len(words),chunk_size):
            chunk_text=" ".join(words[i:i+chunk_size])
            chunks.append({
                "page":page_number,
                "text":chunk_text
            })
    return chunks

