# 🤖 STAN Chatbot – Conversational AI Challenge

A human-like chatbot with **context memory** and **emotion-aware tone adaptation**, built using **FastAPI + Gemini 2.5 Flash**.

---

## 🚀 Features
- 💬 Human-like responses  
- 🧠 Per-user long-term memory (`user_memory.json`)  
- 🎭 Tone adaptation (comforting / cheerful / neutral)  
- ⚙️ Lightweight FastAPI backend  
- 🌐 Easily pluggable into any UGC / social platform  

---

## 🧩 Tech Stack
- **Backend:** FastAPI (Python)  
- **LLM:** Gemini 2.5 Flash  
- **Memory Store:** JSON file (extendable to MongoDB / Redis)  
- **Sentiment Analysis:** TextBlob  
- **Environment Manager:** python-dotenv  

---

## ⚙️ Setup & Run
```bash
git clone <your-repo-link>
cd stan-chatbot
python -m venv .venv
.\.venv\Scriptsctivate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

Test chatbot with:
```bash
python test_chat.py
```

Or use the live terminal chat:
```bash
python terminal_chat.py
```

---

## 🧠 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| **GET** | `/health` | Check server status |
| **POST** | `/chat` | Send a message to the chatbot |

### 📨 Request Body
```json
{
  "user_id": "u123",
  "message": "hello"
}
```

### 💬 Example Response
```json
{
  "user": "u123",
  "tone": "cheerful",
  "bot_reply": "Hey there! Great to see you again!"
}
```

---

## 📂 Memory Format

User summaries are stored in `user_memory.json`:
```json
{
  "u123": {
    "summary": "User's name is Adarsh, likes anime, was happy yesterday."
  }
}
```

---

## 🧱 Project Structure
```
stan-chatbot/
│
├── app/
│   ├── main.py          # Main FastAPI app
│   └── memory.py        # Handles user memory
│
├── test_chat.py         # Chatbot test script
├── terminal_chat.py     # Live terminal chat interface
├── requirements.txt     # Dependencies
├── .env                 # Gemini API key
├── user_memory.json     # Stored long-term memory
├── .gitignore           # Excluded files and folders
└── README.md
```

---

## 📊 Evaluation Summary

| Evaluation Criteria | Feature Implemented |
|----------------------|--------------------|
| Long-Term Memory Recall | ✅ Stored in JSON |
| Context-Aware Tone Adaptation | ✅ Sentiment-driven tone |
| Personalization Over Time | ✅ Memory summaries evolve |
| Response Naturalness | ✅ Gemini-generated replies |
| Identity Consistency | ✅ Persona retained |
| Hallucination Resistance | ✅ Controlled prompt |
| Memory Stability | ✅ Reinforced across sessions |

---

## 📜 Author

Developed for the **STAN Internship Challenge (Round 1)**  
by **Adarsh Kumar** — *NIT Jamshedpur*  
You may reuse or extend it with credit.

---

## 🧾 Submission Checklist

- [ ] GitHub Repository Link  
- [ ] Demo Video Link  