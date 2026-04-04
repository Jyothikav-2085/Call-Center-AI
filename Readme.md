# 📞 Call Center AI

An AI-powered call analytics system that processes customer service calls and provides insights such as transcription, summary, sentiment analysis, and SOP compliance.

---

## 🚀 Features

- 🎤 Speech-to-text transcription (Whisper)
- 🧠 AI-based call summarization
- 📊 SOP compliance detection
- 😊 Sentiment analysis
- 📈 Call analytics extraction

---

## 🛠 Tech Stack

- Python (Flask)
- OpenAI Whisper (Speech Recognition)
- Gunicorn (Production Server)
- Railway (Deployment)

---

## 🌐 Live URL

call-center-ai-production.up.railway.app

---

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/Call-Center-AI.git
cd Call-Center-AI

## Install Dependencies
pip install -r requirements.txt

## Environment Variables
Create .env file
API_KEY=your_api_key_here

##AI Tools Used
ChatGpt or Debugging and Development Guidance
OpenAI Whisper for Speech to Text Conversion

##Limitations
Whisper is CPU Based -> Slower porcoessing
No Frontend (API Only System)
Requires audio in supported format only

##Author
Jyothika V

## Run Locally
python src/main.py


