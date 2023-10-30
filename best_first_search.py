import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = []
    
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
    
    def add_edge(self, v1, v2, w=0):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append((v2, w))
            self.graph[v2].append((v1, w))
            self.edges.append((v1, v2, w))

    def best_first_search(self, start, goal):
        visited = set()
        queue = [(0, start)]  # Use a priority queue with initial cost 0
        l = []
        while queue:
            cost, vertex = heapq.heappop(queue)  # Pop the node with the lowest cost
            if vertex not in visited:
                l.append(vertex)
                visited.add(vertex)
                if vertex == goal:
                    return l
                for neighbor, edge_cost in self.graph[vertex]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (edge_cost, neighbor))  # Prioritize nodes based on edge cost
        return l  # Return the visited nodes if the goal is not reached

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

g.add_edge("A", "B", 10)
g.add_edge("A", "C", 6)
g.add_edge("B", "D", 15)
g.add_edge("C", "D", 4)

print(g.best_first_search('A', 'D'))
