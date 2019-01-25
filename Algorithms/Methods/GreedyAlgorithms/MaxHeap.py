class MaxHeap(object):
    def __init__(self, numbers = None):
        self.heap = [0]
        self.size = 0   
        
    def rearrange(self):
        i = self.size
        while i//2 > 0:
            if self.heap[i] > self.heap[i//2]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2
            
    def add(self, number):
        assert type(number)==int
        self.heap += [number]
        self.size += 1
        self.rearrange()
    
    def extractMax(self):
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.drown(1)
        return max
    
    def drown(self, i):
        while (i * 2) <= self.size:
            if i * 2 + 1 > self.size:
                maxIndex = i * 2
            elif self.heap[i*2] > self.heap[i*2+1]:
                maxIndex = i * 2
            else:
                maxIndex = i * 2 + 1
            if self.heap[i] < self.heap[maxIndex]:
                self.heap[i], self.heap[maxIndex] = self.heap[maxIndex], self.heap[i]
            i = maxIndex
    
    def show(self):
        for i in range(1, self.size+1):
            print(self.heap[i], sep = ' ', end = ' ')

n = int(input())
heap = MaxHeap()
for i in range(n):
    str = input()
    if str.startswith("Insert"):
        number = int(str[7:])
        heap.add(number)
    elif str.startswith("Extract"):
        print(heap.extractMax())
    else: pass
