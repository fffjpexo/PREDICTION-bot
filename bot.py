import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN:", TOKEN)  # temporary debug

TOKEN = os.getenv("8575076584:AAHTcIWv-tWLN5HDtWnGaq6rPu1lOirBHPk")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai 🚀")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
