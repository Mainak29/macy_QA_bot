# Macy_QA_bot
Macy is an Artificial Intelligence ChatBot based on LLM models. 

# Macy 🤖 QA Bot Web App

This project is a simple Question Answering (QA) chatbot built with Python. It uses a language model API (e.g., Together.ai or OpenAI) and serves responses through a clean and responsive web interface using Flask.

----
## 🚀 Features

- Ask natural language questions via a web form
- Get answers powered by large language models
- Simple, clean, responsive HTML interface
- Easily customizable backend

---
## ⚙️ Requirements

You can install all dependencies using:

```bash
pip install -r requirements.txt

or can manually do
pip install flask
pip install python-dotenv
pip install requests

---

Create a .env file in the root directory and add the below details
TOGETHER_API_KEY=your_together_ai_api_key_here

----
Run the App by using the below command in your localhost

python app.py

----
Project Structure

macy_QA_bot/
├── app.py # Flask server
├── qa_bot.py # Your question-answering logic (uses Together.ai/OpenAI)
├── config.py # Environment variable loader
├── templates/
│ └── index.html # Frontend HTML UI
├── .env # Stores your API key securely
├── requirements.txt # All required Python packages
└── README.md # You're reading it!


Thank you.
