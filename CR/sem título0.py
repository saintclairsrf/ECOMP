import numpy as np
import igraph as ig
from igraph import *
import time
import matplotlib.pyplot as plt

# function to check if x is power of 2 
def isPowerOfTwo( x ): 
  
    # First x in the below expression is 
    # for the case when x is 0 
    return x and (not(x & (x - 1))) 
  
# function to check whether the two numbers 
# differ at one bit position only 
def differAtOneBitPos( a , b ): 
    return isPowerOfTwo(a ^ b) 

#Função graph é lenta para n grandes, estimo que ela seja O(n²)
def graph(n):
  vertices = 2 ** n
  arestas = []
  grafo = Graph()
  grafo.add_vertices(vertices)

  for x in range(vertices):
    for y in range(vertices):
      if (differAtOneBitPos(x, y)):
        if (y,x) not in arestas:
          arestas.append((x,y))

  grafo.add_edges(arestas)

  return grafo, arestas


grafo, arestas = graph(3)
print("\n")
a=[]
a=grafo
print(type(a))
print("---------------------------", a.Read_GML)

print("Grafo ",grafo)

#print("\n")
print("Arestas", arestas)
print("\n")
print("Quantidade de arestas ==> ", len(arestas))
print("\n")

print("===== ")
summary(grafo)
print("Grafo ",grafo)
print("===== ")

tempoExecucao = []
tempoExecucao = np.array(tempoExecucao)
print(type(tempoExecucao))
tabLayout=[]
tabLayout=["random","circle","star","grid","graphopt","kamada_kawai","fruchterman_reingold","davidson_harel","mds","lgl"]

v=[]
for i in range(len(arestas)):
  v.append(i)

tab=[]
i=1
for i in range(len(tabLayout)):
    layout = grafo.layout(tabLayout[i])
    inicio = time.time()
    arquivoPDF=tabLayout[i]+".png"
    grafo = Graph(vertex_attrs={"label": v, "color": "Cyan", "size": "30", "label_size" : "20"}, edges=arestas, directed=False)
    plot(grafo,arquivoPDF,layout=layout)
    plot(grafo.get_adjacency(), "aa.png", layout=layout)
    fim=time.time()
    tempoExecucao = fim - inicio
    tab.append(tabLayout[i])
    tab.append(tempoExecucao)
    print (tabLayout[i],tempoExecucao )
print("\n")
print("Number of vertices in the graph:", grafo.vcount())
print("Number of edges in the graph", grafo.ecount())
print("Is the graph directed:", grafo.is_directed())
print("Maximum degree in the graph:", grafo.maxdegree())
print("Adjacency matrix:\n", grafo.get_adjacency())

plt.barh (tabLayout, tempoExecucao, color="red")
plt.show()

# plot(grafo, layout=layout, vertex_label=alfabeto, vertex_color="Blue", **visual_style)
#grafo = Graph(vertex_attrs={"label": v, "color": "Cyan"}, edges=arestas, directed=False)
#plot(grafo, layout=layout)

######################################################
"""

tempos = np.array([0.2979471683502197, 0.21873712539672852, 0.2164618968963623, 0.14659905433654785, 0.1934821605682373,
                   0.17554640769958496, 0.19448590278625488, 0.22937893867492676, 0.18954062461853027, 0.21442580223083496])
grafos = tabLayout

#print(type(tempos))
#tempos = np.array(tempoExecucao)

cores=['gold', 'red', 'blue', 'magenta', 'green','lightskyblue', 'yellowgreen', 'yellow', 'cyan', 'gray']
# o atributo explode indica que fatia do gráfico será destacada. No exemplo abaixo, será a primeira fatia. A quantidade de valores é igual ao número de fatias do gráfico. 
#explode = (0.1, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Atribuindo um título ao gráfico
plt.title("Tempos de geração dos grafos em segundos pizza")

#plt.pie(tempos, explode=explode, labels=grafos, colors=cores, autopct='%1.1f%%', shadow=True, startangle=90)
#plt.pie(tempos, labels=grafos, colors=cores, autopct='%1.2f%', shadow=True, startangle=90)
#plt.pie(tempos, labels=grafos, colors=cores, autopct='%1.2f%', shadow=True)
#plt.pie(tempos, labels=grafos, colors=cores)

#Adiciona Legenda
#plt.legend(grafos, bbox_to_anchor=(1.0, 1.0),loc='upper right')

#Centraliza o gráfico
plt.axis('equal')

#Ajusta o espaçamento para evitar o recorte do rótulo
#plt.tight_layout()

#plt.show()
#summary(tempos)
plt.title("Tempos de geração dos grafos em segundos boxplot")
plt.boxplot(tempos, main="Boxplot: tempos", col="blue")
plt.show()
"""