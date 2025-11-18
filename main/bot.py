import os
import django
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
from main.models import RequiredItem

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

BOT_TOKEN = "8178056523:AAG1roNPcFSacGrNhtpMXpiu90xAQhnXxhs"

def list_books(update: Update, context: CallbackContext):
    items = RequiredItem.objects.select_related('book', 'library').all()
    if not items:
        update.message.reply_text("هیچ کتابی ثبت نشده.")
        return

    message = "📚 لیست کتاب‌ها:\n\n"
    for item in items:
        message += f"{item.book.name} - کتابخانه: {item.library.name} - تعداد مورد نیاز: {item.number_of_required}\n"

    MAX_LENGTH = 4000
    chunks = [message[i:i+MAX_LENGTH] for i in range(0, len(message), MAX_LENGTH)]
    for chunk in chunks:
        update.message.reply_text(chunk)

def start_bot():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("list_books", list_books))
    updater.start_polling()
    updater.idle()