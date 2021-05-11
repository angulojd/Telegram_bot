import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start(update, context):
    logger.info("Se ha iniciado el bot.")
    name = update.message.chat["first_name"]
    update.message.reply_text(f"¡Hola, {name} \U0001F44B!, un gusto tenerte por acá.")

