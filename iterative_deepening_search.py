#iterative deepening depth first search

class Graph:
    def __init__(self):
        self.graph={}
        self.edges=[]
    
    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]
    def add_edge(self,v1,v2,w):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append((v2,w))
            self.graph[v2].append((v1,w))
            self.edges.append((v1,v2,w))
    
    def dfs(self,s,visited=set(),l=[],m=0):
        if m>=0:
            if s[0] not in visited:
                visited.add(s[0])
                l.append(s[0])
                for vertex in self.graph[s[0]]:
                    self.dfs(vertex,visited,l,m-1)
        return l

g=Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")


g.add_edge("A", "C", 6)
g.add_edge("A", "B", 10)
# g.add_edge("A", "D", 5)
g.add_edge("B", "D", 15)
g.add_edge("B", "E", 15)
g.add_edge("C", "F", 4)
g.add_edge("E", "F", 4)

for i in range(3):
    print(g.dfs('A',set(),[],i),i)
        