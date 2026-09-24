# Marco 2
A partir de um grafo baseado em um caso particular, é apresentado a sua representação computacional, suas propriedades de conectividade e o rastreamento do algoritmo de componentes conexas.

## Grafo
O grafo a seguir é baseado em um dos casos de teste disponibilizados pela plataforma.

A representação escolhida é a lista de adjacência, pois ela é adequada para representar grafos esparsos, armazenando para cada vértice apenas os seus vizinhos diretamente conectados. Essa estrutura também permite percorrer eficientemente as conexões durante a execução da DFS.

```
1: [2]
2: [1, 3, 5]
3: [2]
4: [5]
5: [4, 6, 2]
6: [5]
```

## Conectividade
Segue abaixo as propriedades de conectividade do grafo.

exc(1) = max{1, 2, 3, 2, 3} = 3

exc(2) = max{1, 1, 2, 1, 2} = 2

exc(3) = max{2, 1, 3, 2, 3} = 3

exc(4) = max{3, 2, 3, 1, 2} = 3

exc(5) = max{2, 1, 2, 1, 1} = 2

exc(6) = max{3, 2, 3, 2, 1} = 3

raio(G) = min{exc(1), exc(2), exc(3), exc(4), exc(5), exc(6)} = 2

diâmetro(G) = max{exc(1), exc(2), exc(3), exc(4), exc(5), exc(6)} = 3

centro(G) = {2, 5}

## Componentes conexas
Para adequar o grafo ao formato de entrada exigido pelo algoritmo (uma lista de adjacência com vértices indexados de 0 a n−1), realizou-se a conversão da indexação original, subtraindo-se 1 de cada índice de vértice e de seus respectivos vizinhos. A estrutura de adjacências foi integralmente preservada, alterando-se apenas a numeração.

```
0: [1]
1: [0, 2, 4]
2: [1]
3: [4]
4: [3, 5, 1]
5: [4]
```

## Complexidade

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

