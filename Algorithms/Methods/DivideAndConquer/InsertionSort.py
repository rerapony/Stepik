def insertion_sort(array):
    for i in range(2, n):
        j = i
        while j>0 and array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j-=1
    return array
    
n = int(input())
*array, = map(int, input().split())
    
insertion_sort(array)
