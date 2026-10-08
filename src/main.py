from graph import Graph
from cc import CC
import time

start = time.time()

while True:
   total_v = int(input())

   if total_v == 0:
      break

   g = Graph(total_v)

   while True:
      conexoes = input().split()

      if conexoes[0] == "0":
         break

      for i in range(1, len(conexoes)):
         g.add_edge(int(conexoes[0]) - 1, int(conexoes[i]) - 1)

   criticos = 0

   for v in range(g.V):
      dfs_sem_v = CC(g, v)
      if dfs_sem_v.count > 1:
         criticos = criticos + 1

   print(criticos)

print(f"Terminou em {time.time() - start:.3f}s")