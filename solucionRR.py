import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from sympy import *
x = symbols('x')
init_printing(use_unicode=True)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def polinomio(update, context):
    logger.info("El usuario ha iniciado la solucion de recurrencia")
    name = update.message.chat["first_name"]
    text = update.message.text
    text = text.replace("/solucionRR ", "").strip()
    update.message.reply_text(f"Usted ha escrito: \n{text}")
    sw2 = False
    if (text == "/solucionRR"):
        update.message.reply_text(f" {name} has iniciado la solucion de un polinomio caracteristico de una relacion de recurrencia ")
        update.message.reply_text("Por favor digitar los coeficientes de su polinomio: ")
        update.message.reply_text("Ejemplo: /solucionRR (1,1,-6,-4,8)")
        sw2 = True
    try:
        pol = eval(text)
        mat = []
        for i in range(len(pol)):
            sw = int(pol[i])
            mat.append(sw)
        resolver(mat,update,context)

    except Exception as e:
        if(sw2 == False):
            logger.info("Ha ocurrido un error en los parámetros.")
            update.message.reply_text("Hubo un error en los valores digitados, por favor intente de nuevo")

def resolver(mat, update, context):
    grado = int(len(mat))-1
    poli = ""
    stra = "*x**"
    postivo = "+"
    negativo = "-"
    for i in range(len(mat)):
        grad = str(int(grado))
        grado = grado - 1
        if(mat[i] < 0):
            temp = mat[i]*-1
            coef = str(temp)
            poli = poli + negativo+coef+stra+grad
        else:
            coef = str(mat[i])
            poli = poli + postivo+coef+stra+grad
    sw = factor(poli)
    l = sympify(poli)
    if(sw == l):
        update.message.reply_text("El polinomio tiene raices complejas dificil de resolver")
    else:
        temp0 = factor_list(poli)
        res = solve(poli)
        update.message.reply_text(f"Las raices para la solucion son las siguientes: {sw} ")
        contDeC = 0
        contDeN = 2
        valorConstante = "c"
        elevado = "^"
        recurrencia = "n"
        positivo = "+"
        sw1 = False
        resultado = ""
        resolv = temp0[1]

        for i in range(len(resolv)):
            tmp = resolv[i]
            pos1 = tmp[0]
            pos2 = tmp[1]
            res = solve_linear(pos1)
            tmp = str(int(res[1]))
            for j in range(pos2):
                tempC = str(int(contDeC))
                if(pos2 == 1):
                    if(sw1 == False):
                        resultado = resultado + valorConstante + tempC + "(" + tmp + ")" + elevado + recurrencia
                        contDeC = contDeC + 1
                        sw1 = True
                    else:
                        resultado = resultado + positivo + valorConstante + tempC + "(" + tmp + ")" + elevado + recurrencia
                        contDeC = contDeC + 1
            if(pos2 >= 2):
                ls = 0
                for i in range(pos2):
                    print(ls)
                    if(ls == 0):
                        resultado = resultado + positivo + valorConstante + tempC + "(" + tmp + ")" +elevado + recurrencia
                        contDeC = contDeC + 1
                    elif(ls == 1):
                        resultado = resultado + positivo + valorConstante + tempC + recurrencia + "(" +tmp + ")" + elevado + recurrencia
                        contDeC = contDeC + 1
                    else:
                        tempN = str(int(contDeN))
                        resultado = resultado + positivo + valorConstante + tempC + recurrencia + elevado + tempN + "(" + tmp + ")" + elevado + recurrencia
                        contDeN = contDeN + 1
                        contDeC = contDeC + 1
                    ls = ls + 1
        update.message.reply_text(f"La forma solucion de la relacion de recurrencia es: \n\n"
                                  f"f_n = {resultado}")



