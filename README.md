# 💬 LangChain Chatbot using OpenAI API

This is a Python-based chatbot built using the LangChain framework and OpenAI's language models. It demonstrates how to build a conversational interface that securely handles API keys and can be easily extended for other applications.

---

## 🧠 Features

- AI-powered chatbot using OpenAI GPT
- Modular design with LangChain
- Secure API key management using `.env`
- Easy local setup and usage

---

## 🛠️ Technologies Used

- Python 3.8+
- LangChain
- OpenAI API
- python-dotenv

---


---

## 🔐 Environment Variables

This project uses a `.env` file to store sensitive data like API keys.  
Create a `.env` file in the root directory and add:

OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_key_if_required


> ⚠️ Do not share or commit this file. Ensure `.env` is listed in `.gitignore`.

---

## 🧪 How to Run the Project Locally

Follow these steps to set up and run the chatbot:
1. Clone the Repository

bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv

3. Activate the Virtual Environment
On Windows:
venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

5. Create the .env File
OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langchain_key_if_any

6. Run the Chatbot
python app.py

 Using Ollama Instead of OpenAI (Optional)
You can also run this chatbot using Ollama, an open-source local LLM framework, instead of OpenAI’s API. This allows you to use models like llama2, mistral, or gemma locally without relying on external APIs.

✅ Steps to Use Ollama with LangChain
1)Install Ollama for Windows
Download and install Ollama from the official website:
👉 https://ollama.com/download

2)Run a model locally
After installing Ollama, pull and start a model (e.g., llama2) by running:


3)ollama run llama2
Update requirements.txt
Make sure the following package is added to your requirements.txt file:

langchain-community
You can install it manually if needed:

4)pip install langchain-community
Modify the Code to Use Ollama
In your Python script (e.g., app.py), replace the OpenAI import and usage with:
from langchain_community.llms import Ollama
llm = Ollama(model="llama2")
You can replace "llama2" with other models supported by Ollama like "mistral" or "gemma".

5)No API Key Required
When using Ollama, you don’t need an API key or .env file for authentication — the model runs completely on your local machine.
