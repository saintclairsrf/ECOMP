import numpy as np
import igraph as ig
from igraph import *
import time

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


grafo, arestas = graph(4)

print("Grafo ",grafo)
print("\n")
print("Arestas", arestas)
print("\n")
tempoExecucao = []

tabLayout=[]
tabLayout=["random","circle","star","grid","graphopt","kamada_kawai","fruchterman_reingold","davidson_harel","mds","lgl"]

tab=[]
i=1
for i in range(len(tabLayout)):
    layout = grafo.layout(tabLayout[i])
    inicio = time.time()
    arquivoPDF=tabLayout[i]+".png"
    plot(grafo,arquivoPDF,layout=layout)
    fim=time.time()
    tempoExecucao= fim - inicio
    tab.append(tabLayout[i])
    tab.append(tempoExecucao)
    print (tabLayout[i],tempoExecucao )
print("\n")
print("Number of vertices in the graph:", grafo.vcount())
print("Number of edges in the graph", grafo.ecount())
print("Is the graph directed:", grafo.is_directed())
print("Maximum degree in the graph:", grafo.maxdegree())
print("Adjacency matrix:\n", grafo.get_adjacency())
