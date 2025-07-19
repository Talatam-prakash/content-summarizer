## Content Summarizer - YouTube & Web
This is a web application built with Streamlit that generates concise summaries for any public YouTube video or website URL. It leverages the power of LangChain for document processing and the high-speed Groq API for LLM inference to deliver summaries quickly and efficiently.

## Features
- Multi-Source Summarization: Works with both YouTube videos and general website articles.

- Intelligent Transcript Fetching: For YouTube videos, it automatically searches for available transcripts in multiple languages (English and Hindi) to maximize compatibility.

- Handles Long Content: Utilizes a map_reduce chain strategy to effectively summarize long videos or lengthy articles without running into context window limitations.

- High-Speed Inference: Powered by the Groq API and the Gemma2-9b-It model for near-instant summary generation.

- User-Friendly Interface: A clean and simple UI built with Streamlit for ease of use.

- Secure API Key Handling: Uses a password input field to keep your Groq API key secure.

## How It Works
The application follows a simple yet powerful workflow to generate summaries:

**1.URL Input:** The user enters a valid YouTube or website URL.

**2.Content Loading:**

- If a YouTube URL is detected, LangChain's YoutubeLoader is used to fetch the video's transcript. It's configured to look for English, Indonesian, or Hindi transcripts.

- If a Website URL is detected, WebBaseLoader scrapes the main text content from the page.

**3. Text Chunking:** The loaded document (whether from a video transcript or a webpage) is split into smaller, overlapping chunks using RecursiveCharacterTextSplitter. This is crucial for processing long-form content.

**4.Summarization Chain:** A load_summarize_chain with the map_reduce type is initialized. This chain works in two stages:

- Map: It first runs over each text chunk individually and generates a summary for it.

- Reduce: It then takes all the individual summaries and combines them into a single, final summary.

**5.LLM Inference:** The ChatGroq wrapper calls the Groq API, sending the text to the Gemma2-9b-It model to perform the summarization.

**6.Display Results:** The final, coherent summary is displayed in the Streamlit interface.

## Tech Stack
- Backend: Python

- Web Framework: Streamlit

- LLM Orchestration: LangChain

- LLM Provider: Groq API

- Core Libraries:

    - langchain-groq

    - langchain-community

    - youtube-transcript-api

    - validators

    - python-dotenv

## Getting Started
Follow these instructions to get a local copy up and running.

**Prerequisites**
- Python 3.8 or higher

- A Groq API Key. You can get one for free from the Groq Console.

**Installation**

**1.Clone the repository:**
```
git clone https://github.com/YOUR_USERNAME/content-summarizer.git
cd content-summarizer
```

**2. Create and activate a virtual environment (recommended):**

```
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install the required packages:**

Create a requirements.txt file with the following content:
```
streamlit
langchain
langchain-groq
langchain-community
validators
python-dotenv
youtube-transcript-api
beautifulsoup4 # Dependency for WebBaseLoader
```

Then, run the installation command:
```
pip install -r requirements.txt
```
**Configuration**

1. This application uses the script itself to manage the API key, so no .env file is needed. The key is entered directly into the application's UI.

**Running the Application**
1. Launch the Streamlit app:

```
streamlit run app.py
```

**Use the app:**

- Open your web browser and navigate to the local URL provided by Streamlit (usually http://localhost:8501).

- Enter your Groq API Key in the sidebar.

- Paste the YouTube or website URL into the main input box.

- Click the "Generate Summary" button and wait for the result.

