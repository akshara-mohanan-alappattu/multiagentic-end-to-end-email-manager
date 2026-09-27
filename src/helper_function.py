import os
import time
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure,Property,DataType
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

# Function to exract content from LLM response
def json_content_extractor(content):
    starting_index=content.find("{")
    ending_index=content.rfind("}")+1
    extracted_content=content[starting_index:ending_index]
    return extracted_content

# Loading documents for vectorization
def load_doc(file_path:str):
    try:
        loader=PyPDFLoader(file_path)
        document=loader.load()
        print("*"*40+"Document Loaded"+"*"*40)
        return document
    except Exception:
        raise
# Splitting of document into chunks
def split_doc(document):
    try:
        splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
        chunks=splitter.split_documents(document)
        print("*"*40+"Document splitted to chunks"+"*"*40)
        return chunks
    except Exception:
        raise

# Funtion for Connecting to Weaviate Cloud
def connect_to_weaviate():
    print("*"*40+ "Connect to Weaviate function initiated"+"*"*40)
    weaviate_url = os.environ["WEAVIATE_URL"]
    weaviate_api_key = os.environ["WEAVIATE_API_KEY"]

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key),
    )
    print("*"*40+ "Client Connected"+"*"*40)
    return client

# Creating Collection
# Source_properties=This tells Weaviate which property should be converted into an embedding/vector.

def create_collections(client):
    print("*"*40+ "Create Collection function initiated"+"*"*40)
    collection=client.collections.create(
        name="p3_data",
        properties=[
            Property(name="title", data_type=DataType.TEXT),
            Property(name="content", data_type=DataType.TEXT)
        ],
        vector_config=[Configure.Vectors.text2vec_weaviate(
            name="text_vector",
            source_properties=["content"],)
            ],
        )
    print("*"*40+ "Collection created"+"*"*40)
    return collection

# Document/chunk insertion function
def insert_chunk(get_collection,chunk, max_retry=3):
    print("vector collection brought")
    for attempt in range(1,max_retry+1):
        try:
            get_collection.data.insert(
                properties={
                "title": chunk.metadata.get("source","Unknown"),
                "content": chunk.page_content
                }
                )
            print("*"*40+"Chunk inserted in collection successfuly"+"*"*40)
            return True
        except Exception as e:
            print(f"error while inserting chunk to collection :{e}")
            if attempt<max_retry:
                waiting_time=2**(attempt-1)
                time.sleep(waiting_time)
    return False
        