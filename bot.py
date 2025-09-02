from pyrogram import Client, filters
import openai
import os

API_ID = 23212132      # from https://my.telegram.org
API_HASH = "1c17efa86bdef8f806ed70e81b473c20"
BOT_TOKEN = "8125914573:AAG3zY96757uoIGVKSDC0y_KbifIX_uL4So"
OPENAI_KEY = "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"

# Configure OpenAI
openai.api_key = OPENAI_KEY

app = Client("flirty_ai_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Handle messages
@app.on_message(filters.private & filters.text)
async def chat_ai(client, message):
    try:
        # Send user message to AI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You are a playful, flirty chatbot. Respond to: {message.text}",
            max_tokens=150,
            temperature=0.9,
            top_p=0.95,
        )

        reply = response.choices[0].text.strip()
        await message.reply_text(reply)

    except Exception as e:
        await message.reply_text("⚠️ Oops! Something went wrong.")

app.run()
