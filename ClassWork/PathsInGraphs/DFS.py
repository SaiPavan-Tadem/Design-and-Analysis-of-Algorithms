from UndirectedGraph import Graph # TODO: Run this file along with UndirectedGraph.py
def DFS(src,Graph):
    Visted={V:False for V in Graph}
    Prev={V:-1 for V in Graph.keys()}
    Stack=[]
    Stack.append(src)
    while Stack:
        #print(Stack,end=' ')
        u=Stack.pop()
        if Visted[u]==False:
          print(u,end=' :')
          Visted[u]=True
          for edges in Graph[u]:
              Stack.append(edges[0])
    return
if __name__=='__main__':
         g = Graph()
         g.addEdge('A', 'B', 3)
         g.addEdge('A', 'E', 7)
         g.addEdge('A', 'D', 1)
         g.addEdge('B', 'E', 2)
         Graph = g.addEdge('E', 'F', 1)
         DFS('A',Graph)
       