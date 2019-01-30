class TreeDepth(object):
    def __init__(self, parents):
        self._parents = parents
        self._n = len(parents)
        self._max_depth = None
        self._depths = [None] * self._n

    def max_depth(self):
        if self._max_depth==None:
            for idx, parent in enumerate(self._parents):
                depth = self.get_depth(idx)
                if self._max_depth==None:
                    self._max_depth = depth
                elif self._max_depth < depth:
                    self._max_depth = depth
        return self._max_depth

    def get_depth(self, idx):
        depth = self._depths[idx]
        if depth!=None:
            return depth
        parent = self._parents[idx]
        if parent == -1:
            depth = 1
        else:
            depth = self.get_depth(parent) + 1
        self._depths[idx] = depth
        return depth
    
n = int(input())
parents = list(map(int, input().split()))
print(TreeDepth(parents).max_depth())
