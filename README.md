# 🛡️ AI Moderation Portal

A FastAPI microservice for **Content Moderation of User‑Generated Content (UGC)** using **Azure AI Content Moderator** and **Text Analytics APIs**.

---

## 🚨 Pain Point

Enterprises face increasing challenges in managing UGC that may contain:

- ❌ Toxic or abusive language  
- 🧃 Spam or promotional content  
- 🔐 Personally Identifiable Information (PII)

---

## ✅ Solution

This microservice provides a scalable and secure way to screen and flag problematic content using:

- **FastAPI** for high-performance RESTful endpoints  
- **Azure AI Content Moderator** for detecting profanity, PII, and unwanted content  
- **Azure Text Analytics** for sentiment analysis and language detection

---

## 📦 Features

- 🔍 Real-time content screening via REST API  
- 🧠 Sentiment and language analysis  
- 🧹 PII detection and redaction  
- 📊 JSON-based moderation reports  
- 🛠️ Easy integration with frontend portals or backend pipelines

---

## 🚀 Quickstart

```bash
# Clone the repo
git clone https://github.com/serverless-yoda/ai-moderation-portal.git
cd ai-moderation-portal

# Install dependencies
pip install -r requirements.txt

# Run the service
uvicorn main:app --reload
