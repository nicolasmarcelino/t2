# Marco 2 — Componentes conexas

Problema: **796 – Critical Links**. Fonte: <https://onlinejudge.org/external/7/796.pdf>

# Caso particular

O problema original descreve uma rede de servidores com links bidirecionais, e a rede pode ter sub-redes isoladas (várias componentes conexas). Adaptamos o problema a um **grafo simples e não dirigido** (sem laços e sem arestas paralelas), com **V = 6** e **E = 6**.

- Vértices: `0, 1, 2, 3, 4, 5`
- Arestas: `0-1`, `0-2`, `1-2`, `1-3`, `2-3`, `4-5`
- Componentes esperadas: {0, 1, 2, 3} e {4, 5}

Entrada no formato do problema:

```
6
0 (2) 1 2
1 (3) 0 2 3
2 (3) 0 1 3
3 (2) 1 2
4 (1) 5
5 (1) 4
```

Listas de adjacência usadas pelo algoritmo:

| Vértice | Lista de adjacência |
|---------|---------------------|
| 0 | 1 → 2 |
| 1 | 0 → 2 → 3 |
| 2 | 0 → 1 → 3 |
| 3 | 1 → 2 |
| 4 | 5 |
| 5 | 4 |

# Algoritmo de componentes conexas (DFS recursiva)

## Estruturas de dados

- `adj[0..V-1]`: listas de adjacência (tabela acima).
- `comp[0..V-1]`: identificador da componente de cada vértice, inicializado com `-1`. O valor `-1` significa "ainda não visitado", então `comp[]` também faz o papel do vetor `visitado[]`.
- `n`: contador de componentes encontradas.
- Pilha de chamadas da recursão: guarda o caminho atual da DFS.

# Complexidade
## Tempo: O(V + E)

- O laço principal faz V iterações, cada uma com custo constante quando o vértice já foi visitado.
- `dfs` é chamada **exatamente uma vez por vértice**, porque um vértice só entra na recursão se `comp[w] = -1` e é marcado logo na entrada.
- Dentro de cada chamada, a lista de adjacência do vértice é percorrida **uma única vez**. Somando todas as listas, o total de posições visitadas é a soma dos graus, que é 2E (cada aresta aparece nas listas dos dois extremos).
- Total: V + 2E = O(V + E). No caso particular: 6 + 12 = 18 operações elementares.

Com matriz de adjacência, examinar os vizinhos de um vértice custaria O(V) mesmo para vértices de grau baixo, levando a O(V²). Por isso usamos listas de adjacência.

## Espaço: O(V + E)

- Listas de adjacência: O(V + E) (V cabeças de lista e 2E entradas; aqui, 6 e 12).
- Vetor `comp[]`: O(V).
- Pilha de recursão: O(V) no pior caso, quando o grafo é um caminho e a DFS desce por todos os vértices. No caso particular o máximo foi 4.
- Total: O(V + E).

## Custo das consultas de conectividade

Depois do pré-processamento em O(V + E), que é a execução de `componentes(G)`, a pergunta "os vértices `u` e `v` estão ligados?" se resume a:

```
conectados(u, v):
    retorne comp[u] = comp[v]
```

- **Consulta em O(1)**, sem percorrer o grafo. Exemplos: `conectados(0, 3)` → `0 = 0` → verdadeiro; `conectados(1, 5)` → `0 ≠ 1` → falso.
- A quantidade de componentes também sai em O(1), pois basta ler `n`.
- Sem o pré-processamento, cada consulta exigiria uma nova DFS, com custo O(V + E). Para Q consultas, seriam O(Q · (V + E)), contra O((V + E) + Q) com o vetor `comp[]`.
- Ressalva: o vetor `comp[]` vale para o grafo **estático**. Se arestas fossem inseridas ou removidas, ele precisaria ser recalculado (ou substituído por outra estrutura, como union-find).
