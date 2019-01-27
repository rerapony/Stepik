def check(expression):
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []
    queue_count = []
    
    for i in range(len(expression)):
        letter = expression[i]
        if letter in opening:
            queue.append(mapping[letter])
            queue_count.append(i+1)
        elif letter in closing:
            if not queue or letter != queue.pop():
                return i+1
            else: queue_count.pop()
            
    if not queue_count:
        return 'Success'
    else:
        return queue_count[0]
    
    
exp = input()
print(check(exp))
