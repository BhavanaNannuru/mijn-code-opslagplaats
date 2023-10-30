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