import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📺 YouTube", url="https://youtube.com/ТВОЙ_КАНАЛ")],
        [InlineKeyboardButton("🎮 Twitch", url="https://twitch.tv/ТВОЙ_НИК")],
        [InlineKeyboardButton("🎵 TikTok", url="https://tiktok.com/@ТВОЙ_НИК")],
        [InlineKeyboardButton("✈️ ТГК", url="https://t.me/ТВОЙ_КАНАЛ")]
    ]

    await update.message.reply_text(
        "Мои площадки 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
