from telegram import Update
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext

import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom!")

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
# print(updater.bot)

updater.start_polling()
updater.idle()
