import sys
 
# put your python code here
def ceilIndex(Arr, Indeces, left, right, key):
    while (left <= right):
        m = (left+right)//2
        if (Arr[Indeces[m]] >= key):
            left = m + 1
        else:
            right = m - 1
    return left
 
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = [0]*(N+1)
P = [-1]*(N)
 
l = 0
for i in range(0, N):
    k = ceilIndex(A, D, 1, l, A[i])
    #print(k)
    D[k] = i
    if k>0:
        P[i] = D[k-1]
    if k>l:
        l = k
       
new_A = [None]*l  
s = D[l]
for j in range(l-1, -1, -1):
    new_A[j] = s+1
    s = P[s]
#print(P)
#print(D)
print(l)
for a in new_A:
    print(a, end = ' ')
