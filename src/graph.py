
class Graph:

    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(self.V)]

    def __str__(self):
        lines = ["%d vertices, %d edges" % (self.V, self.E)]
        for v in range(self.V):
            neighbors = " ".join(str(w+1) for w in self.adj[v])
            lines.append("%d: %s" % (v+1, neighbors))
        return "\n".join(lines)

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1