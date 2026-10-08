# Marco 4

## Solução
_A solução foi implementada em Python e pode ser acessada pela pasta `/src` na raíz do repositório.

## Estrutura

```
src/
├── cc.py     (algoritmo de componentes conexas adaptado)
├── graph.py  (grafo como lista de adjacência)
└── main.py   (leitura e saída de dados/solução aplicada)
```

## Execução

```bash
python ./src/main.py < ./dados/casos-de-teste.tx
```

## Adaptações do _algs4_

A implementação teve como referência [algs4-py](https://github.com/carubbi/RPG/tree/main/algs4-py).

`cc.py` é o algoritmo de componentes conexas e foi adaptado.

```python
class CC:

    def __init__(self, G, r):
        self.marked = [False for _ in range(G.V)]
        self.id = [0 for _ in range(G.V)]
        self._size = [0 for _ in range(G.V)]
        self.count = 0

        for s in range(G.V):
         # remoção lógica do vértice r ao iterar sobre o grafo G
            if not self.marked[s] and s != r:
                self.dfs(G, s, r)
                self.count += 1

    def dfs(self, G, v, r):
        self.marked[v] = True
        self.id[v] = self.count
        self._size[self.count] += 1
        for w in G.adj[v]:
            # remoção lógica do vértice r na visitação dos vizinhos de v
            if not self.marked[w] and w != r:
                self.dfs(G, w, r)
```

