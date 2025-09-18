import asyncio
import edge_tts

script_text = """
Hello friends! Want to build your own AI agent? Let’s do it in just 3 easy steps!
Step one: Use Vapi to power real-time voice conversations with AI.
Step two: Automate your tasks with an n8n workflow — from data handling to sending emails.
Step three: Deploy your frontend using Vercel or Replit. That’s it — your AI agent is live!
Get the full code and start building today. Link in bio!
"""

async def main():
    voice = "en-US-GuyNeural"  # Male natural voice
    communicate = edge_tts.Communicate(script_text, voice)
    await communicate.save("voice_ai_agent.mp3")
    print("✅ Saved as voice_ai_agent.mp3")

asyncio.run(main())
