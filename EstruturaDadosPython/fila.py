

from collections import deque


fila = deque()

fila.append('Daniel')
fila.append('Harry Potter')
fila.append('Rony')

print(f"antes de remover: {fila}")
rm = fila.popleft()                        # remove sempre o da esquerda como uma fila (first in, first out)
print(f"depois de remover: {fila}")
print(f"quem foi removido ? {rm}")

 