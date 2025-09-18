import requests
from IPython.display import Audio

# Replace with your real ElevenLabs API key
api_key = "xxxxxxcccccccccccccc"

voice_id = "TxGEqnHWrfWFTfGW9XjX"  # Josh - male English voice

text = """
aur bhai kya haal chal  Apna khud ka AI agent banana chahte ho? Bas 3 easy steps mein bana lo!
Step one: Vapi ka use karo taaki real-time voice conversations ho sakein AI ke saath.
Step two: n8n workflow ke through apne tasks automate karo — jaise data handle karna ya emails bhejna.
Step three: Frontend Replit AI se banao aur Vercel pe deploy karo. Bas ho gaya — tumhara AI agent live hai!
Pura code chahiye? Neeche link diya gaya hai — aaj hi shuru karo!
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
with open("hi_output.mp3", "wb") as f:
    f.write(response.content)

Audio("hi_output.mp3")
