import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v1, v2, weight):
        if v1 not in self.graph:
            self.graph[v1] = []
        self.graph[v1].append((v2, weight))
        
    def uniform_cost_search(self, start, goal):
        visited = set()
        queue = [(0, start, [])]  # Each element in the queue is a tuple: (cost, node, path)
        
        while queue:
            cost, node, path = heapq.heappop(queue)
            
            if node in visited:
                continue

            path = path + [node]
            if node == goal:
                return cost, path

            visited.add(node)

            for neighbor, weight in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))

        return None, None  # If the goal is not reached, return None

# Example usage:
g = Graph()
g.add_edge("A", "B", 10)
g.add_edge("A", "C", 6)
g.add_edge("B", "D", 15)
g.add_edge("C", "D", 4)

cost, result = g.uniform_cost_search('A', 'D')
if result:
    print("Cumulative Cost:", cost)
    print("Path:", result)
else:
    print("No path found")
