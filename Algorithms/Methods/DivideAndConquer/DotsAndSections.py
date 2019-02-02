from sys import stdin
import random
import bisect


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
    
n_sections, n_dots = map(int, stdin.readline().split())
begins = []
ends = []
for i in range(n_sections):
    fst, lst = map(int, stdin.readline().split())
    begins.append(fst)
    ends.append(lst)
dots = list(map(int, stdin.readline().split()))

quicksort(begins, 0, n_sections-1)
quicksort(ends, 0, n_sections-1)

for dot in dots:
    count1 = bisect.bisect_right(begins, dot)
    count2 = bisect.bisect_left(ends, dot)
    print(abs(count1-count2), end = ' ')
