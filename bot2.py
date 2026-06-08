from telegram.ext import Application, MessageHandler, filters

TOKEN = "8562820526:AAHyur_T-tfwKImc3MWNAEUR3FYrfhMh3vQ"

async def reply(update, context):
text = update.message.text.lower()
name = update.effective_user.first_name

if "hi alexa" in text:
    await update.message.reply_text(f"Hi {name} 😎")

app = Application.builder().token(TOKEN).build()

app.add_handler(
MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
)

app.run_polling()
