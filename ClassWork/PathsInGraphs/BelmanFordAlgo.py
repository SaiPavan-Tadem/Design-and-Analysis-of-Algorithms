# TODO : You must run this along with DirectedGraph.py file
import math
import heapq
from DirectedGraph import Graph     # TODO here directed graph is imported

def BFA(src,Graph):   # TODO Belman Ford Algorithm
   distance = {v: math.inf for v in Graph}
   Prev = {v: -1 for v in Graph}
   distance[src] = 0
   for i in range(1, len(Graph) + 1):
      for u in Graph:
         for v,w in Graph[u]:
            if distance[v] > distance[u] + w:
               distance[v] = distance[u] + w
               Prev[v[0]]=u
   return distance,Prev

# TODO Runs here
if __name__=='__main__':
         g = Graph()
         g.addEdge('S', 'A', 10)
         g.addEdge('S', 'G', 8)
         g.addEdge('A', 'E', 2)
         g.addEdge('B', 'A', 1)
         g.addEdge('B', 'C', 1)
         g.addEdge('C', 'D', 3)
         g.addEdge('D', 'E', -1)
         g.addEdge('E', 'B', -2)
         g.addEdge('F', 'E', -1)
         g.addEdge('F', 'A', -4)
         Graph = g.addEdge('G', 'F', 1)
         print(Graph)
         distance,Prev=BFA('S',Graph)
         print('Distance  :',distance)
         print('Previous :',Prev)