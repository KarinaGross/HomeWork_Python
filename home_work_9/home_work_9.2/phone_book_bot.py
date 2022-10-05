from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("5722238267:AAEtKNJRpJk7wUaIK28O4LfIqUQB2fYpFq0").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("bye", bye))
app.add_handler(CommandHandler("help", help))
# app.add_handler(CommandHandler("add_number", add_number))
# app.add_handler(CommandHandler("delete_number", delete_number))
# app.add_handler(CommandHandler("looking_for_number", looking_for_number))
# app.add_handler(CommandHandler("view_the_list", view_the_list))



print('server start')
app.run_polling()