from queue import PriorityQueue
from collections import defaultdict

def make_code(queue):
    code = defaultdict(str)
    while queue.qsize()>1:
        left, right = queue.get(), queue.get()
        for letter in left[1]:
            code[letter] = '0' + code[letter]
        for letter in right[1]:
            code[letter] = '1' + code[letter]
        queue.put((left[0] + right[0], left[1] + right[1]))
    
    return code

s = input()

freq = defaultdict(int)
freq_q = PriorityQueue()
count=0

for char in s:
    freq[char]+=1

if len(freq)==1:
    print(len(freq), len(s), sep = ' ')
    for key in freq.keys():
        print(key, '0', sep=': ', end='\n')
    for ch in s:
        print('0', sep='', end='')
else:
    for key, value in freq.items():
        freq_q.put((value, [key]))

    huffman_code = make_code(freq_q)
    for ch in s:
        count+=len(huffman_code[ch])
     
    print(len(freq), count, sep = ' ')
    for (char, code)  in huffman_code.items():
        print(char, code, sep=': ', end='\n')

    for ch in s:
        if ch in huffman_code.keys():
            print(huffman_code[ch], end='')
