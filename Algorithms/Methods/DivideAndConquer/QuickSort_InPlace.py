def quicksort(array, l, r):
    if l >= r: return

    i, j = l, r
    pivot = array[random.randint(l, r)]

    while i <= j:
        while array[i] < pivot: i += 1
        while array[j] > pivot: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    quicksort(array, l, j)
    quicksort(array, i, r)
