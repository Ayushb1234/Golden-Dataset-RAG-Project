# Golden Dataset Methodology

## 🧠 Objective

The goal of this dataset is to evaluate the retrieval accuracy of a RAG (Retrieval-Augmented Generation) system built on YouTube transcripts related to neural networks and deep learning.

---

## 📌 Selection Criteria

The questions were designed based on the following principles:

- Each question maps to a **specific video segment**
- Questions are **non-trivial** and require understanding
- Each has **only one correct source**
- Questions are **distractor-prone**, meaning similar concepts exist in other videos

---

## ⚙️ Extraction Process

1. Transcripts were collected using:
   - `youtube-transcript-api`
   - `yt-dlp` (fallback)

2. Transcripts were:
   - Cleaned (removed noise, filler words)
   - Converted into structured format with timestamps

3. Content was manually analyzed to:
   - Identify key concepts
   - Map topics to timestamps
   - Select unique concept segments

4. Questions were generated:
   - Using LLM (Grok) for initial drafts
   - Refined manually for clarity and precision

---

## 🎯 What This Dataset Tests

This dataset evaluates:

- ✅ Retrieval Accuracy  
  Whether the system retrieves the correct source chunk

- ✅ Context Grounding  
  Whether answers are based on retrieved content

- ✅ Distractor Resistance  
  Whether the system avoids retrieving similar but incorrect content

---

## ⚠️ Failure Cases

The system is considered incorrect if:

- Retrieves content from the wrong video
- Retrieves partially relevant but incorrect context
- Generates answers not grounded in retrieved chunks

---

## 📊 Evaluation Approach

- Each question is passed through the RAG pipeline
- Top-k retrieved chunks are analyzed
- Correctness is determined based on source matching
- Accuracy is computed as:

Accuracy = Correct Retrievals / Total Questions

---

## 🚀 Summary

This dataset ensures that the RAG system is not only generating answers, but also retrieving the correct context from the correct source, making it robust and reliable.