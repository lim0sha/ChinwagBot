import logging
import os

from mistralai import Mistral
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

with open('prompt.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    # print(content)

SYSTEM_PROMPT = content

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = Mistral(api_key=MISTRAL_API_KEY)


def ask_llm(user_message: str) -> str:
    try:
        response = client.chat.complete(
            model="mistral-medium",  # also available: mistral-small, mistral-large
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка: {str(e)}"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Ready to chinwag a little bit!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    bot_username = context.bot.username

    if f"@{bot_username}" in user_message:
        clean_message = user_message.replace(f"@{bot_username}", "").strip()
        answer = ask_llm(clean_message)
        await update.message.reply_text(answer)


def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()


if __name__ == "__main__":
    main()
