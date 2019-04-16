import sys

class Processor(object):
    
    def __init__(self, n_proc = 0):
        self.size = n_proc
        self.array = []
        for i in range(n_proc):
            self.array.append([i, 0])
        
    def sift_up(self, i):
        if i>0 and self.array[(i-1)//2][1]>=self.array[i][1]:
            if self.array[(i-1)//2][1]>self.array[i][1]:
                self.array[(i-1)//2], self.array[i] = self.array[i], self.array[(i-1)//2]
            elif self.array[(i-1)//2][0]>self.array[i][0]:
                self.array[(i-1)//2], self.array[i] = self.array[i], self.array[(i-1)//2]
            i = (i-1)//2
            self.sift_up(i)
    
    def sift_down(self, i):
            minIndex = i
            l = i*2+1
            r = i*2+2
            if l < self.size and self.array[l][1] <= self.array[minIndex][1]:
                if self.array[l][1] < self.array[minIndex][1]:
                    minIndex = l
                elif self.array[l][0] < self.array[minIndex][0]:
                    minIndex = l
            if r < self.size and self.array[r][1] <= self.array[minIndex][1]:
                if self.array[r][1] < self.array[minIndex][1]:
                    minIndex = r
                elif self.array[r][0] < self.array[minIndex][0]:
                    minIndex = r
            if i != minIndex:
                self.array[i], self.array[minIndex] = self.array[minIndex], self.array[i]
                self.sift_down(minIndex)
    
    def print_max(self):
        if self.size>0:
            result = self.array[0]
            print(result[0], result[1])
        else: 
            print("ERROR: empty proccesor")
    
    def change_time(self, i, time):
        old_time = self.array[i][1]
        self.array[i][1] += time
        if self.array[i][1] >= old_time:
            self.sift_down(i)
        else:
            self.sift_up(i)
            
n_proc, m_packages = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))
proc = Processor(n_proc)
for i in range(m_packages):
    proc.print_max()
    proc.change_time(0, times[i])
    
