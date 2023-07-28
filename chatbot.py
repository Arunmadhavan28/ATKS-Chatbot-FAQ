!pip install python-docx
pip install python-telegram-bot
import logging
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

from docx import Document

# Path to the Word file containing responses
word_file_path = '/Users/arunmadhavanevr/Downloads/chatbot/chatbot FAQ.docx'

# Read the Word file
doc = Document(word_file_path)

# Initialize a list to store the FAQs and responses
faqs = []

# Read the content of the Word file and store FAQs and responses in the list
for paragraph in doc.paragraphs:
    if ':' in paragraph.text:
        faq, answer = paragraph.text.split(':', 1)
        faqs.append((faq.strip(), answer.strip()))


def handle_message(update, context):
    user_message = update.message.text
    response = find_response(user_message)
    if response:
        update.message.reply_text(response)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def main():
    # Your Telegram Bot API Token
    telegram_token = 'TELEGRAM API ID'

    # Create an Updater object and pass your Telegram Bot API token
    updater = Updater(token=telegram_token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Handle user messages with the handle_message function
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
    dispatcher.add_handler(message_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you stop it manually with Ctrl+C
    updater.idle()

if __name__ == "__main__":
    main()
