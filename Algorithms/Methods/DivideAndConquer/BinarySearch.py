def binary_search(array, element):
    up = len(array)-1
    down = 0
    while up>=down:
        mid = (up+down)//2
        if element==array[mid]:
            return (mid+1)
        elif element>array[mid]:
            down = mid+1
        else:
            up = mid-1
    return -1

input1, input2 = input().split(), input().split()
n, array1 = int(input1[0]), list(map(int, input1[1:]))
k, array2 = int(input2[0]), list(map(int, input2[1:]))
for element in array2:
    print(binary_search(array1, element), end = ' ')
