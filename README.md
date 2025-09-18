# Text-to-speech-for-linkdin-post
---

## 🎤 Voice AI  Text to Speech in 3 Ways

Build your own Voice AI Agent that converts text into speech with multiple options:

✅ Local / Free TTS (No API needed)

🌍 ElevenLabs API – English

🇮🇳 ElevenLabs API – Hindi



---

🚀 Features

Generate voiceover in .mp3 for your scripts

Multiple TTS providers (local or cloud-based)

Easy-to-use Python scripts

Supports male/female voices

Hindi and English speech synthesis



---

📂 Project Structure

voice-ai-agent/
│── README.md
│── requirements.txt
│── scripts/
│   ├── basic.py.py          # Local TTS using pyttsx3 / edge-tts
│   ├── en_to_speech.py    # ElevenLabs English voice
│   ├── hi_to_speech.py    # ElevenLabs Hindi voice
│── output/
│   ├── voice_ai_agent.mp3      # Generated voice files saved here


---

⚙️ Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/voice-ai-agent.git
cd voice-ai-agent
pip install -r requirements.txt

Dependencies

pyttsx3 (offline TTS)

edge-tts (Microsoft neural voices, optional)

requests (for ElevenLabs API)

dotenv (for API keys management)


Install with:

pip install pyttsx3 edge-tts requests python-dotenv


---

🔹 1. Run Without ElevenLabs API (Free & Offline)

You can use pyttsx3 (offline) or edge-tts (Microsoft’s neural voices).

Example: Offline TTS

# scripts/tts_offline.py
import pyttsx3

script_text = "Hello friends! This is your AI agent speaking in offline mode."

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Pick a male/female voice
engine.save_to_file(script_text, "output/voice_ai_agent.mp3")
engine.runAndWait()
print("✅ Offline voiceover saved!")

Run:

python scripts/tts_offline.py


---

🔹 2. With ElevenLabs API (English TTS)

1. Get your API key from ElevenLabs.


2. Create a .env file:



ELEVEN_API_KEY=your_api_key_here

3. Example code:



# scripts/tts_elevenlabs_en.py
import os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVEN_API_KEY")

url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"  # Voice ID (English Male/Female)

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": "Hello friends! Build your AI agent in 3 easy steps with ElevenLabs!",
    "voice_settings": {"stability": 0.6, "similarity_boost": 0.8}
}

response = requests.post(url, headers=headers, json=data)

with open("output/voice_ai_agent_en.mp3", "wb") as f:
    f.write(response.content)

print("✅ English voiceover saved with ElevenLabs!")

Run:

python scripts/tts_elevenlabs_en.py


---

🔹 3. With ElevenLabs API (Hindi TTS)

You can also generate Hindi speech using ElevenLabs multilingual voices.

# scripts/tts_elevenlabs_hi.py
import os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVEN_API_KEY")

url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"  # Multilingual Voice ID

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": "नमस्ते दोस्तों! अब सिर्फ तीन आसान स्टेप्स में अपना एआई एजेंट बनाइए।",
    "voice_settings": {"stability": 0.6, "similarity_boost": 0.8}
}

response = requests.post(url, headers=headers, json=data)

with open("output/voice_ai_agent_hi.mp3", "wb") as f:
    f.write(response.content)

print("✅ Hindi voiceover saved with ElevenLabs!")

Run:

python scripts/tts_elevenlabs_hi.py


---

📌 Notes

Replace EXAVITQu4vr4xnSDxMaL with your chosen ElevenLabs Voice ID.

Hindi voices require a multilingual-enabled voice in ElevenLabs.

Free mode (offline pyttsx3 / edge-tts) works without API keys.



---

🎬 Example Use Case

Create voiceovers for videos

Build AI agents that speak

Automate workflow + speech generation



---

📜 License

MIT License. Free to use and modify.


---

👉 Do you want me to also include a ready-made requirements.txt file for this repo so you can just pip install -r requirements.txt and run?


