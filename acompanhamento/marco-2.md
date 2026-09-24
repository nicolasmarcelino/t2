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
Para adequar o grafo ao formato de entrada exigido pelo algoritmo (uma lista de adjacência com vértices indexados de 0 a n-1), realizou-se a conversão da indexação original, subtraindo-se 1 de cada índice de vértice e de seus respectivos vizinhos. A estrutura de adjacências foi integralmente preservada, alterando-se apenas a numeração.

A seguir, rastreamento do algoritmo de componentes conexas aplicado ao grafo descrito pela lista de adjacência apresentada. O objetivo do algoritmo é identificar as componentes conexas de um grafo e relacionar cada vértice a sua componente.

Seguindo cc.py, uma adaptação em Python de CC.java do *algs4*, o algoritmo itera sobre todos os vértices, executa uma DFS no primeiro não visitado.

*marked* é o vetor que marca quais vértices já foram visitados. *id* associa cada vértice ao identificador da sua componente. *_size* marca a contagem de vértices de cada componente conexa. *count* marca a contagem de componentes conexas.

```
0: [1]
1: [0, 2, 4]
2: [1]
3: [4]
4: [3, 5, 1]
5: [4]
```

## s = 0

### v = 0
dfs(G, 0)

```
marked = [True, False, False, False, False, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [1, 0, 0, 0, 0, 0]
count  = 0
```

w = 1
dfs(G, 1)

```
marked = [True, True, False, False, False, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [2, 0, 0, 0, 0, 0]
count  = 0
```

w = 0 (já visitado)
w = 2
dfs(G, 2)

```
marked = [True, True, True, False, False, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [3, 0, 0, 0, 0, 0]
count  = 0
```

w = 1 (já visitado)
Volta para dfs(G, 1)

w = 4
dfs(G, 4)

```
marked = [True, True, True, False, True, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [4, 0, 0, 0, 0, 0]
count  = 0
```

w = 3
dfs(G, 3)

```
marked = [True, True, True, True, True, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [5, 0, 0, 0, 0, 0]
count  = 0
```

w = 4 (já visitado)
Volta para dfs(G, 4)

w = 5
dfs(G, 5)

```
marked = [True, True, True, True, True, True]
id     = [0, 0, 0, 0, 0, 0]
_size  = [6, 0, 0, 0, 0, 0]
count  = 0
```

w = 4 (já visitado)

Volta para dfs(G, 4)

w = 1 (já visitado)

Volta para dfs(G, 1)

Volta dfs(G, 0)

``self.count += 1```

## s = v = 1 (já visitado)
## s = v = 2 (já visitado)
## s = v = 3 (já visitado)
## s = v = 4 (já visitado)
## s = v = 5 (já visitado)

Estado final:

```
marked = [True, True, True, True, True, True]
id     = [0, 0, 0, 0, 0, 0]
_size  = [6, 0, 0, 0, 0, 0]
count  = 1
```

## Complexidade

Seja V = 6 o número de vértices e E = 5 o número de arestas do grafo (a soma dos graus é 2E = 10, como se vê nas listas de adjacência).

### Tempo: O(V + E)

- O laço principal percorre os V vértices, e cada iteração tem custo constante quando o vértice já foi visitado.
- A DFS é chamada **exatamente uma vez por vértice**, pois um vértice só entra na recursão se ainda não foi visitado e é marcado logo na entrada.
- Dentro de cada chamada, a lista de adjacência do vértice é percorrida **uma única vez**. Somando todas as listas, o total de posições visitadas é a soma dos graus, que é 2E, pois cada aresta aparece nas listas dos dois extremos.
- Total: V + 2E = O(V + E). No grafo deste marco: 6 + 10 = 16 operações elementares.

Com matriz de adjacência, examinar os vizinhos de um vértice custaria O(V) mesmo para vértices de grau baixo, levando a O(V²). Como o grafo é esparso (E = 5, muito menor que V² = 36), a lista de adjacência é a escolha mais eficiente.

### Espaço: O(V + E)

- Listas de adjacência: O(V + E), com V cabeças de lista e 2E entradas (aqui, 6 e 10).
- Vetor de componentes (que também indica os vértices já visitados): O(V).
- Pilha de recursão: O(V) no pior caso, quando o grafo é um caminho e a DFS desce por todos os vértices. Neste grafo, a profundidade máxima é 4 (por exemplo, 0 → 1 → 4 → 3 na indexação de 0 a n−1).
- Total: O(V + E).

### Custo das consultas de conectividade

Depois do pré-processamento em O(V + E), que é a execução do algoritmo de componentes conexas, a pergunta "os vértices `u` e `v` estão ligados?" se resume a comparar o identificador de componente de `u` com o de `v`.

- **Consulta em O(1)**, sem percorrer o grafo novamente. Como o grafo deste marco é conexo, todos os vértices recebem o mesmo identificador e qualquer par de vértices é considerado ligado.
- A quantidade de componentes conexas também é obtida em O(1), pois basta ler o contador mantido pelo algoritmo (aqui, 1).
- Sem o pré-processamento, cada consulta exigiria uma nova DFS, com custo O(V + E). Para Q consultas, o custo seria O(Q · (V + E)), contra O((V + E) + Q) com o vetor de componentes.
- Ressalva: o vetor de componentes vale para o grafo **estático**. Se arestas fossem inseridas ou removidas, ele precisaria ser recalculado (ou substituído por outra estrutura, como union-find).
- Total: O(V + E).

