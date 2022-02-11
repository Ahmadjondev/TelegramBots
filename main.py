from telegram import Update
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext

import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom!")
    context.bot.send_message(chat_id == update.message.chat_id, text="Salom yana bir bor")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
# print(updater.bot)

updater.start_polling()
updater.idle()
