

import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, Configure, DataType
from dotenv import load_dotenv
load_dotenv()
from src.helper_function import connect_to_weaviate,create_collections,load_doc,split_doc,insert_chunk



def ingest_doc(file_path:str):
    client=connect_to_weaviate()
    try:
        if client.collections.exists("p3_data"):
            print("Collection already exists")
        else:
            create_collections(client)
    # Loading documents for vectorization
        document=load_doc(file_path)
    # Splitting the douments
        chunks=split_doc(document)
    # Getting the collection here
        get_collection = client.collections.get("p3_data")
    # Inserting doc as chunks to collection
        for chunk in chunks:
            chunk_insertion_status=insert_chunk(get_collection,chunk=chunk, max_retry=3)
            if chunk_insertion_status:
                print("success")
            else:
                print("failed")
            
    finally:
        client.close()