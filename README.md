
<h1 align="center"> 🔍 Auto Code Analyzer</h1>

Analyze source code from any GitHub repository using the power of AI.

This project demonstrates how to build an AI-powered code analyzer that can read and understand source code from GitHub repositories. By combining Python, OpenAI, LangChain, and vector databases like ChromaDB, the system creates a smart knowledge base of code that can be queried conversationally.



## 🚀 Features

- 🔗 **GitHub Integration** – Fetch and analyze any public repository.
- 🧠 **AI-Powered Code Understanding** – Use OpenAI's models to generate insights and explanations.
- 📚 **Knowledge Base Creation** – Store code context using vector embeddings.
- 💬 **Conversational Interface** – Interact with your code via natural language.
- ☁️ **Cloud Deployment** – Easily deploy your solution to the cloud.



## 🛠️ Tech Stack

| Tool        | Description                                   |
|-------------|-----------------------------------------------|
| Python      | Core programming language                     |
| Flask       | Backend framework for serving the API         |
| OpenAI      | GPT models for code analysis and Q&A          |
| LangChain   | Language model orchestration and chaining     |
| ChromaDB    | Vector database for semantic search           |



## 📂 Project Structure
```
auto-code-analyzer/
├── app/ # Flask backend
│ ├── routes.py
│ ├── analyzer.py
│ └── utils/
├── langchain/ # LangChain workflows
├── chromadb/ # Vector store setup
├── scripts/ # GitHub fetchers and parsers
├── requirements.txt
├── README.md
└── run.py
```

## 📌 How It Works

1. **Clone a GitHub Repository** – User provides a repository URL.
2. **Parse & Extract Code** – Files are scanned, parsed, and preprocessed.
3. **Embed the Code** – Code snippets are converted into embeddings using OpenAI.
4. **Store in Vector DB** – Embeddings are saved in ChromaDB for quick retrieval.
5. **Ask Questions** – Users ask questions, and the system uses semantic search + GPT to respond intelligently.


## 🧪 Example Use Cases

- "What does the `main.py` file do?"
- "Where is the database configured?"
- "Show all functions using recursion."
- "Explain the structure of this Django project."


## 🖥️ Installation

```bash
git clone https://github.com/yourusername/auto-code-analyzer.git
cd auto-code-analyzer
pip install -r requirements.txt
```
Set your OpenAI API key:

```bash
Copy
Edit
export OPENAI_API_KEY=your_key_here
```

▶️ Run the App
```bash
Copy
Edit
python run.py
```
Then open your browser at http://localhost:5000.


## ☁️ Deployment
Deploy to any cloud provider (AWS EC2, Render, Heroku). Ensure environment variables like OPENAI_API_KEY are securely set.


## 📖 Learning Goals
 - Build practical AI tools with real-world utility

 - Learn backend development with Flask

 - Gain experience in LangChain and vector search (ChromaDB)

 - Master the integration of OpenAI APIs in production-level apps

## 🤝 Contributing
Contributions are welcome! If you'd like to enhance the system with features like:

 - GUI (JavaFX or Swing)

 - Persistent storage (File I/O or JDBC)

 - Enhanced validation and exception handling

 - Feel free to fork the repo and submit a pull request.

<h3 align="center">Happy Coding!</h3>

