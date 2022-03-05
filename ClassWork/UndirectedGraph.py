class Graph:
   def __init__(self):
      self.graph=dict()
   def addEdge(self,V1,V2,value):
      if V1  not in self.graph and V2 not in self.graph:
         self.graph[V1]=[(V2,value)]
         self.graph[V2]=[(V1,value)]
      elif V1 in self.graph and V2 in self.graph:
         self.graph[V1].append((V2,value))
         self.graph[V2].append((V1,value))
      elif V1 not in self.graph and V2 in self.graph:
         self.graph[V1]=[(V2,value)]
         self.graph[V2].append((V1,value))
      elif V1  in self.graph and V2 not in self.graph:
         self.graph[V1].append((V2,value))
         self.graph[V2]=[(V1,value)]
      return self.graph