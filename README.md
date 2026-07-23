<div align="center">

# 🚀 LangChain Mastery

### Build Modern AI Applications with LangChain, RAG, AI Agents, LangGraph, CrewAI & More

A comprehensive hands-on repository containing practical examples, mini-projects, and production-ready concepts for learning modern AI application development using LangChain and the latest Generative AI technologies.

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Latest-00C853?style=for-the-badge)
![Generative AI](https://img.shields.io/badge/Generative-AI-blueviolet?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Applications-orange?style=for-the-badge)
![AI Agents](https://img.shields.io/badge/AI-Agents-red?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

---

### ⭐ Learn by Building • Practice by Coding • Master by Creating

</div>

---

# 👨‍💻 Author

## Sujit Sadalage

AI Engineer • Python Developer • Generative AI Enthusiast

Welcome to **LangChain Mastery**, a complete practical learning repository designed for developers who want to master modern AI application development.

Unlike repositories that only explain concepts, this project focuses on **building real examples**. Every directory introduces a new concept with executable Python code so you understand not only *what* LangChain does, but *why* it works and *how* to use it in real-world applications.

Whether you're a beginner exploring Large Language Models for the first time or an experienced developer looking to build production-ready AI systems, this repository provides a structured path from basic chat models to advanced AI agents.

---

# 📖 About This Repository

Large Language Models have changed software development forever.

Today, developers are expected to know much more than simply calling an API.

Modern AI applications require knowledge of:

- Prompt Engineering
- Context Management
- Embeddings
- Retrieval-Augmented Generation
- Vector Databases
- AI Agents
- Tool Calling
- Workflow Automation
- Memory
- Multi-Agent Systems

Learning all these concepts individually can be overwhelming.

This repository solves that problem by organizing everything into small, focused examples that gradually build your understanding.

Instead of reading hundreds of pages of documentation, you'll learn by running code, modifying examples, and experimenting yourself.

---

# 🎯 Learning Objectives

After completing this repository, you'll be able to:

- Connect to multiple Large Language Models
- Write reusable prompt templates
- Build LangChain pipelines
- Understand LCEL (LangChain Expression Language)
- Create Sequential and Parallel Chains
- Work with documents
- Generate embeddings
- Store vectors inside vector databases
- Perform semantic search
- Build Retrieval-Augmented Generation (RAG)
- Develop conversational AI applications
- Build autonomous AI Agents
- Create custom LangChain Tools
- Understand LangGraph workflows
- Build multi-agent systems
- Integrate Groq and Hugging Face models
- Connect AI applications with Supabase
- Design scalable AI architectures

---

# 🌟 Repository Highlights

✔ 50+ Practical Examples

✔ Beginner Friendly

✔ Step-by-Step Learning

✔ Well Commented Code

✔ Production Concepts

✔ Modern LangChain APIs

✔ RAG Deep Dive

✔ AI Agent Examples

✔ LangGraph Examples

✔ CrewAI Examples

✔ Groq Integration

✔ Hugging Face Integration

✔ Supabase Integration

✔ Real Mini Projects

✔ Easy to Extend

---

# 👥 Who Should Use This Repository?

This repository is ideal for:

- Python Developers
- AI Engineers
- Software Engineers
- Machine Learning Engineers
- Data Scientists
- College Students
- Working Professionals
- Backend Developers
- Generative AI Enthusiasts
- Anyone interested in building AI applications

No previous LangChain experience is required.

Basic Python knowledge is enough to get started.

---

# 🧠 Technologies Covered

This repository includes practical examples using modern AI technologies.

## Programming

- Python

---

## AI Frameworks

- LangChain
- LangGraph
- CrewAI
- PydanticAI

---

## LLM Providers

- OpenAI
- Google Gemini
- Groq
- Hugging Face
- Anthropic (where applicable)

---

## Vector Databases

- ChromaDB

---

## Backend

- Supabase
- Firebase
- FastAPI (Projects)

---

## AI Concepts

- Prompt Engineering
- Chat Models
- Chains
- LCEL
- Embeddings
- Vector Search
- Semantic Search
- Retrieval
- Metadata Filtering
- RAG
- Conversational RAG
- Tool Calling
- AI Agents
- Multi-Agent Systems

---

# 📚 Learning Roadmap

The repository follows a structured roadmap.

```
Python Basics
      │
      ▼
Environment Setup
      │
      ▼
Chat Models
      │
      ▼
Prompt Templates
      │
      ▼
Chains
      │
      ▼
Documents
      │
      ▼
Text Splitting
      │
      ▼
Embeddings
      │
      ▼
Vector Databases
      │
      ▼
Retrievers
      │
      ▼
RAG
      │
      ▼
Conversational RAG
      │
      ▼
AI Agents
      │
      ▼
Custom Tools
      │
      ▼
LangGraph
      │
      ▼
CrewAI
      │
      ▼
Production AI Applications
```

---

# 📦 Repository Structure

```
langchain_project
│
├── 1_chat_models
├── 2_prompt_templates
├── 3_chains
├── 4_rag
├── 5_agents_and_tools
├── crewai
├── groq
├── HF
├── HybridAgent
├── langGraph
├── pydanticAi
├── rag
├── supabase_auth
├── supbase
│
├── README.md
├── main.py
└── requirements.txt
```

Every folder focuses on a specific topic so you can learn one concept at a time.

---

# ⚙️ Prerequisites

Before running the examples, ensure you have the following installed:

- Python 3.10 or above
- Git
- pip
- Virtual Environment (recommended)
- VS Code or PyCharm

Depending on the example, you'll also need one or more API keys such as:

- OpenAI
- Google Gemini
- Groq
- Hugging Face
- Firebase
- Supabase

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/langchain-mastery.git
```

---

## Navigate into the Project

```bash
cd langchain-mastery
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Linux / macOS

```bash
python3 -m venv .venv
```

---

## Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
poetry install --no-root
```

---

## Configure Environment Variables

Create a `.env` file in the required project folders.

Example:

```env
OPENAI_API_KEY=

GOOGLE_API_KEY=

GROQ_API_KEY=

HUGGINGFACE_API_KEY=

SUPABASE_URL=

SUPABASE_KEY=

FIREBASE_API_KEY=
```

---

## Run an Example

```bash
python 1_chat_models/1_chat_model_basic.py
```

or

```bash
python 4_rag/7_rag_conversational.py
```

---

# 📂 Project Walkthrough

---

# 1️⃣ Chat Models

Folder:

```
1_chat_models/
```

This section introduces the foundation of LangChain.

You'll learn how to communicate with modern Large Language Models using a clean and structured interface.

Examples included:

- Basic Chat Model
- Multi-turn Conversations
- Alternative Model Providers
- Interactive Chat
- Saving Chat History

Topics covered:

- HumanMessage
- AIMessage
- SystemMessage
- Chat History
- Model Parameters
- Temperature
- Max Tokens
- Streaming
- Session Memory

By the end of this section you'll understand how LangChain standardizes communication with different LLM providers.

---

# 2️⃣ Prompt Templates

Folder:

```
2_prompt_templates/
```

Prompt engineering is one of the most important skills when building AI applications.

Instead of writing prompts as plain strings, LangChain provides reusable prompt templates.

Examples include:

- PromptTemplate
- ChatPromptTemplate
- Dynamic Variables
- Prompt Composition
- Structured Prompt Design

You'll learn how to create prompts that are:

- Reusable
- Maintainable
- Easy to scale
- Easy to debug

---

# 3️⃣ Chains

Folder:

```
3_chains/
```

Chains connect multiple LangChain components together.

Instead of manually calling prompts and models one by one, chains automate the entire workflow.

Examples include:

- Basic Chains
- LCEL Examples
- Sequential Chains
- Parallel Chains
- Branching Chains
- Runnable Pipelines

Topics covered:

- RunnableLambda
- RunnableSequence
- RunnableParallel
- RunnableBranch
- Output Parsing
- Pipeline Composition

Chains are one of the core building blocks of modern LangChain applications.

---

# 4️⃣ Retrieval-Augmented Generation (RAG)

Folder:

```
4_rag/
```

This section explores one of the most important techniques in modern AI.

Rather than relying only on an LLM's training data, Retrieval-Augmented Generation allows models to retrieve relevant information from external documents before generating responses.

The RAG examples are divided into progressive stages so you can understand each component individually before combining them into a complete system.

**➡️ Continue with Part 2**, where the README covers every RAG example in detail, AI Agents, LangGraph, CrewAI, Groq, Hugging Face, Supabase, your HybridAgent project, FAQs, contributing, license, and the remaining sections.

## 📄 RAG Examples Included

The `4_rag` folder contains a complete progression from beginner to advanced Retrieval-Augmented Generation concepts.

### 1a. Basic RAG

Learn the basic RAG workflow:

- Load documents
- Split documents
- Generate embeddings
- Store vectors
- Ask questions

---

### 1b. Improved RAG

Extends the basic implementation with cleaner architecture and better retrieval.

Topics covered:

- Better prompts
- Better retrieval
- Response generation
- Context handling

---

### 2a. Metadata Filtering

Documents often contain useful metadata.

Example metadata:

- Author
- Source
- Date
- Category
- Tags

Instead of searching every document, metadata allows searching only relevant documents.

---

### 2b. Advanced Metadata Search

Build more intelligent retrieval systems using metadata filters.

You'll learn:

- Filtering
- Search optimization
- Structured retrieval

---

### 3. Text Splitting Deep Dive

One of the most important topics in RAG.

Topics covered:

- Chunk Size
- Chunk Overlap
- Recursive Character Splitter
- Why chunking matters
- Performance comparison

You'll understand why poor chunking often leads to poor AI responses.

---

### 4. Embedding Deep Dive

Learn how text becomes vectors.

Topics include:

- Embedding Models
- Dense Vectors
- Vector Dimensions
- Cosine Similarity
- Semantic Meaning
- Similarity Search

You'll understand how AI "understands" relationships between pieces of text.

---

### 5. Retriever Deep Dive

Retrievers decide which documents are sent to the LLM.

Topics include:

- Top-K Search
- Similarity Search
- Retriever Configuration
- Ranking
- Search Accuracy

---

### 6. One-Off Question Answering

Build a simple RAG pipeline capable of answering questions from external documents.

Workflow:

```
Documents
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database
      ↓
Retriever
      ↓
LLM
      ↓
Final Answer
```

---

### 7. Conversational RAG

Move beyond one-time questions.

Learn how to build chatbots capable of remembering previous conversations while retrieving external knowledge.

Topics covered:

- Chat History
- Memory
- Context Management
- Follow-up Questions
- Conversation State

---

### 8. Web Scraping RAG

Instead of querying local files, build a RAG system using website content.

Examples include:

- Basic Web Scraping
- Firecrawl Integration
- Website Knowledge Bases

---

### Included Dataset

The repository contains multiple books and documents for experimentation.

Examples include:

- Sherlock Holmes
- Moby Dick
- Pride and Prejudice
- Frankenstein
- Romeo and Juliet
- War and Peace
- The Odyssey
- The Iliad
- Declaration of Independence
- Bill of Rights
- And more...

---

# 🤖 AI Agents & Tools

Folder:

```
5_agents_and_tools/
```

Traditional chatbots only generate text.

AI Agents can:

- Think
- Reason
- Decide
- Use tools
- Observe results
- Continue reasoning
- Produce final answers

This section introduces autonomous AI systems using LangChain Agents.

---

## Agent Basics

Learn:

- What is an AI Agent?
- Agent Executor
- Tool Calling
- Multi-step Reasoning
- Decision Making

---

## ReAct Agent

The ReAct framework combines reasoning and acting.

Typical workflow:

```
Question
     ↓
Reason
     ↓
Select Tool
     ↓
Execute Tool
     ↓
Observe Result
     ↓
Reason Again
     ↓
Final Answer
```

---

## DocStore Agent

Learn how agents interact with document stores to retrieve knowledge before answering questions.

---

## Tool Development

The repository demonstrates multiple ways to create custom tools.

Examples include:

### Tool Constructor

Create tools manually.

### Tool Decorator

Use decorators for cleaner implementations.

### BaseTool

Build production-ready custom tools with validation and structured inputs.

Topics include:

- Tool Schema
- Validation
- Metadata
- Input Parsing
- Output Handling

---

# 🌐 LangGraph

Folder:

```
langGraph/
```

LangGraph is designed for building stateful AI workflows.

Examples included:

- Simple Chatbot
- Conditional Graphs

You'll learn:

- Nodes
- Edges
- State
- Conditional Routing
- Workflow Execution
- Graph-Based AI Systems

---

# 👥 CrewAI

Folder:

```
crewai/
```

CrewAI enables collaboration between multiple AI agents.

Examples demonstrate:

- Agent Creation
- Role Assignment
- Task Delegation
- Collaboration
- Multi-Agent Workflows

---

# 🤗 Hugging Face

Folder:

```
HF/
```

Examples show how to integrate Hugging Face models into LangChain workflows.

Topics include:

- Model Loading
- Local Inference
- Open Models
- Embeddings
- Pipelines

---

# ⚡ Groq

Folder:

```
groq/
```

Groq provides ultra-fast inference for modern LLMs.

Examples demonstrate:

- Chat Completion
- API Integration
- High-Speed Inference
- LangChain Integration

---

# 🧩 PydanticAI

Folder:

```
pydanticAi/
```

Learn how structured outputs improve AI applications.

Topics include:

- Data Validation
- Structured Responses
- Type Safety
- Response Parsing

---

# 📚 Local RAG Example

Folder:

```
rag/
```

A complete local Retrieval-Augmented Generation implementation.

Features:

- ChromaDB
- Local Vector Store
- Indexing
- Retrieval
- Persistent Storage

---

# 🔐 Supabase Authentication

Folder:

```
supabase_auth/
```

Learn how to integrate authentication into AI applications.

Topics:

- User Login
- Authentication
- Secure Access
- API Protection

---

# ☁️ Supabase Chatbot

Folder:

```
supbase/
```

Demonstrates integrating LangChain with Supabase.

Features:

- Chatbot
- Database Storage
- Cloud Backend
- Authentication

---

# 🚀 HybridAgent Project

Folder:

```
HybridAgent/
```

One of the largest projects in this repository.

This project combines multiple AI capabilities into a single intelligent assistant.

Features include:

- Intelligent Query Processing
- Tool Registry
- File Management
- GitHub Integration
- Coding Assistant
- Shell Commands
- Memory Management
- Logging
- Modular Architecture

Included tools:

- File Tools
- GitHub Tools
- General Utility Tools
- Coding Tools
- System Tools

The project demonstrates how multiple AI components can work together to build a production-style AI assistant.

---

# 🏗 Repository Architecture

```
                User
                  │
                  ▼
           Prompt Template
                  │
                  ▼
            Chat Model
                  │
                  ▼
            LangChain
                  │
      ┌───────────┼───────────┐
      │           │           │
      ▼           ▼           ▼
    Chains      Agents      Tools
      │           │           │
      └───────────┼───────────┘
                  │
                  ▼
               Retrieval
                  │
                  ▼
             Vector Store
                  │
                  ▼
               Documents
                  │
                  ▼
             Final Response
```

---

# 🎯 Skills You'll Gain

After completing this repository you'll understand:

- LangChain Fundamentals
- Prompt Engineering
- Chat Models
- LCEL
- Chains
- Runnables
- Embeddings
- ChromaDB
- Vector Search
- Semantic Search
- Metadata Filtering
- Retrieval
- RAG
- Conversational RAG
- AI Agents
- Tool Calling
- LangGraph
- CrewAI
- Groq
- Hugging Face
- Supabase Integration
- Production AI Design

---

# 💡 Best Practices

- Keep API keys inside `.env`
- Use virtual environments
- Read comments before modifying code
- Run examples sequentially
- Experiment with different models
- Compare embedding providers
- Try different chunk sizes
- Build your own AI projects after completing each section

---

# 🤝 Contributing

Contributions are welcome.

You can contribute by:

- Adding new examples
- Improving documentation
- Fixing bugs
- Optimizing code
- Updating dependencies
- Adding new AI providers

If you have a useful idea or find an issue, feel free to open a Pull Request or submit an Issue.

---

# 📌 Future Improvements

Planned additions include:

- Model Context Protocol (MCP)
- Memory Systems
- Multi-Agent Collaboration
- OpenAI Responses API
- LangSmith Examples
- LlamaIndex Integration
- Qdrant
- Pinecone
- FAISS
- PostgreSQL + pgvector
- FastAPI AI Backend
- Streamlit AI Applications
- Advanced LangGraph Workflows

---

# 📖 Frequently Asked Questions

### Is this repository beginner friendly?

Yes. Every topic starts with the fundamentals before moving toward advanced concepts.

---

### Which Python version should I use?

Python **3.10+** is recommended.

---

### Do I need paid APIs?

No. Many examples can be adapted to free providers or local models, though some examples may require API keys from supported services.

---

### Can I use this repository for learning AI?

Absolutely. It is specifically designed as a practical learning resource.

---

### Can I contribute?

Yes! Contributions, suggestions, and improvements are always welcome.

---

# ⭐ Support

If this repository helped you learn LangChain or build your own AI applications:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠 Build something awesome
- 📢 Share it with others

Your support helps improve future content and encourages continued development.

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute the code in accordance with the license.

---

<div align="center">

# ❤️ Built with Passion by Sujit Sadalage

### AI Engineer • Python Developer • Generative AI Enthusiast

*"The best way to learn AI is to build AI."*

---

### Happy Coding...! 🚀

</div>
