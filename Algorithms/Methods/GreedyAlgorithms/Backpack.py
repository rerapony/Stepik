"""
Первая строка содержит количество предметов 1≤n≤103 и вместимость рюкзака 0≤W≤2⋅106. 
Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅106 и объём 0<wi≤2⋅106 предмета (n, W, ci, wi — целые числа). 
Выведите максимальную стоимость частей предметов 
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), 
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
"""


n, max_size = map(int, input().split())
cost_size = []
for i in range(n):
    cost, size = map(int, input().split())
    cost_size.append([cost, size, cost/size])
    
cost_size.sort(key = lambda x: x[2], reverse=True)

put = 0
sum_cost = 0


for i in range(n):
    item_cost, item_size = cost_size[i][0], cost_size[i][1]
    size_free = max_size - put
    if size_free >= 0:
        if item_size<=size_free:
            put+=item_size
            sum_cost+=item_cost
        else:
            put+=size_free
            sum_cost+=((size_free/item_size)*item_cost)

print('{:.3f}'.format(sum_cost))
