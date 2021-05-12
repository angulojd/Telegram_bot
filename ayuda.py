import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, MessageEntity
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def ayuda(update, context):
    opciones = [[InlineKeyboardButton("Descripción del bot", callback_data="op6")],
                [InlineKeyboardButton("Funciones del bot", callback_data="op7")],
                [InlineKeyboardButton("Lista de comandos", callback_data="op8")],
                [InlineKeyboardButton("Información del creador", callback_data="op9")]]
    reply_markup = InlineKeyboardMarkup(opciones)
    name = update.message.chat["first_name"]
    logger.info(f"El usuario {name} ha solicitado ayuda.")
    text = f"Hola {name}, estos los comandos que puedo ejecutar:"
    update.message.reply_text(text, reply_markup=reply_markup)

def descripcion(name, query):
    logger.info(f"El usuario {name} pidio descripcion")
    query.message.reply_text("Es un bot con fines completamente académicos para la asignatura de Estructuras Discretas de la Universidad del Norte.")

def funciones(name, query):
    logger.info(f"El usuario {name} pidio funciones")
    text = ("Las funciones del bot son las siguientes: \n\n"
            "1.	Mostrar la forma solución de una relación de recurrencia\n"
            "2.	Mostrar la subsecuencia de una función de Fibonacci de una secuencia previamente suministrada por el usuario \n"
            "3.	Creación de grafos \n\n")
    query.message.reply_text(text)
def comandos(name, query):
    logger.info(f"El usuario {name} pidio lista de comandos")
    text = 'Puedes utilizar los siguientes comandos : \n\n/solucionRR - Solucion de relaciones de recurrencia. \n/fibonacci - Subsecuencia de Fibonacci. \n/grafo - Crea un grafo. \n/ayuda - Como funciona el bot e informacion de interes. \n\n'
    query.message.reply_text(text)

def infoCreador(name, query):
    logger.info(f"El usuario {name} pidio informacion del creador")
    text="El bot fue diseñado por un estudiante en ingeniería de sistemas y computación de la Universidad del Norte (Colombia-Atlántico) \n\n" \
         "Nombre: Jesus Daniel Angulo Rivera \n" \
         "Usuario de Telegram: @Jesus_Angulo \n"
    query.message.reply_text(text)
