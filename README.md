# 🧮 Personalized Math Tutor Agent

A personalized AI-powered math tutor built using **Streamlit** and **Groq LLM**, designed to adapt to individual learners by remembering their name and weak topics. The system provides step-by-step explanations and personalized guidance while remaining efficient under free-tier API limits.

---

## 🚀 Features

- 🧠 **Personalized Learning**  
  Remembers user name and weak topics (e.g., multiplication).

- ✏️ **Step-by-Step Explanations**  
  Explains math problems in a simple, tutor-friendly manner.

- 💾 **Bounded External Memory**  
  Uses lightweight session-based memory instead of long chat history to avoid token overflow.

- 🌐 **Interactive Web Interface**  
  Built with Streamlit for an easy-to-use chat interface.

- 🆓 **Free-Tier Friendly**  
  Optimized to work with Groq’s free API limits.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq LLM (`llama-3.1-8b-instant`)**
- **Regex-based NLP for memory extraction**

---

## 📂 Project Structure

