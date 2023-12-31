from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
#from langchain.templates import PromptTemplate
#from jinja2 import Template
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

from llama_index.node_parser import SimpleNodeParser
from llama_index.text_splitter import TokenTextSplitter
from llama_index import Document
import os

def creat_db(embeddings):

    '''loader = DirectoryLoader('./model/data/',
                            glob="*.md",  # Assuming your text files have a .txt extension
                            loader_cls=TextLoader
                            )
    documents = loader.load()'''
    # Split text from PDF into chunks
    '''text_splitter = RecursiveCharacterTextSplitter(chunk_size=9000,
                                                chunk_overlap=70
                                                )
    texts = text_splitter.split_documents(documents)
    print("======================")
    print(texts)
    # Build and persist FAISS vector store'''


    text_splitter = TokenTextSplitter(
        separator="\n",
        chunk_size=1024,
        chunk_overlap=20,
        backup_separators=["\n\n", ".", ","]
    )

    node_parser = SimpleNodeParser(text_splitter=text_splitter)
    nodes = node_parser.get_nodes_from_documents(
        [Document(text='./model/data/')], show_progress=True)
    print(nodes)

    # build index
   # index = VectorStoreIndex(nodes)
    #print(index)

    print("Index created!")
    
    #vectorstore = FAISS.from_documents(texts, embeddings)
    #return vectorstore.save_local('vectorstore/db_faiss')
    return nodes