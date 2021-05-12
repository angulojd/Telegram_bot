import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, MessageEntity

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start(update, context):
    logger.info("Se ha iniciado el bot.")
    name = update.message.chat["first_name"]
    update.message.reply_text(f"¡Hola, {name} \U0001F44B!, un gusto tenerte por acá.")
    text = 'Puedes utilizar los siguientes comandos : \n\n/solucionRR - Solucion de relaciones de recurrencia. \n/fibonacci - Subsecuencia de Fibonacci. \n/grafo - Crea un grafo. \n/ayuda - Como funciona el bot e informacion de interes. \n\n'
    update.message.reply_text(text)
