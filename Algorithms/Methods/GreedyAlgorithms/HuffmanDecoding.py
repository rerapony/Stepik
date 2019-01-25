from collections import defaultdict
code = defaultdict(str)

n, N = map(int, input().split())
for i in range(n):
    key, value = input().split(': ')
    code[key] = value
    
encoded = input()
while len(encoded)>0:
    for ch in code:
        if encoded.startswith(code[ch]):
            print(ch, end = '')
            encoded = encoded[len(code[ch]):]
        else:
            pass
