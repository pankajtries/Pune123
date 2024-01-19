class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if 0 <= i < len(parent):
            return i if parent[i] == i else self.find(parent, parent[i])
        else:
            return i

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if 0 <= xroot < len(rank) and 0 <= yroot < len(rank):
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [node for node in range(self.V)]
        rank = [0] * self.V
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


def get_user_input():
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        g.add_edge(u, v, weight)

    return g


def main():
    g = get_user_input()
    print("Minimum Spanning Tree:")
    g.kruskal_algo()


if __name__ == "__main__":
    main()
