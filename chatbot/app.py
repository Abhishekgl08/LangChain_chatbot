from langchain_openai import ChatOpenAI #This imports a class that acts as a wrapper around OpenAI's chat models (like gpt-3.5-turbo or gpt-4).LangChain uses this class to talk to OpenAI's API without writing raw HTTP requests.
from langchain_core.prompts import ChatPromptTemplate #Instead of writing prompts as strings, you write them as templates with dynamic variables like {question}.
from langchain_core.output_parsers import StrOutputParser  #Some chains in LangChain return structured outputs or objects. This parser ensures we get plain readable text.

import streamlit as st #Streamlit is a Python library for building interactive web apps.
import os  #Standard Python library for interacting with the operating system,You use it to fetch environment variables (like your API key).
from dotenv import load_dotenv #It loads environment variables from a file named .env into os.environ.

load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true" #it is used to track its a langchain feature 

print("OPENAI KEY:", os.getenv("OPENAI_API_KEY"))

##Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpfull assistant. Please response to the user queries"), #here we are setting the tone for llm model so that it will reply back {} here this placeholder will be filled with the question that user asks 
        ("user","Question:{question}")
    ]
)

##streamlit framework

st.title('Langchain Demo with OpenAI')
input_text=st.text_input("Search the Topic You want")

#OpenAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser() #it will give response in plain text 
chain=prompt|llm|output_parser # here it is creating a chain Prompt ➜ LLM ➜ Parser

openai_key = os.getenv("OPENAI_API_KEY")
langchain_key = os.getenv("LANGCHAIN_API_KEY")
if openai_key:
    os.environ["OPENAI_API_KEY"] = openai_key
if langchain_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_key

if input_text:
    st.write(chain.invoke({'question':input_text})) #this input text will be filled into the placeholder with name question 
    #here write is used to display the response and chain.invoke is actual calling of llm is done 
