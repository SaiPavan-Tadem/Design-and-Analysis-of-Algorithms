from collections import OrderedDict, defaultdict
import math
import heapq
from UndirectedGraph import Graph

#TODO : Prism Algorithm

def PrimsAlgo(src,Graph):
   cost = {v: math.inf for v in Graph}
   prev = {v: -1 for v in Graph}
   selected = {v: False for v in Graph}
   cost[src] = 0
   Q = [[u, ele] for u, ele in cost.items()]
   heapq.heapify(Q)
   edges = []
   while Q:
      u = heapq.heappop(Q)
      for v, w in Graph[u[0]]:
         if cost[v] > w :
            cost[v] = w
            prev[v] = u[0]
            heapq.heappush(Q, [v, w])
   return cost, prev

if __name__=='__main__':
         g = Graph()
         g.addEdge('A', 'B', 5)
         g.addEdge('A', 'C', 6)
         g.addEdge('A', 'D', 4)
         g.addEdge('B', 'C', 1)
         g.addEdge('B', 'D', 2)
         g.addEdge('C', 'D', 2)
         g.addEdge('C', 'E', 5)
         g.addEdge('C', 'F', 3)
         g.addEdge('D', 'F', 4)

         Graph = g.addEdge('E', 'F', 4)
         Graph= G = OrderedDict(Graph)
         cost,Prev=PrimsAlgo('A',Graph)
         print('cost :',cost)
         print('Prev  :', Prev)

cost: {'A': 0, 'B': 2, 'C': 1, 'D': 4, 'E': 4, 'F': 3}
Previous: {'A': None, 'B': 'D', 'C': 'B', 'D': 'A', 'E': 'F', 'F': 'C'}

