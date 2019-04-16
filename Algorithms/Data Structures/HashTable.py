import sys
def hashing(word):
    global m
    sum = 0
    x = 263
    p = 1000000007
    for i in range(len(word)):
        sum += ord(word[i])*(x**i)
    return (sum%p)%m

def add(hash_table, word):
    key = hashing(word)
    if search_word(hash_table, key, word)=='yes':
        pass
    else:
        hash_table[key].append(word)
    
def search_word(hash_table, key, word):
    search_table = hash_table[key]
    if len(search_table)>0:
        for k, v in enumerate(search_table):
            if v == word:
                return 'yes'
    return 'no'
        
def search_index(hash_table, key, word):
    search_table = hash_table[key]
    if len(search_table)>0:
        for k, v in enumerate(search_table):
            if v == word:   
                return k
    return None

def delete(hash_table, word):
    key = hashing(word)
    ix = search_index(hash_table, key, word)
    if ix == None:
        pass
    else:
        del hash_table[key][ix]
    
def check(hash_table, key):
    search_table = hash_table[key]
    if len(search_table)>0:
        for i in range(len(search_table)-1, -1, -1):
            print(search_table[i], end = ' ')
    else:
        print('')
    print()
        
m = int(sys.stdin.readline())
n = int(sys.stdin.readline()) 
hash_table = [[] for _ in range(m+1)]
for i in range(n):
    request = sys.stdin.readline().split()
    #print(request)
    if request[0] == 'add':
        add(hash_table, request[1])
    elif request[0] == 'check':
        key = int(request[1])
        check(hash_table, key)
    elif request[0] == 'del':
        delete(hash_table, request[1])
    elif request[0] == 'find':
        key = hashing(request[1])
        print(search_word(hash_table, key, request[1]))
    #print(hash_table)
