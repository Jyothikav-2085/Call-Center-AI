# from flask import Flask, request, jsonify

# app = Flask(__name__)

# API_KEY = "mysecretkey"

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# API_KEY = "mysecretkey"

# @app.route('/')
# def home():
#     return "API is running"

# # @app.route('/api/call-analytics', methods=['POST'])
# def analyze_call():
    
   
    
#     # 🔐 Check API key
#     key = request.headers.get('x-api-key')

#     if key != API_KEY:
#         return jsonify({"error": "Unauthorized"}), 401

#     # 📦 Get request data
#     data = request.json

#     language = data.get("language")
#     audio_format = data.get("audioFormat")
#     audio_base64 = data.get("audioBase64")

#     return jsonify({
#         "status": "success",
#         "message": "API working",
#         "language": language,
#         "audioFormat": audio_format
#     })

# @app.route('/api/call-analytics', methods=['POST'])
# def analyze_call():
#     import base64

#     # 🔐 Step 1: Check API key FIRST
#     key = request.headers.get('x-api-key')

#     if key != API_KEY:
#         return jsonify({"error": "Unauthorized"}), 401

#     # 📦 Step 2: Get request data
#     data = request.json

#     if not data:
#         return jsonify({"error": "No JSON received"}), 400

#     audio_base64 = data.get("audioBase64")

#     if not audio_base64:
#         return jsonify({"error": "No audio provided"}), 400

#     # 🔄 Step 3: Convert Base64 → audio file
#     try:
#         audio_bytes = base64.b64decode(audio_base64)

#         with open("input_audio.mp3", "wb") as f:
#             f.write(audio_bytes)

#     except Exception as e:
#         return jsonify({"error": "Invalid Base64 data"}), 400

#     # ✅ Step 4: Return success
#     return jsonify({
#         "status": "success",
#         "message": "Audio received and saved"
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# import base64
# import whisper
# import google.generativeai as genai

# # 🔑 SET YOUR GEMINI API KEY HERE
# genai.configure(api_key="AIzaSyBCFkyttgSiOVIuvHzy4U22iOkxDpdulLM")

# # 🤖 Load Gemini model
# model_ai = genai.GenerativeModel("gemini-pro")

# # 🎤 Load Whisper model (loads once)
# model_whisper = whisper.load_model("base")

# app = Flask(__name__)

# API_KEY = "mysecretkey"


# @app.route('/')
# def home():
#     return "API is running 🚀"


# @app.route('/api/call-analytics', methods=['POST'])
# def analyze_call():

#     # 🔐 Step 1: Check API key
#     key = request.headers.get('x-api-key')
#     if key != API_KEY:
#         return jsonify({"error": "Unauthorized"}), 401

#     # 📦 Step 2: Get JSON data
#     data = request.json
#     if not data:
#         return jsonify({"error": "No JSON received"}), 400

#     audio_base64 = data.get("audioBase64")
#     if not audio_base64:
#         return jsonify({"error": "No audio provided"}), 400

#     # 🎧 Step 3: Decode Base64 → audio file
#     try:
#         audio_bytes = base64.b64decode(audio_base64)
#         with open("input_audio.mp3", "wb") as f:
#             f.write(audio_bytes)
#     except:
#         return jsonify({"error": "Invalid Base64 data"}), 400

#     # 🎤 Step 4: Speech → Text (Whisper)
#     try:
#         result = model_whisper.transcribe("input_audio.mp3")
#         transcript = result["text"]
#     except Exception as e:
#         return jsonify({"error": "Transcription failed", "details": str(e)}), 500

#     # 🧠 Step 5: Generate Summary (Gemini)
#     try:
#         response = model_ai.generate_content(
#             f"Summarize this call:\n{transcript}"
#         )
#         summary = response.text
#     except Exception as e:
#         return jsonify({"error": "Gemini failed", "details": str(e)}), 500

#     # 📊 Step 6: Return output
#     return jsonify({
#         "status": "success",
#         "transcript": transcript,
#         "summary": summary
#     })


# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, request, jsonify
# import base64
# import whisper
# import json
# from google import genai

# # 🔑 Put your Gemini API key here
# client = genai.Client(api_key="AIzaSyBCFkyttgSiOVIuvHzy4U22iOkxDpdulLM")

# # Load Whisper model
# model_whisper = whisper.load_model("base")

# app = Flask(__name__)

# API_KEY = "mysecretkey"


# @app.route('/')
# def home():
#     return "Call Center AI API is running 🚀"


# @app.route('/api/call-analytics', methods=['POST'])
# def analyze_call():

#     # 🔐 API key check
#     key = request.headers.get('x-api-key')
#     if key != API_KEY:
#         return jsonify({"error": "Unauthorized"}), 401

#     # 📦 Get data
#     data = request.json
#     if not data:
#         return jsonify({"error": "No JSON received"}), 400

#     audio_base64 = data.get("audioBase64")
#     language = data.get("language")

#     if not audio_base64:
#         return jsonify({"error": "No audio provided"}), 400

#     # 🎧 Decode Base64 → audio file
#     try:
#         audio_bytes = base64.b64decode(audio_base64)
#         with open("input_audio.mp3", "wb") as f:
#             f.write(audio_bytes)
#     except:
#         return jsonify({"error": "Invalid Base64"}), 400

#     # 🎤 Whisper transcription
#     try:
#         result = model_whisper.transcribe("input_audio.mp3")
#         transcript = result["text"]
#     except Exception as e:
#         return jsonify({"error": "Transcription failed", "details": str(e)}), 500

#     # 🧠 Gemini Summary
#     try:
#         response = client.models.generate_content(
#             model="models/gemini-1.5-flash",
#             contents=f"Summarize this call:\n{transcript}"
#         )
#         summary = response.text
#     except Exception as e:
#         return jsonify({"error": "Summary failed", "details": str(e)}), 500

#     # 🧠 Gemini Analysis
#     try:
#         analysis_response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=f"""
# Analyze this call and return STRICT JSON:

# Transcript:
# {transcript}

# Return ONLY this JSON:

# {{
#   "greeting": true,
#   "identification": false,
#   "problemStatement": true,
#   "solutionOffering": true,
#   "closing": true,
#   "paymentPreference": "EMI",
#   "rejectionReason": "NONE",
#   "sentiment": "Neutral"
# }}
# """
#         )

#         analysis_text = analysis_response.text
#         analysis = json.loads(analysis_text)

#     except:
#         analysis = {}

#     # 📊 Compliance score
#     sop_keys = ["greeting", "identification", "problemStatement", "solutionOffering", "closing"]

#     score = 0
#     for key in sop_keys:
#         if analysis.get(key) == True:
#             score += 1

#     compliance_score = score / 5

#     status = "FOLLOWED" if compliance_score == 1 else "NOT_FOLLOWED"

#     # 📊 Final response
#     return jsonify({
#         "status": "success",
#         "language": language,
#         "transcript": transcript,
#         "summary": summary,
#         "sop_validation": {
#             "greeting": analysis.get("greeting", False),
#             "identification": analysis.get("identification", False),
#             "problemStatement": analysis.get("problemStatement", False),
#             "solutionOffering": analysis.get("solutionOffering", False),
#             "closing": analysis.get("closing", False),
#             "complianceScore": compliance_score,
#             "adherenceStatus": status,
#             "explanation": "Auto-generated"
#         },
#         "analytics": {
#             "paymentPreference": analysis.get("paymentPreference", "UNKNOWN"),
#             "rejectionReason": analysis.get("rejectionReason", "NONE"),
#             "sentiment": analysis.get("sentiment", "Neutral")
#         }
#     })


# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import base64
# import whisper
# import json
# from google import genai

# # 🔑 Put your Gemini API key here
# client = genai.Client(api_key="AIzaSyBCFkyttgSiOVIuvHzy4U22iOkxDpdulLM")

# # Load Whisper model
# model_whisper = whisper.load_model("base")

# app = Flask(__name__)

# API_KEY = "mysecretkey"


# @app.route('/')
# def home():
#     return "Call Center AI API is running 🚀"


# @app.route('/api/call-analytics', methods=['POST'])
# def analyze_call():

#     # 🔐 API key check
#     key = request.headers.get('x-api-key')
#     if key != API_KEY:
#         return jsonify({"error": "Unauthorized"}), 401

#     # 📦 Get data
#     data = request.json
#     if not data:
#         return jsonify({"error": "No JSON received"}), 400

#     audio_base64 = data.get("audioBase64")
#     language = data.get("language")

#     if not audio_base64:
#         return jsonify({"error": "No audio provided"}), 400

#     # 🎧 Decode Base64 → audio file
#     try:
#         audio_bytes = base64.b64decode(audio_base64)
#         with open("input_audio.mp3", "wb") as f:
#             f.write(audio_bytes)
#     except:
#         return jsonify({"error": "Invalid Base64"}), 400

#     # 🎤 Whisper transcription
#     try:
#         result = model_whisper.transcribe("input_audio.mp3")
#         transcript = result["text"]
#     except Exception as e:
#         return jsonify({"error": "Transcription failed", "details": str(e)}), 500

#     # 🧠 Gemini Summary
#     try:
#         response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=f"Summarize this call:\n{transcript}"
#         )
#         summary = response.text
#     except Exception as e:
#         return jsonify({"error": "Summary failed", "details": str(e)}), 500

#     # 🧠 Gemini Analysis
#     try:
#         analysis_response = client.models.generate_content(
#             model="models/gemini-1.5-flash",
#             contents=f"""
# Analyze this call and return STRICT JSON:

# Transcript:
# {transcript}

# Return ONLY this JSON:

# {{
#   "greeting": true,
#   "identification": false,
#   "problemStatement": true,
#   "solutionOffering": true,
#   "closing": true,
#   "paymentPreference": "EMI",
#   "rejectionReason": "NONE",
#   "sentiment": "Neutral"
# }}
# """
#         )

#         analysis_text = analysis_response.text

#         # 🔥 CLEAN JSON (important fix)
#         analysis_text = analysis_text.replace("```json", "").replace("```", "").strip()

#         try:
#             analysis = json.loads(analysis_text)
#         except:
#             analysis = {}

#     except:
#         analysis = {}

#     # 📊 Compliance score
#     sop_keys = ["greeting", "identification", "problemStatement", "solutionOffering", "closing"]

#     score = 0
#     for key in sop_keys:
#         if analysis.get(key) == True:
#             score += 1

#     compliance_score = score / 5
#     status = "FOLLOWED" if compliance_score == 1 else "NOT_FOLLOWED"

#     # 📊 Final response
#     return jsonify({
#         "status": "success",
#         "language": language,
#         "transcript": transcript,
#         "summary": summary,
#         "sop_validation": {
#             "greeting": analysis.get("greeting", False),
#             "identification": analysis.get("identification", False),
#             "problemStatement": analysis.get("problemStatement", False),
#             "solutionOffering": analysis.get("solutionOffering", False),
#             "closing": analysis.get("closing", False),
#             "complianceScore": compliance_score,
#             "adherenceStatus": status,
#             "explanation": "Auto-generated"
#         },
#         "analytics": {
#             "paymentPreference": analysis.get("paymentPreference", "UNKNOWN"),
#             "rejectionReason": analysis.get("rejectionReason", "NONE"),
#             "sentiment": analysis.get("sentiment", "Neutral")
#         }
#     })


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
import base64
import whisper

# Load Whisper model
model_whisper = whisper.load_model("base")

app = Flask(__name__)

API_KEY = "mysecretkey"


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
    app.run(debug=True)