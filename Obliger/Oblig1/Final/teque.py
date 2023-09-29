import math

# Definerer klassen Teque, som blir implementert i Array form.
class Teque:
    def __init__(self):
        self.teque = []
    
    # Setter inn element bakerst i Tequen.
    def push_back(self, x):
        self.teque.append(x)

    # Setter inn element 'x' foran i Tequen.
    def push_front(self, x):
        self.teque.insert(0,x)
    
    # Setter inn element 'x' i midten av Tequen.
    def push_middle(self, x):
        middle = math.floor( (len(self.teque) + 1)/2 )
        print(middle)
        self.teque.insert(middle,x)

    # Printer ut elementet paa index 'i'.
    def get(self, i):
        print(self.teque[i])


# Leser input slik input blir gitt.
teque = Teque()
nInst = int(input())
for i in range(nInst):
    inst = input().split()

    if (inst[0] == "push_back"):
        teque.push_back(int(inst[1]))

    elif (inst[0] == "push_front"):
        teque.push_front(int(inst[1]))

    elif (inst[0] == "push_middle"):
        teque.push_middle(int(inst[1]))

    elif (inst[0] == "get"):
        teque.get(int(inst[1]))

