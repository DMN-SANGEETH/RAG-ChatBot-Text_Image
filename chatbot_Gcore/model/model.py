from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
#from langchain.templates import PromptTemplate
#from jinja2 import Template
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import os
from langchain.vectorstores import FAISS
from .createDb import creat_db
from .promptTemplate import qa_template
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA




os.environ["OPENAI_API_KEY"] = "sk-0000000000000000000000000000000000000000"
embeddings = OpenAIEmbeddings()

# Check if the directory exists before creating the database
if not os.path.exists('./model/vectorstore/db_faiss'):
    creat_db(embeddings)
#gpt-3.5-turbo

llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0.07)

def set_qa_prompt():
    prompt = PromptTemplate(template=qa_template,
                            input_variables=['context', 'question']
                            )
    return prompt

def build_retrieval_qa(llm, prompt, vectordb):
    modeldb = RetrievalQA.from_chain_type(llm=llm,
                                          chain_type='stuff',
                                          retriever=vectordb.as_retriever(search_kwargs={'k':4}),
                                          return_source_documents=True,
                                          chain_type_kwargs={'prompt': prompt}
                                          )
    return modeldb

def setup_dbqa(llm, embeddings):
    vectordb = FAISS.load_local('./vectorstore/db_faiss', embeddings)
    qa_prompt = set_qa_prompt()
    model_qa = build_retrieval_qa(llm, qa_prompt, vectordb)
    return model_qa

# Call the setup_dbqa function to create the model_qa
model_qa = setup_dbqa(llm, embeddings)

#get_response("What are the ways users get notified if API token got expired?")

def get_response(question):
    result = model_qa({'context': 'Gcore Product Documentation, Explore product functionality, configuration, and troubleshooting guides.', 'query': question})
    print(result['result'] )
    answer = result['result'] 
    return answer







































'''os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings()

cerate_db(embeddings)

llm = OpenAI(model_name='gpt-3.5-turbo', temperature=1)


def set_qa_prompt():
    prompt = PromptTemplate(template=qa_template,
                        input_variables=['context', 'question']
                        )
    return prompt


def build_retrieval_qa(llm, prompt, vectordb):
    modeldb = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=vectordb.as_retriever(search_kwargs={'k':2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )
    return modeldb


def setup_dbqa(llm,embeddings):
    vectordb = FAISS.load_local('vectorstore/db_faiss', embeddings)
    qa_prompt = set_qa_prompt()
    model_qa = build_retrieval_qa(llm, qa_prompt, vectordb)

    return model_qa




response = model_qa({'query': 'What are the method use?'})
Answer = response['Answer']
print(Answer)
'''
'''embekddings = OpenAIEmbeddings()
vectordb = FAISS.load_local('vectorstore/db_faiss', embeddings)
qa_prompt = set_qa_prompt()
model = build_retrieval_qa(llm, qa_prompt, vectordb)'''