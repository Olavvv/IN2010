from binarySet import *

bSet = BinarySet()

def BST():
    N = input("Antall instruksjoner: \n")
    print(f"{N} - Instruksjoner: \n")
    for i in range(N):
        input = ()
        if (input == "size"):
            print(bSet.size())
        else:
            input.split()
            if (input[0] == "insert"):
                bSet.insert(int(input[1]))
            elif (input[0] == "contains"):
                bSet.contains(int(input[1]))


input = input("Teste mengde for AVL eller BST? BST/AVL")

if (input == "BST"):
    BST()
