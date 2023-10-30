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
    

    def combined(self,fl,bl):
        l=fl[:]+bl[::-1]
        return l

        
    def bfs(self,s,d):
        f_visited=set()
        f_queue=[s]
        b_visited=set()
        b_queue=[d]
        fl=[]
        bl=[]
        l=[]
        while f_queue and b_queue:
            svertex=f_queue.pop(0)
            
            if svertex not in f_visited:
                f_visited.add(svertex)
                if svertex in bl:
                    return self.combined(fl,bl)
                fl.append(svertex)
                for ve in self.graph[svertex]:
                    if ve[0] not in f_visited:
                       f_queue.append(ve[0])
            
            dvertex=b_queue.pop(0)
            
            if dvertex not in b_visited:
                b_visited.add(dvertex)
                if dvertex in fl:
                    return self.combined(fl,bl)
                bl.append(dvertex)
                for ve in self.graph[dvertex]:
                    if ve[0] not in b_visited:
                       b_queue.append(ve[0])
            
            

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

print(g.bfs('A','F'))
            