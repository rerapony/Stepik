def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = random.choice(array)
        left = []
        right = []
        equal = []
        for element in array:
            if element < pivot:
                left.append(n)
            elif element > pivot:
                right.append(n)
            else:
                equal.append(n)
        return quicksort(left) + equal + quicksort(right)
