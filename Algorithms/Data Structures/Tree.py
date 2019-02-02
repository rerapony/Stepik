class Tree:
    def __init__(self, root):
        self.root = data
        self.children = []
        self.height = 1

    def add_child(self, child):
        assert isinstance(child, Tree)
        if not self.children:
            self.height += child.height
        else: 
            pass
        self.children.append(child)
