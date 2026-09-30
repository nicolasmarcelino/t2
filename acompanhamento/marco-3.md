# Marco 3

Este marco identifica a propriedade estrutural central do Problema C (rede de cabos de telefone), explica o critério usado para reconhecê-la, rastreia manualmente a estratégia em uma instância pequena e estima a complexidade de tempo e memória.

## Propriedade estrutural central

A rede é um grafo conexo não direcionado, em que os locais são vértices e as linhas são arestas. Um local é **crítico** quando a falha da sua central deixa a rede desconexa. Em teoria dos grafos, isso é um **vértice de articulação** (ponto de corte, *cut vertex*): um vértice `v` tal que `G − v` tem mais componentes conexas do que `G`. Como `G` é conexo, basta verificar se `G − v` é desconexo.

A resposta exigida pelo problema é a **quantidade** de vértices de articulação de cada rede.

Uma propriedade relacionada é a de **bloco** (componente biconexa): um subgrafo maximal sem vértice de articulação. Os vértices de articulação são exatamente os vértices que pertencem a mais de um bloco. Uma rede sem locais críticos tem um único bloco e responde 0.

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

| Componente | Custo | Na instância principal |
|---|---|---|
| **Representação do grafo** (lista de adjacência): `V` cabeças de lista e `2E` entradas | `O(V + E)` | 6 listas, 10 entradas |
| **Memória auxiliar**: `marked`, `pre`, `low`, `art` (um valor por vértice) | `O(V)` | 4 vetores de 6 posições |
| **Memória auxiliar**: pilha de recursão da DFS | `O(V)` no pior caso (grafo em caminho) | profundidade máxima 4 (`0 → 1 → 4 → 3`) |
| **Memória auxiliar**: contador de tempo, contador de filhos e resposta | `O(1)` | 3 inteiros |

Memória auxiliar total: `O(V)`. Memória total: `O(V + E)`, dominada pela representação do grafo. A versão direta usa a mesma memória auxiliar, pois reaproveita o vetor de visitados a cada remoção. A vantagem da versão com *low-link* é apenas de tempo.

Uma matriz de adjacência custaria `O(V²)` de memória e faria a DFS gastar `O(V)` por vértice, levando o tempo a `O(V²)`. A lista de adjacência continua a melhor escolha para redes esparsas.

