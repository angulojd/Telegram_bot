import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import ayuda

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def menuAyuda(update, context):
    query = update.callback_query
    query.answer()
    answer = query.data
    chat_id = query.message.chat_id
    name = query.message.chat["first_name"]
    last_name = query.message.chat["last_name"]
    if answer == "op6":
        ayuda.descripcion(name, query)
    elif answer == "op7":
        ayuda.funciones(name,query)
    elif answer == "op8":
        ayuda.comandos(name, query)
    elif answer == "op9":
        ayuda.infoCreador(name, query)