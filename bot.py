import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import start

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def ayuda(update, context):
    opciones = [[InlineKeyboardButton("Recibir saludo", callback_data="op1")],
                [InlineKeyboardButton("Mostrar apellido", callback_data="op2")],
                [InlineKeyboardButton("Recibir imagen", callback_data="op3")],
                [InlineKeyboardButton("Recibir documento", callback_data="op4")]]
    reply_markup = InlineKeyboardMarkup(opciones)
    name = update.message.chat["first_name"]
    logger.info(f"El usuario {name} ha solicitado ayuda.")
    text = f"Hola {name}, estos los comandos que puedo ejecutar:"
    update.message.reply_text(text, reply_markup=reply_markup)


def saludar(name, query):
    logger.info(f"El usuario {name} ha solicitado su nombre.")
    query.message.reply_text(f"Bienvenido {name}.")




def apellido(name, last_name, query):
    logger.info(f"El usuario {name} ha solicitado su apellido.")
    query.message.reply_text(f"Su apellido es: {last_name}.")


def imagen(chat_id, query, name):

    logger.info(f"El usuario {name} ha solicitado una imagen.")
    query.message.reply_text(f"Una foto de mi presidente \U0001F60D\U0001F60D\U0001F60D ")
    img = open("src/images/duque.jpg", "rb")
    query.bot.send_photo(chat_id=chat_id, photo=img)


def document(chat_id, query):
    logger.info("El usuario ha solicitado un documento.")
    query.message.reply_text("No estoy estoy mostrando documentos actualmente.")



def documento(update, context):
    logger.info("El usuario ha solicitado un documento.")
    documento = open("src/docs/documento.pdf", "rb")
    update.message.reply_text("Se está subiendo el documento, por favor espere...")
    chat_id = update.message.chat_id
    update.message.bot.sendDocument(chat_id=chat_id, document=documento, timeout=200)


def image(update, context, query):
    query.message.reply_text(f"Aqui una imagen de Danna la mas hermosa y su amix")
    logger.info("El usuario ha solicitado una imagen.")
    img = open("src/images/danna.jpg", "rb")
    chat_id = update.message.chat_id
    update.message.bot.sendPhoto(chat_id=chat_id, photo=img)


def grafo(update, context):
    logger.info(f"El usuario {update.message.chat['first_name']} ha solicitado un grafo.")
    text = update.message.text
    text = text.replace("/grafo ", "").strip()
    update.message.reply_text(f"Usted ha escrito: \n{text}")
    try:
        graph = eval(text)
        vertices = int(graph[0])
        aristas = int(graph[1])
        update.message.reply_text(f"La cantidad de vértices son: {vertices}")
        update.message.reply_text(f"La cantidad de aristas son: {aristas}")
    except Exception as e:
        logger.info("Ha ocurrido un error en los parámetros.")
        update.message.reply_text("Por favor, digite los parámetros nuevamente.")


def secuencia(update, context):
    text = update.message.text
    text = text.replace("/sec ", "").strip()
    try:
        secuencia = eval(text)
        for item in secuencia:
            item = int(item)
            update.message.reply_text(item)
    except Exception as e:
        logger.info("Ha ocurrido un error en los parámetros.")
        update.message.reply_text("Por favor, digite los parámetros nuevamente.")

def informacion(chat_id, query, name):
    logger.info(f"El usuario {name} pidio informacion")
    query.message.reply_text("No estoy mostrando informacion actualmente.")


def menu(update, context):
    query = update.callback_query
    query.answer()
    answer = query.data
    chat_id = query.message.chat_id
    name = query.message.chat["first_name"]
    last_name = query.message.chat["last_name"]
    if answer == "op1":
        saludar(name, query)
    elif answer == "op2":
        apellido(name, last_name, query)
    elif answer == "op3":
        imagen(chat_id, query, name)
    elif answer == "op4":
        document(chat_id, query)
