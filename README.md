# INDUS AI

## AI for Industrial Knowledge Intelligence

INDUS AI is an AI-powered Industrial Knowledge Intelligence platform developed for ET AI Hackathon 2026 (Problem Statement 8).

The system converts scattered industrial documents into an intelligent knowledge base using Retrieval-Augmented Generation (RAG), OCR, Semantic Search, and Large Language Models.

---

## Problem Statement

Industries generate thousands of manuals, SOPs, inspection reports, maintenance logs, engineering drawings, and compliance documents. Finding accurate information is time-consuming and inefficient.

INDUS AI provides an AI assistant that understands technical documents and answers questions instantly with document citations.

---

## Features

- AI Chat Assistant
- OCR for scanned documents
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Vector Database Search
- Maintenance Recommendations
- Compliance Insights
- Executive Dashboard

---

## Technology Stack

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- FastAPI

### AI

- LangChain
- Gemini / OpenAI
- Sentence Transformers

### Database

- FAISS
- SQLite

### OCR

- Tesseract OCR
- PyMuPDF

---

## System Architecture

User

↓

Web Interface

↓

FastAPI Backend

↓

OCR + PDF Parser

↓

Embedding Model

↓

FAISS Vector Database

↓

RAG Engine

↓

LLM (Gemini/OpenAI)

↓

Response with Citations

---

## Folder Structure

backend/

frontend/

docs/

architecture/

screenshots/

---

## Installation

```bash
git clone https://github.com/yourusername/INDUS-AI.git

cd INDUS-AI

pip install -r requirements.txt

python app.py
```

## Future Enhancements

- ERP Integration
- SAP Integration
- IoT Sensors
- Digital Twin
- Predictive Maintenance
- Voice Assistant
- Multilingual Support

## Team

ET AI Hackathon 2026

Problem Statement 8

AI for Industrial Knowledge Intelligence
