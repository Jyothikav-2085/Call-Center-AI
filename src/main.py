from flask import Flask, request, jsonify
import base64
import whisper
import os

# Load Whisper model
model_whisper = whisper.load_model("base")

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


@app.route('/')
def home():
    return "Call Center AI API is running 🚀"


@app.route('/api/call-analytics', methods=['POST'])
def analyze_call():

    # 🔐 API key check
    key = request.headers.get('x-api-key')
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    # 📦 Get data
    data = request.json
    if not data:
        return jsonify({"error": "No JSON received"}), 400

    audio_base64 = data.get("audioBase64")
    language = data.get("language")

    if not audio_base64:
        return jsonify({"error": "No audio provided"}), 400

    # 🎧 Decode Base64 → audio file
    try:
        audio_bytes = base64.b64decode(audio_base64)
        with open("input_audio.mp3", "wb") as f:
            f.write(audio_bytes)
    except:
        return jsonify({"error": "Invalid Base64"}), 400

    # 🎤 Whisper transcription
    try:
        result = model_whisper.transcribe("input_audio.mp3")
        transcript = result["text"].lower()
    except Exception as e:
        return jsonify({"error": "Transcription failed", "details": str(e)}), 500

    # 🧠 SIMPLE SUMMARY (local logic)
    summary = transcript[:150] + "..."

    # 🧠 SOP DETECTION (keyword-based)
    greeting = any(word in transcript for word in ["hello", "hi", "vanakkam"])
    identification = any(word in transcript for word in ["my name", "i am calling"])
    problem = any(word in transcript for word in ["problem", "issue", "payment"])
    solution = any(word in transcript for word in ["you can", "please pay", "solution"])
    closing = any(word in transcript for word in ["thank you", "bye"])

    # 📊 Compliance score
    sop_list = [greeting, identification, problem, solution, closing]
    score = sum(sop_list)
    compliance_score = score / 5

    status = "FOLLOWED" if compliance_score == 1 else "NOT_FOLLOWED"

    # 💳 Payment detection
    if "emi" in transcript:
        payment = "EMI"
    elif "full payment" in transcript:
        payment = "FULL_PAYMENT"
    elif "partial" in transcript:
        payment = "PARTIAL_PAYMENT"
    else:
        payment = "UNKNOWN"

    # 😐 Sentiment detection
    if any(word in transcript for word in ["good", "happy", "yes"]):
        sentiment = "Positive"
    elif any(word in transcript for word in ["no", "not interested", "later"]):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # 📊 Final response
    return jsonify({
        "status": "success",
        "language": language,
        "transcript": transcript,
        "summary": summary,
        "sop_validation": {
            "greeting": greeting,
            "identification": identification,
            "problemStatement": problem,
            "solutionOffering": solution,
            "closing": closing,
            "complianceScore": compliance_score,
            "adherenceStatus": status,
            "explanation": "Keyword-based analysis"
        },
        "analytics": {
            "paymentPreference": payment,
            "rejectionReason": "NONE",
            "sentiment": sentiment
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
