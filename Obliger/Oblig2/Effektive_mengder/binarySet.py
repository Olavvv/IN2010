class BinarySet:

    class Node:
        def __init__(self, _element):
            self.element = _element
            self.left = None
            self.right = None
    
    def __init__(self):
        self._size = 0
        self._root = None

    def search(self, v, x):
        if (v == None):
            return False
        if (v.element == x):
            return True
        if (x < v.element):
            return self.search(v.left, x)
        if (x > v.element):
            return self.search(v.right, x)
    
    def contains(self, x):
        return self.search()

    def insert(self, v, x):
        if (self._root == None):
            v = self.Node(x)
            self._root = v
            return v
        
        if (v == None):
            v = self.Node(x)
            self.size += 1
        elif (x < v.element):
            v.left = self.insert(v.left, x)
        elif (x > v.element):
            v.right = self.insert(v.right, x)
        return v
    
    def find_min(self, v):
        if (v == None):
            return None
        
        if (v.left == None):
            return v
        else:
            self.find_min(v.left)
    
    def remove(self, v, x):
        if (v == None):
            return None
        if (x < v.element):
            v.left = self.remove(v.left, x)
        if (x > v.element):
            v.right = self.remove(v.right, x) 
        if (v.left == None):
            return v.right
        if (v.right == None):
            return v.left
        
        u = self.find_min(v.right)
        v.element = u.element
        v.right = self.remove(v.right, u.element)
        self.size -= 1
        return v
    
    def size(self):
        return self._size
        