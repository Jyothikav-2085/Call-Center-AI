import requests
import base64

url = "http://127.0.0.1:5000/api/call-analytics"

# Read audio file
with open("input_audio.mp3", "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode()

headers = {
    "Content-Type": "application/json",
    "x-api-key": "mysecretkey"
}

data = {
    "language": "Tamil",
    "audioFormat": "mp3",
    "audioBase64": audio_base64
}

response = requests.post(url, json=data, headers=headers)

print(response.json())