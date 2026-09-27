
# import os
# import weaviate
# from weaviate.classes.init import Auth
# from weaviate.classes.config import Configure,Property,DataType
# from src.helper_function import create_collections
from dotenv import load_dotenv
load_dotenv()
from src.tools.data_loader_function import ingest_doc
doc_path=r"C:\Users\aksha\Downloads\ANS Institution - Text Prospectus 2027.pdf"
ingest_doc(doc_path)