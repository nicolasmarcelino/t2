# Marco 2
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
