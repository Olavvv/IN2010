import math

class Heap:
    def __init__(self):
        self.heap = list()

    def bubbleDown(self, value):
        pass

    def bubbleUp(self, value):
        pass

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap)
        while (i > 0 and self.heap[i] < self.heap[self.parentOf(i)]):
            self.heap[i], self.heap[self.parentOf(i)] = self.heap[self.parentOf(i)], self.heap[i]
            i = self.parentOf(i)

    def remove(self):
        x = self.heap[0]
        self.heap[0] = self.heap.pop()
        i = 0
        while (self.rightOf(i) < (len(self.heap - 1))):
            j = self.leftOf(i) if self.heap[self.leftOf(i)] <= self.heap[self.rightOf(i)] else self.rightOf(i)
            if self.heap[j] > self.heap[i]:
                return x
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
        if (self.leftOf(i) < (len(self.heap) - 1)) and (self.heap[self.rightOf(i)] <= self.heap[i]):
            self.heap[i], self.heap[self.leftOf(i)] = self.heap[self.leftOf(i)], self.heap[i]
        return x

    def parentOf(i):
        return math.floor((i-1)/2)
    
    def leftOf(i):
        return (2*i)+1
    
    def rightOf(i):
        return (2*i)+2
    

def main():
  
    #Skriv noen tester her!
    # Sett for eksempel inn 10 verdier, og sjekk at verdien som hentes ut er det du forventer!
    pass

if __name__ == "__main__":
    main()