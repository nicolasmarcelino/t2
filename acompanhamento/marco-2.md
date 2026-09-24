# Marco 2 — Componentes conexas

Problema: **315 – Network**. Fonte: <https://onlinejudge.org/external/3/315.pdf>

# Caso particular

O problema original descreve uma rede de lugares (numerados a partir de 1) ligados por linhas bidirecionais e pede o número de **lugares críticos**, isto é, aqueles cuja remoção desconecta parte da rede. A rede pode ter sub-redes isoladas (várias componentes conexas). Adaptamos o problema a um **grafo simples e não dirigido** (sem laços e sem arestas paralelas), com **V = 6** e **E = 5**.

- Vértices: `1, 2, 3, 4, 5, 6`
- Arestas: `1-2`, `2-3`, `2-4`, `3-4`, `5-6`
- Componentes esperadas: {1, 2, 3, 4} e {5, 6}
- Resposta esperada: **1** lugar crítico (o lugar `2`). Removendo `2`, o vértice `1` fica isolado e o número de componentes passa de 2 para 3. Os vértices `3` e `4` formam um ciclo com `2`, então remover qualquer um deles não desconecta ninguém. Em {5, 6}, remover um extremo deixa o outro isolado, mas o número de componentes não aumenta.

Entrada no formato do problema (cada bloco termina com uma linha `0`, e a entrada termina com `N = 0`):

```
6
1 2
2 1 3 4
3 2 4
4 2 3
5 6
6 5
0
0
```

Saída esperada:

```
1
```

Listas de adjacência usadas pelo algoritmo:

| Vértice | Lista de adjacência |
|---------|---------------------|
| 1 | 2 |
| 2 | 1 → 3 → 4 |
| 3 | 2 → 4 |
| 4 | 2 → 3 |
| 5 | 6 |
| 6 | 5 |

# Algoritmo de componentes conexas (DFS recursiva)

Um lugar é crítico se, ao removê-lo, o número de componentes conexas **aumenta**. Por isso, o algoritmo de componentes é executado uma vez no grafo original e depois uma vez para cada vértice removido, comparando as contagens.

## Estruturas de dados

- `adj[1..V]`: listas de adjacência (tabela acima).
- `comp[1..V]`: identificador da componente de cada vértice, inicializado com `-1`. O valor `-1` significa "ainda não visitado", então `comp[]` também faz o papel do vetor `visitado[]`.
- `n`: contador de componentes encontradas.
- Vértice removido `r`: marcado temporariamente com `comp[r] = -2`. Como a DFS só entra em um vizinho `w` quando `comp[w] = -1`, o vértice `r` é ignorado naturalmente, sem alterar as listas de adjacência.
- Pilha de chamadas da recursão: guarda o caminho atual da DFS.

## Execução no caso particular

- Grafo original: `n = 2` componentes.
- Removendo `1`: {2, 3, 4} e {5, 6}, então 2 componentes (não aumentou).
- Removendo `2`: {1}, {3, 4} e {5, 6}, então **3 componentes** (aumentou, `2` é crítico).
- Removendo `3`: {1, 2, 4} e {5, 6}, então 2 componentes (não aumentou).
- Removendo `4`: {1, 2, 3} e {5, 6}, então 2 componentes (não aumentou).
- Removendo `5`: {1, 2, 3, 4} e {6}, então 2 componentes (não aumentou).
- Removendo `6`: {1, 2, 3, 4} e {5}, então 2 componentes (não aumentou).
- Apenas a remoção de `2` aumenta o número de componentes, portanto o total de lugares críticos é **1**, como esperado.

# Complexidade

## Tempo: O(V · (V + E))

Cada execução do algoritmo de componentes custa O(V + E):

- O laço principal faz V iterações, cada uma com custo constante quando o vértice já foi visitado.
- `dfs` é chamada **exatamente uma vez por vértice**, porque um vértice só entra na recursão se `comp[w] = -1` e é marcado logo na entrada.
- Dentro de cada chamada, a lista de adjacência do vértice é percorrida **uma única vez**. Somando todas as listas, o total de posições visitadas é a soma dos graus, que é 2E (cada aresta aparece nas listas dos dois extremos).
- Total por execução: V + 2E = O(V + E). No caso particular: 6 + 10 = 16 operações elementares.

Para encontrar os lugares críticos, o algoritmo é executado uma vez no grafo original e V vezes com um vértice removido, ou seja, V + 1 execuções. Total: O(V · (V + E)). No caso particular, no máximo 7 × 16 = 112 operações elementares (na prática menos, pois o vértice removido e suas arestas são ignorados).

Com matriz de adjacência, examinar os vizinhos de um vértice custaria O(V) mesmo para vértices de grau baixo, levando a O(V³) no total. Por isso usamos listas de adjacência.

## Espaço: O(V + E)

- Listas de adjacência: O(V + E) (V cabeças de lista e 2E entradas; aqui, 6 e 10).
- Vetor `comp[]`: O(V), reinicializado a cada remoção, sem alocar novo espaço.
- Pilha de recursão: O(V) no pior caso, quando o grafo é um caminho e a DFS desce por todos os vértices. No caso particular o máximo foi 4 (caminho 1 → 2 → 3 → 4 no grafo original).
- Total: O(V + E).

## Custo das consultas de conectividade

Depois do pré-processamento em O(V + E), que é a execução do algoritmo de componentes no grafo original, a pergunta "os vértices `u` e `v` estão ligados?" se resume a comparar `comp[u]` com `comp[v]`: se forem iguais, estão na mesma componente.

- **Consulta em O(1)**, sem percorrer o grafo. Exemplos: `1` e `4` → `comp` igual (`0 = 0`) → ligados; `2` e `6` → `comp` diferente (`0 ≠ 1`) → não ligados.
- A quantidade de componentes também sai em O(1), pois basta ler `n`.
- Sem o pré-processamento, cada consulta exigiria uma nova DFS, com custo O(V + E). Para Q consultas, seriam O(Q · (V + E)), contra O((V + E) + Q) com o vetor `comp[]`.
- Ressalva: o vetor `comp[]` vale para o grafo **estático**. Se arestas fossem inseridas ou removidas, ele precisaria ser recalculado (ou substituído por outra estrutura, como union-find).
- Observação para o problema 315: a abordagem "remover cada vértice e recontar componentes" é suficiente para as entradas pequenas do problema (N < 100). Uma única DFS com `low-link` (algoritmo de Tarjan) resolveria em O(V + E), mas foge do escopo deste marco.
