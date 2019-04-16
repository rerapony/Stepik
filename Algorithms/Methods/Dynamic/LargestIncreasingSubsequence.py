import sys 

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [1]*N
for i in range(len(A)):
    for j in range(i):
        if A[i]%A[j]==0 and D[j]+1>D[i]:
            D[i] += 1

ans = 0
for num in D:
    ans = max(ans, num)
print(ans)
