
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.embeddings import HuggingFaceEmbeddings
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings

#Extract data from pdf file 
def load_pdf_file(file):
    loader=DirectoryLoader(file,        glob='*.pdf',    loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents



#Split data into chunks
def text_split(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks


#vector embedding
def download_hugging_face_embeddings():
  embedding= OpenAIEmbeddings()
  #HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')# 384 diamensional vector - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
  return embedding

