"""
По данному числу 1≤n≤109 найдите максимальное число k, 
для которого n можно представить как сумму k различных натуральных слагаемых. 
Выведите в первой строке число k, во второй — k слагаемых.
"""


number = int(input())
used = []
i=1

while number>0:
    if (number - i)>i or (number-i)==0:
        used.append(i)
        number-=i
        i+=1
    else:
        i+=1
        
print(len(used))
print(*used)
