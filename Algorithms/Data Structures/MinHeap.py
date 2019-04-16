import sys

class MinHeap(object):
    def __init__(self, array):
        self.size = len(array)
        self.array = array
        self.swaps = []
        self.n_swaps = 0
        for i in range((self.size//2)-1, 0-1, -1):
            #print(i)
            self.sift_down(i)
    
    def sift_down(self, i):
            minIndex = i
            l = i*2+1
            r = i*2+2
            if l < self.size and self.array[l] < self.array[minIndex]:
                minIndex = l
            if r < self.size and self.array[r] < self.array[minIndex]:
                minIndex = r
            if i != minIndex:
                #print(i, minIndex)
                self.swaps.append((i, minIndex))
                self.n_swaps += 1
                self.array[i], self.array[minIndex] = self.array[minIndex], self.array[i]
                self.sift_down(minIndex)

sys.stdin.readline()
a = MinHeap(list(map(int, sys.stdin.readline().split())))
#print(a)
print(a.n_swaps)
for j in range(a.n_swaps):
    print(a.swaps[j][0], a.swaps[j][1], sep=' ')
