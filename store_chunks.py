import uuid
from pinecone_client import index
from embedding_function_chunks import get_embedding

def store_chunks_to_pinecone(chunks:list, namespace="pdf"):
    vectors=[]
    for chunk in chunks:
        vec=get_embedding(chunk['text'])
        vectors.append({
            "id":str(uuid.uuid4()),
            "values":vec,
            "metadata":{
                "page":chunk['page'],
                "text":chunk['text']
            }

        })
    # Upsert to Pinecone
    batch_size=100
    for i in range(0, len(vectors), batch_size):
        batch=vectors[i:i+batch_size]
        index.upsert(vectors=batch, namespace=namespace)


def upsert_chunks(vectors, namespace="pdf"):
    index.upsert(vectors=vectors, namespace=namespace)