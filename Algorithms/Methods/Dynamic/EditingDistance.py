import sys 
import numpy as np

def diff(char_a, char_b):
    if char_a==char_b:
        return 0
    else: return 1

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
n = len(first)
m = len(second)
D = np.empty([n+1, m+1])

for i in range(n+1):
    D[i, 0] = i
for j in range(m+1):
    D[0, j] = j
for i in range(n):
    for j in range(m):
        c = diff(first[i], second[j])
        D[i+1, j+1] = min(D[i, j+1]+1, D[i+1, j]+1, D[i, j]+c)
print(int(D[n,m]))
