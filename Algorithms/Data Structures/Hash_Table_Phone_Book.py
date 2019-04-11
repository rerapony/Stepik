import sys

def hashing(key):
    #print(int(key[0]))
    return int(key[0])

def add(hash_table, key, value):
    answer = search_index(hash_table, key)
    new_key = hashing(key)
    if answer == None:
        hash_table[new_key].append((key, value))
    else:
        hash_table[new_key][answer] = (key, value)
        
def search_index(hash_table, key):
    search_table = hash_table[hashing(key)]
    for i, kv in enumerate(search_table):
        k, v = kv
        if key == k:
            return i
    return None

def search_name(hash_table, key):
    search_table = hash_table[hashing(key)]
    for i, kv in enumerate(search_table):
        k, v = kv
        if key == k:
            return v
    return 'not found'

def delete(hash_table, key):
    search_table = hash_table[hashing(key)]
    for i, kv in enumerate(search_table):
        k, v = kv
        if key == k:
            del search_table[i]


n = int(sys.stdin.readline())
phone_book = [[] for _ in range(10)]
#print(phone_book)
for i in range(n):
    request = sys.stdin.readline().split()
    #print(request)
    if request[0] == 'add':
        add(phone_book, request[1], request[2])
    elif request[0] == 'find':
        answer = search_name(phone_book, request[1])
        print(answer)
    elif request[0] == 'del':
        delete(phone_book, request[1])
    #print(phone_book)
