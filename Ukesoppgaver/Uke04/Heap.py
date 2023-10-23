import math

class Heap:
    def __init__(self):
        self.heap = list()


    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while (0 < i and self.heap[i] < self.heap[self.parentOf(i)]):
            self.heap[i], self.heap[self.parentOf(i)] = self.heap[self.parentOf(i)], self.heap[i]
            i = self.parentOf(i)

    def remove(self):
        x = self.heap[0]
        self.heap[0] = self.heap.pop()
        i = 0
        while (self.rightOf(i) < (len(self.heap) - 1)):
            j = self.leftOf(i) if self.heap[self.leftOf(i)] <= self.heap[self.rightOf(i)] else self.rightOf(i)
            if self.heap[j] > self.heap[i]:
                return x
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
        if (self.leftOf(i) < (len(self.heap) - 1)) and (self.heap[self.rightOf(i)] <= self.heap[i]):
            self.heap[i], self.heap[self.leftOf(i)] = self.heap[self.leftOf(i)], self.heap[i]
        return x

    def parentOf(self, i):
        return math.floor((i-1)/2)
    
    def leftOf(self, i):
        return (2*i)+1
    
    def rightOf(self,i):
        return (2*i)+2
    

def main():
    heap = Heap()

    heap.insert(5)
    heap.insert(1)
    heap.insert(6)
    heap.insert(3)
    heap.insert(20)
    heap.insert(15)
    heap.insert(60)
    heap.insert(4)
    heap.insert(11)
    heap.insert(22)


    for i in range(len(heap.heap) - 1):
        print(heap.remove())

if __name__ == "__main__":
    main()