import queue
from UndirectedGraph import Graph # TODO : You must runf this file along with UndirectedGraph.py
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
    g.addEdge('A', 'B', 3)
    g.addEdge('A', 'E', 7)
    g.addEdge('A', 'D', 1)
    g.addEdge('B', 'E', 2)
    Graph = g.addEdge('E', 'F', 1)
    BFS('A', Graph)
