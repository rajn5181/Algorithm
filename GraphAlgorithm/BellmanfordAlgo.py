class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def bellman_ford(self, source):
        # Step 1: Initialization
        distance = [float('inf')] * self.vertices
        predecessor = [None] * self.vertices
        distance[source] = 0

        # Step 2: Relaxation
        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

        # Step 3: Check for Negative Cycles
        for u, v, w in self.graph:
            if distance[u] + w < distance[v]:
                print("Graph contains a negative cycle")
                return None

        return distance, predecessor

