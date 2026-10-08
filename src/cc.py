from graph import Graph

class CC:

    def __init__(self, G, r):
        self.marked = [False for _ in range(G.V)]
        self.id = [0 for _ in range(G.V)]
        self._size = [0 for _ in range(G.V)]
        self.count = 0

        for s in range(G.V):
            if not self.marked[s] and s != r:
                self.dfs(G, s, r)
                self.count += 1

    def dfs(self, G, v, r):
        self.marked[v] = True
        self.id[v] = self.count
        self._size[self.count] += 1
        for w in G.adj[v]:
            if not self.marked[w] and w != r:
                self.dfs(G, w, r)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def size(self, v):
        if v < 0 or v >= len(self.marked):
            raise ValueError("vertex %s is not between 0 and %s" %
                             (v, len(self.marked) - 1))
        return self._size[self.id[v]]

if __name__ == "__main__":
    import sys
    f = open(sys.argv[1])
    V = int(f.readline())
    E = int(f.readline())
    g = Graph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    cc = CC(g)
    print(cc.count, " components")
    components = []
    for i in range(cc.count):
        components.append([])

    for v in range(g.V):
        components[cc.id[v]].append(v)

    for i in range(cc.count):
        for v in components[i]:
            print(v, " ", end='')
        print()