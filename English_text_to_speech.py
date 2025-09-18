import requests
from IPython.display import Audio

# Replace with your real ElevenLabs API key
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"

voice_id = "TxGEqnHWrfWFTfGW9XjX"  # Josh - male English voice

text = """
Hello friends! Want to build your own AI agent? Let’s do it in just 3 easy steps!
Step one: Use Vapi to power real-time voice conversations with AI.
Step two: Automate your tasks with an n8n workflow — from data handling to sending emails.
Step three:Create frontend using Replit Ai and  Deploy your frontend on Vercel. That’s it — your AI agent is live!
Get the full code and start building today. Link below!
"""

# API endpoint
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

# Send request
response = requests.post(
    url,
    headers={
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    },
    json={
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
)

# Save and play audio
with open("en_output.mp3", "wb") as f:
    f.write(response.content)

Audio("en_output.mp3")
