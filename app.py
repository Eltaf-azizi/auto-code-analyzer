from langchain.vectorstores import Chroma
from src.helper import dotenv
from dotenv import load_dotenv
import os
from src.helper import repo_ingestion
from flask import Flask, render_template, jsonify, request
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langhcain.chains import ConversationalRetrievalChain



app = Flask(__name__)



load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY



embeddings = load_embedding()
persist_directory = "db"

# Now we can load the persisted from disk, and use it as normal
vectordb = Chroma(persist_directory = persist_directory,
                  embedding_function = embeddings)




llm = ChatOpenAI()
memory = ConversationSummaryMemory(llm=llm, memory_key = "chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=vectordb.as_retriever(search_type="mmr", search_kwargs={"k":8}))




@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')




@app.route('/chatbot', methods=["GET", "POST"])
def gitRepo():


