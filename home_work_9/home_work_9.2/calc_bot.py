from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from calc_bot_commands import *


app = ApplicationBuilder().token("5662048036:AAFfSqSOkNhf_NdM11a36gfQfjwep_YGs-o").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("bye", bye))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("calc", calc))

app.run_polling()