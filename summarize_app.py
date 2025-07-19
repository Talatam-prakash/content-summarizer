import validators, streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os   
# Load environment variables from .env file
load_dotenv()

#set streamlit page config
st.set_page_config(page_title="Summarize YouTube and Website URL") 
st.title("Summarize YouTube and Website URL")
st.subheader("Summarize YouTube and Website URL using Groq LLM")

with st.sidebar:
    groq_api_key = st.text_input("Enter your Groq API Key:", type="password")

llm = None
if groq_api_key:
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

generic_url = st.text_input("Enter a YouTube or Website URL",label_visibility="collapsed")
prompt = """You are a helpful assistant that summarizes content from YouTube videos and websites.
Summarize the content in a concise and informative manner, highlighting the main points and key information.

{text}"""
prompt_template = PromptTemplate(template=prompt, input_variables=["text"])

if st.button("Summarize"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please enter both Groq API Key and URL.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Loading data..."):
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(  generic_url,
                        add_video_info=False, # Set to False to avoid metadata errors
                         language=["en", "id", "hi"] # Look for English or Indonesian transcripts
                        # Translate to English if necessary
                    )
                else:
                    loader = WebBaseLoader(web_paths=[generic_url])
                
                documents = loader.load()
                if not documents:
                    st.error("No content found at the provided URL.")
                    st.stop()
                chain= load_summarize_chain(
                    llm=llm,
                    chain_type="stuff",
                    prompt=prompt_template,
                    verbose=True
                )
                output = chain.run(documents)
                st.success("Summary generated successfully!")
                st.write(output)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.stop()   

            