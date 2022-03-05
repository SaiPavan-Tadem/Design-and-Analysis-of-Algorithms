import queue

from UndirectedGraph import Graph
# class Graph:
#     def __init__(self):
#         self.graph = dict()
#
#     def addEdge(self, V1, V2, value):
#         if V1 not in self.graph and V2 not in self.graph:
#             self.graph[V1] = [(V2, value)]
#             self.graph[V2] = [(V1, value)]
#         elif V1 in self.graph and V2 in self.graph:
#             self.graph[V1].append((V2, value))
#             self.graph[V2].append((V1, value))
#         elif V1 not in self.graph and V2 in self.graph:
#             self.graph[V1] = [(V2, value)]
#             self.graph[V2].append((V1, value))
#         elif V1 in self.graph and V2 not in self.graph:
#             self.graph[V1].append((V2, value))
#             self.graph[V2] = [(V1, value)]
#         return self.graph
#
# DFS Using Stack
# BFS Using Queue

def BFS(src, Graph):
    Visited = {V: False for V in Graph.keys()}
    Prev = {V: -1 for V in Graph.keys()}
    Q = queue.Queue()
    Q.put(src)
    while Q.qsize() > 0:
        u = Q.get()
        if Visited[u] == False:
            print(u, end=':')
            Visited[u] = True
            for edges in Graph[u]:
                Q.put(edges[0])

    return

if __name__ == '__main__':
    g = Graph()
    g.addEdge('E', 'S', 3)
    g.addEdge('E', 'D', 7)
    g.addEdge('S', 'A', 1)
    g.addEdge('S', 'C', 1)
    g.addEdge('S', 'D', 1)
    g.addEdge('B', 'E', 2)
    g.addEdge('A', 'B', 2)

    Graph = g.addEdge('B', 'C', 2)
    BFS('A', Graph)

# 'E': {'S', 'D'},
# 'S': {'A', 'E', 'C', 'D'},
# 'A': {'S', 'B'},
# 'B': {'A', 'C'},
# 'C': {'S', 'B'},
# 'D': {'S', 'E'}