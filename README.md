# 🎥 YouTube RAG System with Golden Dataset

## 🚀 Overview
This project builds a **Retrieval-Augmented Generation (RAG)** system on top of YouTube videos related to Neural Networks and Deep Learning.

It extracts transcripts, processes them, and enables intelligent question answering using semantic search and Grok (LLM).

---

## 🧠 Features

- 📥 YouTube transcript ingestion (API + yt-dlp fallback)
- 🧹 Transcript cleaning & normalization
- ✂️ Smart chunking with timestamps
- 🔍 Semantic search using embeddings
- 🗂️ Vector database using FAISS
- 🤖 Answer generation using Grok API
- 📊 Evaluation using Golden Dataset

---

## 🏗️ Project Structure

Golden-Dataset-RAG-Project/
│
├── data/
│ ├── raw/ # Raw transcripts (.json / .vtt)
│ ├── processed/ # Cleaned transcripts
│
├── src/
│ ├── ingestion/ # Transcript fetching + parsing
│ ├── retrieval/ # Chunking, embeddings, vector DB
│ ├── qa/ # RAG pipeline, QA generation, evaluation
│
├── golden_dataset/
│ ├── qa_pairs.json # Golden dataset (evaluation)
│ ├── methodology.md # Dataset design explanation
│
├── main.py # Entry point
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ayushb1234/Golden-Dataset-RAG-Project.git
cd Golden-Dataset-RAG-Project
```

### 2. Create virtual environment
```
python -m venv venv
source venv/Scripts/activate   # Git Bash (Windows)
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 🔑 Environment Setup

Create a .env file in the root directory:

GROK_API_KEY=your_api_key_here

### ▶️ How to Run

python main.py

### 🔍 Example Query

How does backpropagation work in neural networks?

### 🧠 System Architecture

YouTube Videos
      ↓
Transcript Extraction
      ↓
Cleaning & Processing
      ↓
Chunking (with timestamps)
      ↓
Embeddings (HuggingFace)
      ↓
FAISS Vector Database
      ↓
User Query
      ↓
Top-k Retrieval
      ↓
Grok (LLM)
      ↓
Final Answer + Source


### 📊 Golden Dataset

The project includes a curated dataset for evaluation:

✔️ 5 high-quality QA pairs
✔️ Each linked to a specific video + timestamp
✔️ Designed with distractors to test retrieval

### 📌 Methodology

Questions are mapped to specific video segments
Each query has only one correct source
Designed to test:
Retrieval accuracy
Context grounding
Distractor resistance

### 📈 Evaluation

The system evaluates:

✅ Correct retrieval (source matching)
❌ Wrong retrieval (incorrect video/segment)

###  Metric:

Accuracy = Correct Retrievals / Total Questions

### ⚠️ Challenges Faced
----------------------------

YouTube transcript API failures
Rate limiting (HTTP 429)
Handling multiple formats (.json, .vtt)
LLM response parsing
Dependency deprecations (LangChain updates)