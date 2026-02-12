from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_NAME = "Fiza 💙✨"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi 👋 Main Fiza hoon 💙✨\n\n"
        "Tum mujhe kuch bhi pooch sakte ho.\n"
        "Bas likho: Fiza, mujhe ___ chahiye 😄"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Bot start karo\n"
        "/help - Help dekho\n\n"
        "Example:\nFiza, mujhe motivation chahiye 💙"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "fiza" in text:
        reply = "Haan bolo 😄💙 Main yahin hoon ✨"
    else:
        reply = "Cute message hai 😌💙\nFiza likhkar bolo na ✨"

    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Fiza is running 💙✨")
    app.run_polling()

if __name__ == "__main__":
    main()
