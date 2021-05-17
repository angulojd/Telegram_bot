import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def fibo(update, context):
    logger.info(f"El usuario {update.message.chat['first_name']} ha solicitado una subsecuencia fibonacci.")
    text = update.message.text
    text = text.replace("/fibonacci ", "").strip()
    update.message.reply_text(f"Usted ha escrito: \n{text}")
    sw = False
    if(text == "/fibonacci"):
        update.message.reply_text("Ingresaste a la creacion de una subsecuencia de fibonacci")
        update.message.reply_text("Por favor digitar los valores de la siguiente forma: \n\n"
                              "/fibonacci (1,1,1,1...n)\n\n"
                              "donde puede reemplazar el 1 por cualquier valor")
        sw = True
    try:
        fibo = eval(text)
        fibo = sorted(fibo)
        may = 0
        update.message.reply_text(f"Valores ordenados: \n{fibo}")
        for i in range(len(fibo)):
            if(may < int(fibo[i])):
                may = int(fibo[i])
        a, b = fibo[0], fibo[1]
        result = []
        while a <= may:
            result.append(a)
            a, b = b, a + b
        result2 = []
        for i in range(len(fibo)):
            sw = False
            for j in range(len(result)):
                if(fibo[i] == result[j]):
                    result2.append(fibo[i])
        update.message.reply_text(f"La subsecuencia fibonacci de los valores previamente ingresadio es: \n{result2}")

    except Exception as e:
        if(sw == False):
            logger.info("Ha ocurrido un error en los parámetros.")
            update.message.reply_text("Hubo un error en los valores digitados, por favor intente de nuevo")
