from sys import stdin
#W -  knapksack weight
#n - number of gold bars
#weights - weights of n gold bars
W, n = map(int, stdin.readline().split())
weights = list(map(int, stdin.readline().split()))

D = [[None for i in range(W+1)] for j in range(n+1)]
for wi in range(W+1):
    D[0][wi] = 0
for i in range(n+1):
    D[i][0] = 0
    
for i in range(1, n+1):
    for wi in range(1, W+1):
        D[i][wi] = D[i-1][wi]
        if weights[i-1]<=wi:
            D[i][wi] = max(D[i][wi], D[i-1][wi-weights[i-1]]+weights[i-1])
print(D[n][W])
