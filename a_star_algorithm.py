import heapq
import math

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2, w=0):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append((v2, w))
            self.graph[v2].append((v1, w))

    def a_star_search(self, start, goal):
        open_set = [(0, start)]  # Priority queue with initial cost 0
        came_from = {}  # Mapping from a node to the previous node in the optimal path
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor, cost in self.graph[current]:
                tentative_g_score = g_score[current] + cost

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None

    def heuristic(self, node, goal):
        # Example heuristic: Euclidean distance
        x1, y1 = node
        x2, y2 = goal
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)
        return path

# Example usage:
g = Graph()
g.add_vertex((0, 0))
g.add_vertex((0, 1))
g.add_vertex((1, 0))
g.add_vertex((1, 1))

g.add_edge((0, 0), (0, 1), 1)
g.add_edge((0, 0), (1, 0), 1)
g.add_edge((0, 1), (1, 1), 1)
g.add_edge((1, 0), (1, 1), 1)

start_node = (0, 0)
goal_node = (1, 1)

path = g.a_star_search(start_node, goal_node)

if path:
    print("A* Path:", path)
else:
    print("No path found")
