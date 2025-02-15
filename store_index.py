from  src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
print(PINECONE_API_KEY)

#1
extracted_data = load_pdf("data/")

#2
text_chunks = text_split(extracted_data)
print("length of my chunk:", len(text_chunks))

#3
embeddings = download_hugging_face_embeddings()



#4
#Initializing the Pinecone
#pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
pinecone.init(api_key=PINECONE_API_KEY)


index_name = "medical-chatbot"

#Creating Embeddings for Each of the Text Chunks and storing
docsearch = Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)
