import math
import heapq
from UndirectedGraph import Graph  #TODO: Run along with UndirectedGraph.py

#TODO: Dijkstras Algorithm

def Dijkstras(src, dest, Graph):
   distance = {V: math.inf for V in Graph}
   Prev = {V: -1 for V in Graph}
   distance[src] = 0
   H = [ele for ele in distance.items()]
   heapq.heapify(H)
   while H:
      # print(distance)
      u = heapq.heappop(H)
      if distance[u[0]] != math.inf:
         for v in Graph[u[0]]:
            if distance[v[0]] > distance[u[0]] + v[1]:
               distance[v[0]] = distance[u[0]] + v[1]
               Prev[v[0]] = u[0]
               heapq.heappush(H, (v[0], distance[v[0]]))

   return distance, Prev
if __name__=='__main__':
         g = Graph()
         g.addEdge('A', 'B', 3)
         g.addEdge('A', 'E', 7)
         g.addEdge('A', 'D', 1)
         g.addEdge('B', 'E', 2)
         Graph = g.addEdge('E', 'F', 1)
         distance,Prev=Dijkstras('A', 'F', Graph)
         print('Distance  :',distance)
         print('Previous :',Prev)
