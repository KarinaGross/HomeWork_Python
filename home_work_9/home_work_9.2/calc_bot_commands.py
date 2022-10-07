from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello,  {update.effective_user.first_name}!')

async def bye (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Goodbye,  {update.effective_user.first_name}!')

async def calc (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    string = msg[6:]
    def funct(esp_str:str) -> int:
        par_close=esp_str.find(')')
        if par_close != -1:
            par_open = esp_str[:par_close].rfind('(')
            return funct(esp_str[:par_open] + str(funct(esp_str[par_open + 1:par_close])) \
                + (esp_str[par_close + 1:] if par_close != len(esp_str) else '')) 
        plus = esp_str.find('+')
        minus = esp_str.find('-')
        mult = esp_str.find('*') 
        div = esp_str.find('/')
        if (plus == -1) and (minus == -1) and (mult == -1) and (div == -1):
            return float(esp_str)
        if plus != -1:
            return funct(esp_str[:plus]) + funct(esp_str[plus + 1:])
        if minus != -1:
            return funct(esp_str[:minus]) - funct(esp_str[minus + 1:])
        if mult != -1:
            return funct(esp_str[:mult]) * funct(esp_str[mult + 1:])
        return int(funct(esp_str[:div]) / funct(esp_str[div + 1:]))

    result = funct(string)
    await update.message.reply_text(f'{result}')
    
async def help (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hello\n/bye\n/calc\n/help')