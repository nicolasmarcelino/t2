# T2
Repositório do T2 registrando o problema, os marcos e a solução.

# Problema
UVA 315 Network (Problema C)

_Resumo: dado uma rede telefônica, retorne a quantidade de locais críticos para manter a conectividade da rede._

# Participantes
_Grupo D:_
- Nicolas Marcelino da Mota
- Gabriel Rocha da Cunha

# Modelagem
A solução é baseada no algoritmo de componentes conexas do _algs4_, onde o objetivo original do algoritmo é mapear as componentes conexas de um grafo. Aqui, o modelo foi adaptado para identificar os vértices de articulação por meio da remoção lógica do vértice durante a execução do algoritmo.

# Referências
A solução foi desenvolvida a partir das adaptações em Python do código do livro *Algorithms* (SEDGEWICK; WAYNE, 4. ed.), disponibilizadas pelo Prof. Ricardo Carubbi no repositório [RPG/algs4-py](https://github.com/carubbi/RPG/tree/main/algs4-py).

# Nota de evidências
Devido à indisponibilidade de registro no site [Online Judge](https://onlinejudge.org/), não foi possível enviar a solução para avaliação. O documento que descreve o problema cita um limite de tamanho de entrada e de tempo de 3 segundos. Em `/dados/casos-de-teste.txt`, é possível encontrar como último caso de teste um grafo que respeita esse limite de entrada, e executar o algoritmo em `/src/main.py` para avaliar o tempo de execução.
