from src.helper import load_pdf_file,text_split,download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from  dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY =os.getenv('PINECONE_API_KEY')
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY
os.environ['PINECONE_API_KEY']=PINECONE_API_KEY

extracted_data=load_pdf_file(file='data/')
text_chunks=text_split(extracted_data)
print(len(text_chunks))
embedding=download_hugging_face_embeddings()

#Pinecone initialise
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-bot"

pc.create_index(
    name=index_name,
    dimension=1536, # OpenAi input diamension
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embedding,
)
