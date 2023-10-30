#dfs

class Graph:
    def __init__(self):
        self.graph={}
        self.edges=[]

    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]
    
    def add_edge(self,v1,v2,w=0):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append((v2,w))
            self.graph[v2].append((v1,w))
            self.edges.append((v1,v2,w))
    
    def dfs(self,v,visited=set(),l=[]):
        if v not in visited:
            visited.add(v)
            l.append(v)
            for vertex in self.graph[v]:
                self.dfs(vertex[0],visited,l)
        return l
    
g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B", 10)
g.add_edge("A", "C", 6)
# g.add_edge("A", "D", 5)
g.add_edge("B", "D", 15)
g.add_edge("C", "D", 4)

print(g.dfs('A'))