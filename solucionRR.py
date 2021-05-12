import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def polinomio(update, context):
    logger.info("El usuario ha iniciado la solucion de recurrencia")
    name = update.message.chat["first_name"]
    update.message.reply_text(f" {name} has iniciado la solucion de un polinomio caracteristico de una relacion de recurrencia ")
    update.message.reply_text("Por favor digitar los coeficientes de su polinomio")