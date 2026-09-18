# Problema C
Cenário: uma rede de cabos de telefone.

# Descrição
Elas conectam locais enumerados de 1 a _n_.
Dois locais não tem o mesmo número.
As linhas são bidirecionais e sempre conectam dois locais.
As linhas terminam em uma central em cada local.
Em situações estáveis, é possível contatar qualquer local a partir do outro, mesmo que a conexão não seja direta.
Por isso, quando a energia falha em um dos locais, a central daquele local para de funcionar e a conexão para alguns locais é cortada.
O local onde a energia falhou é considerado crítico.
Objetivo: encontrar estes locais críticos e retornar quantos existem.

# Modelagem
Pela descrição do problema, podemos considerar a rede telefônica como um **grafo conexo**, pois é possível entrar em contato com qualquer local a partir de outro. No entanto, há locais críticos em que a falha na central associada a ele compromete essa propriedade. O objetivo é contar quantos locais (vértices) são essenciais para manter a conectividade do grafo.

**Solução proposta**: remover cada um dos vértices e executar o algoritmo de DFS (busca em profundidade) em cada cenário do grafo modificado para verificar se o mesmo continua conexo.

# Entradas e saídas

**Significado das entradas**: quantos locais existem e quais são suas conexões.

**Significado da saída**: quantos locais críticos em cada uma das redes.

Cada entrada é um bloco de uma ou mais redes telefônicas, cada uma sendo indicada por um número inteiro que indica o número total de nós da rede. As próximas linhas descrevem as conexões das redes, indicando primeiro o nó e seus vizinhos diretos. A descrição de cada rede termina com 0 e a do bloco de entrada completo termina com 0.

## Exemplo de entrada
```
5
5 1 2 3 4
0
6
2 1 3
5 4 6 2
0
0
```

## Exemplo de saída
```
1
2
```

Fonte: https://onlinejudge.org/external/3/315.pdf
