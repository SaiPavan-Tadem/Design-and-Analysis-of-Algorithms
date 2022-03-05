from collections import OrderedDict, defaultdict
import math
import heapq
from UndirectedGraph import Graph
def find(u,Parent):
   if Parent[u]==-1:
      return u
   return find(Parent[u],Parent)
def union(u, v, Parent, Rank):
   root_u = find(u, Parent)
   root_v = find(v, Parent)
   if root_u == root_v:
      return
   if Rank[root_u] > Rank[root_v]:
      Parent[root_v] = root_u
   else:
      Parent[root_u] = root_v
      Rank[root_v] = Rank[root_v] + 1
def KruskalsAlgo(Graph):
   Parent = {v: -1 for v in Graph}
   Rank = {v: 0 for v in Graph}
   li = []
   cost = 0
   mst = defaultdict(dict)
   G = OrderedDict(Graph)
   for u, edges in Graph.items():
      for v, w in edges:
         li.append([u, v, w])
   li = sorted(li, key=lambda x: x[2])
   for u, v, w in li:
      if find(u, Parent) != find(v, Parent):
         cost = cost + w
         mst[u][v] = w
         union(u, v, Parent, Rank)
   return mst,cost
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
         mst,cost=KruskalsAlgo(Graph)
         print('Distance  :',mst)
         print('Previous :',cost)


