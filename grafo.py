import logging
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.harary_graph import hnm_harary_graph, hkn_harary_graph

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
vertices = 5
aristas = 5
k = 1
def grafo(update, context):
    logger.info(f"El usuario {update.message.chat['first_name']} ha solicitado un grafo.")
    text = update.message.text
    text = text.replace("/grafo ","").strip()
    update.message.reply_text(f"Usted ha escrito: \n{text}")
    sw = False
    if(text == "/grafo"):
        update.message.reply_text("Por favor digitar la cantidad de vertices, cantidad de aristas, y grado de cada vertice respectivamente")
        update.message.reply_text("Ejemplo: /grafo (9,10,3)")
        sw = True
    try:
        graph = eval(text)
        vertices = int(graph[0])
        aristas = int(graph[1])
        k = int(graph[2])
        r = k * vertices / 2
        if(aristas > k and vertices > k and aristas >= vertices and aristas <= r):
            logger.info("El usuario digito bien los valores del grafo")
            update.message.reply_text(f"En su grafo puede tener un maximo de {r} aristas")
            mostrarGrafo(vertices,aristas,k,update, context)
        else:
            if (aristas <= k):
                logger.info("El usuario digito mal los valores del grafo")
                update.message.reply_text("El numero de aristas es menor o igual que el maximo de aristas por vertice")
            elif(vertices <= k):
                logger.info("El usuario digito mal los valores del grafo")
                update.message.reply_text("El numero de vertices es menor al numero maximo de aristas por vertice")
            elif(aristas < vertices):
                logger.info("El usuario digito mal los valores del grafo")
                update.message.reply_text("El numero de aristas no puede ser menor al numero de vertices")
            elif(aristas>r):
                logger.info("El usuario digito mal los valores del grafo")
                update.message.reply_text("El numero de aristas excedio el numero maximo de aristas que puede tener el grafo")
    except Exception as e:
        if(sw == False):
            update.message.reply_text("Por favor, digite los parámetros nuevamente de la siguiente forma: \n\n /grafo (V,E,K) \n\n donde en las letras van los numeros correspondientes.")
            update.message.reply_text("Ej: \n V = 9 \n E = 10 \n K = 3 \n /grafo (9,10,3)")
            logger.info("Ha ocurrido un error en los parámetros.")


class GraphVisualization:

    def __init__(self):
        self.visual = []
        self.visualRemove = []


    def visualize(self,update, context, aristas, sw):
        G = nx.Graph()
        cont = 0
        if(sw == True):
            for u, v, a in self.visual(data=True):
                if (cont < aristas):
                    temp = (u,v)
                    self.visualRemove.append(temp)
                cont = cont + 1
        G.add_edges_from(self.visualRemove)
        nx.draw_networkx(G)
        plt.savefig("src/images/blanco.jpg")
        img = open("src/images/blanco.jpg", "rb")
        chat_id = update.message.chat_id
        update.message.bot.sendPhoto(chat_id=chat_id, photo=img)
        update.message.reply_text("¡Felicidades ya tienes tu grafo!")
        plt.close()


def mostrarGrafo(vertices, aristas, k,update, context):
    G = GraphVisualization()
    g = hkn_harary_graph(k,vertices)
    G.visual = g.edges
    cont = 0
    sw = True
    if(k == 1):
        sw = False
        for u, v, a in G.visual(data=True):
            if(cont%2 == 0):
                temp = (u, v)
                G.visualRemove.append(temp)
            cont = cont + 1
        if(vertices%2!=0):
            temp = (vertices,vertices)
            G.visualRemove.append(temp)


    G.visualize(update, context, aristas, sw)
