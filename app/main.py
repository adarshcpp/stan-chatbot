from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from textblob import TextBlob
import os
from dotenv import load_dotenv
from app.memory import load_memory, save_memory

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="Stan Chatbot")

class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    memory = load_memory()
    user_data = memory.get(req.user_id, {"summary": ""})
    history = user_data["summary"]

    sentiment = TextBlob(req.message).sentiment.polarity
    tone = "comforting" if sentiment < -0.2 else "cheerful" if sentiment > 0.2 else "neutral"

    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
You are a {tone} human-like friend.

Past summary: {history}
User says: {req.message}

Respond in a {tone} tone, 1-2 sentences max, and update memory naturally.
"""
    response = model.generate_content(prompt)
    user_data["summary"] = f"{history}\n{req.message}\n{response.text}"
    memory[req.user_id] = user_data
    save_memory(memory)

    return {"user": req.user_id, "tone": tone, "bot_reply": response.text}
