import sys
phone_book = [None]*(10**7)
n = int(sys.stdin.readline())
for i in range(n):
    request = sys.stdin.readline().split()
    #print(request)
    if request[0] == 'add':
        phone_book[int(request[1])] = request[2]
    elif request[0] == 'find':
        answer = phone_book[int(request[1])] 
        if answer!=None:
            print(answer)
        else: print('not found')
    elif request[0] == 'del':
        phone_book[int(request[1])] = None
    #print(phone_book)
