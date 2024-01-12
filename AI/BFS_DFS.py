from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def recursive_dfs(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.recursive_dfs(neighbor, visited)

    def dfs(self, start_vertex):
        visited = {v: False for v in self.graph}
        print("Depth First Search (DFS):")
        self.recursive_dfs(start_vertex, visited)
        print()

    def recursive_bfs(self, queue, visited):
        if not queue:
            return

        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        self.recursive_bfs(queue, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        print("Breadth First Search (BFS):")
        self.recursive_bfs(queue, visited)
        print()

# Example Usage:
g = Graph()

n = int(input("Enter no of vertices: "))
for i in range(n):
    vertex = int(input("Enter the vertex to add: "))
    g.add_vertex(vertex)

m = int(input("Enter no of edges: "))
for i in range(m):
    u, v = map(int, input("Enter the edge (u.v or u v): ").replace('.', ' ').split())
    g.add_edge(u, v)

while True:
    print("1. Recursive Depth First Search (DFS)")
    print("2. Recursive Breadth First Search (BFS)")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        start_vertex = int(input("Enter the starting vertex for DFS: "))
        g.dfs(start_vertex)
    elif choice == 2:
        start_vertex = int(input("Enter the starting vertex for BFS: "))
        g.bfs(start_vertex)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
