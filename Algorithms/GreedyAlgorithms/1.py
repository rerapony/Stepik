S = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    S.append([x, y])


S.sort(key = lambda x: x[1])  

answer = []
point = S[0][1]
answer.append(point)
i=1
while i<n:
    if S[i][0] <= point <= S[i][1]:
        i+=1
    else:
        point = S[i][1]
        answer.append(point)
        i+=1

print(len(answer))
print(*answer)
    
