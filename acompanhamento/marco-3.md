# Marco 3

Este marco identifica a propriedade estrutural central do Problema C (rede de cabos de telefone), explica o critério usado para reconhecê-la, rastreia manualmente a estratégia em uma instância pequena e estima a complexidade de tempo e memória.

## Propriedade estrutural central

A rede é um grafo conexo não direcionado, em que os locais são vértices e as linhas são arestas. Um local é **crítico** quando a falha da sua central deixa a rede desconexa. Em teoria dos grafos, isso é um **vértice de articulação** (ponto de corte, *cut vertex*): um vértice `v` tal que `G − v` tem mais componentes conexas do que `G`. Como `G` é conexo, basta verificar se `G − v` é desconexo.

A resposta exigida pelo problema é a **quantidade** de vértices de articulação de cada rede.

A lista de adjacência abaixo representa o grafo `G` utilizado no marco anterior e construído com base em um dos casos de teste disponibilizados pela plataforma.

```
0: [1]
1: [0, 2, 4]
2: [1]
3: [4]
4: [3, 5, 1]
5: [4]
```

| Implementação | Papel | Adaptação prevista |
|---|---|---|
| `graph.py` | Representação do grafo com listas de adjacência | Lista de `Bag()` para "lista de listas" |
| `CC.py` | DFS para componentes conexas | Adaptar para ignorar um vértice `r` |

O objetivo aqui é simular uma modificação do `cc.py`, uma adaptação em Python de CC.java do *algs4*, utilizada no marco anterior, para ignorar um dos vértices do grafo (que será chamado de vértice `r`) e verificar se o mesmo se divide em mais de uma componente conexa.

`CC` recebe `G` em seu construtor e itera sobre o primeiro vértice, executando uma DFS, recebendo como parâmetro o vértice `r`.

`dfs(G, 0, 4)`

```
marked = [True, False, False, False, False, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [1, 0, 0, 0, 0, 0]
count  = 0
```

`dfs(G, 1, 4)`

```
marked = [True, True, False, False, False, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [2, 0, 0, 0, 0, 0]
count  = 0
```

`dfs(G, 2, 4)`

```
marked = [True, True, True, False, False, False]
id     = [0, 0, 0, 0, 0, 0]
_size  = [3, 0, 0, 0, 0, 0]
count  = 0
```

Como o único `w` em `G.adj[2]` é `1` (já visitado), o algoritmo retorna para `dfs(G, 1, 4)` e encontra `w = 4`, ignorando o vizinho e finalizando `dfs(G, 1, 4)`. A chamada `dfs(G, 4, 4)`, portanto, deverá ser descartada também no _loop_ principal.

Finalizando `dfs(G, 1, 4)`, também é finalizada `dfs(G, 0, 4)` e o _loop_ principal avança para a chamada `dfs(G, 3, 4)` com `count = 1`.

`dfs(G, 3, 4)`
```
marked = [True, True, True, True, False, False]
id     = [0, 0, 0, 1, 0, 0]
_size  = [3, 1, 0, 0, 0, 0]
count  = 1
```

Como o único `w` em `G.adj[3]` é `4`, o algoritmo finaliza `dfs(G, 3, 4)` e, a partir do _loop_ principal, avança para a chamada `dfs(G, 5, 4)` com `count = 2`.

`dfs(G, 5, 4)`
```
marked = [True, True, True, True, False, False]
id     = [0, 0, 0, 1, 0, 2]
_size  = [3, 1, 1, 0, 0, 0]
count  = 2
```

Como o único `w` em `G.adj[5]` é `4`, o algortimo finaliza a chamada `dfs(G, 5, 4)` e termina sua execução com `count = 3`.

Como a contagem de componentes ao ignorar o vértice `r = 4` é maior que 1, ele é um vértice de articulação. O objetivo, então, é construir um algoritmo que execute o algoritmo de componentes tomando cada vértice do grafo como `r` e verificar quantos retornam `count > 1`.

## Critério de reconhecimento

### Critério direto (definição)

Para cada `v`, remove-se `v`, executa-se uma DFS a partir de qualquer outro vértice e verifica-se se todos os `V − 1` vértices restantes foram visitados. Se não, `v` é crítico. Essa é a solução proposta no Marco 1 e serve como referência de corretude. Custo: `V` DFS, ou seja, `O(V · (V + E))`.

## Complexidade

Sejam `V` o número de locais e `E` o número de linhas de uma rede.

### Tempo

- **Critério eficiente:** `O(V + E)` por rede. Cada vértice é visitado uma única vez pela DFS, e cada lista de adjacência é percorrida uma única vez. A soma dos graus é `2E`, e cada teste (`min`, comparação) é `O(1)`. A contagem final dos vértices críticos custa `O(V)`. Na instância principal: `V + 2E = 6 + 10 = 16` operações elementares de varredura.
- **Critério direto (remover cada vértice e rodar DFS):** `O(V · (V + E))`. Na instância principal, 6 DFS, cada uma sobre um grafo com no máximo 5 vértices.
- A leitura da entrada também é `O(V + E)` por rede. Como a rede é conexa, `E >= V − 1`, então `O(V + E) = O(E)`.

### Memória

Distinguindo a representação do grafo da memória auxiliar:

| Componente | Custo | Neste grafo |
|---|---|---|
| **Representação do grafo** (lista de adjacência): `V` cabeças de lista e `2E` entradas | `O(V + E)` | 6 listas, 10 entradas |
| **Memória auxiliar**: `marked`, `id` e `_size` (um valor por vértice) | `O(V)` | 3 vetores de 6 posições |
| **Memória auxiliar**: pilha de recursão da DFS | `O(V)` no pior caso (grafo em caminho) | profundidade máxima 4 (por exemplo, `0 → 1 → 4 → 3` com `r = 2`) |
| **Memória auxiliar**: `count`, `r` e o contador de vértices críticos | `O(1)` | 3 inteiros |

O grafo `G − r` não é construído: o vértice `r` é apenas ignorado pelo laço principal e pela DFS. Por isso, a representação continua sendo uma única lista de adjacência, sem cópia do grafo a cada remoção.

Os vetores `marked`, `id` e `_size` são reinicializados a cada novo valor de `r`, então a memória auxiliar não se acumula entre as `V` execuções do `CC`: em qualquer instante existe apenas um conjunto desses vetores.

Memória auxiliar total: `O(V)`. Memória total: `O(V + E)`, dominada pela representação do grafo. A repetição do `CC` para cada `r` aumenta o tempo (de `O(V + E)` para `O(V · (V + E))`), mas não a memória.

Uma matriz de adjacência custaria `O(V²)` de memória. Como a rede é esparsa, a lista de adjacência continua a melhor escolha.
_Referência: a descrição e a aplicação do algoritmo de componentes conexas apresentadas neste documento foram baseadas no material [A4_Conectividade.pdf](https://github.com/carubbi/RPG/blob/main/mat-didatico/aulas/A4_Conectividade.pdf) , do professor Ricardo Carubbi, que utiliza como referência o livro Algorithms, de Robert Sedgewick e Kevin Wayne._
