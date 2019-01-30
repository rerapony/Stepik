
n = int(input())
s = list(map(int, input().split()))
n = len(s)

d={}
def up(v):
    next=s[v]
    if next==-1:
        return 1
    if v not in d:
        d[v]=up(next)+1
    return d[v]


mx = 0
for i in range(n):
    mx = max(mx, up(i))
print(mx)
