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
        # Use Chat Completions API
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a playful, flirty chatbot that responds with humor, emojis, and light teasing."},
                {"role": "user", "content": message.text}
            ],
            max_tokens=150,
            temperature=0.9,
        )

        reply = response["choices"][0]["message"]["content"].strip()
        await message.reply_text(reply)

    except Exception as e:
        await message.reply_text(f"⚠️ Oops! Error: {e}")

app.run()
