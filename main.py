from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


import ayuda
from config import TOKEN
import bot
import start, solucionRR, grafo, fibo

def main():
    # Establecemos una conexión entre nuestro programa y el bot.
    updater = Updater(TOKEN, use_context=True)  # Insertemos el Token del bot.
    dp = updater.dispatcher

    # Establecer los comandos que ejecutará el bot.
    dp.add_handler(CommandHandler("start", start.start))
    dp.add_handler(CommandHandler("ayuda", ayuda.ayuda))
    dp.add_handler(CallbackQueryHandler(bot.menuAyuda, pattern="op6"))
    dp.add_handler(CallbackQueryHandler(bot.menuAyuda, pattern="op7"))
    dp.add_handler(CallbackQueryHandler(bot.menuAyuda, pattern="op8"))
    dp.add_handler(CallbackQueryHandler(bot.menuAyuda, pattern="op9"))
    dp.add_handler(CommandHandler("solucionRR", solucionRR.polinomio))
    dp.add_handler(CommandHandler("grafo", grafo.grafo))
    dp.add_handler(CommandHandler("fibonacci", fibo.fibo))
    # Iniciamos el bot.
    updater.start_polling()
    # Mantener al bot ejecutándose hasta que ocurra una interrupción.
    updater.idle()


if __name__ == '__main__':
    main()