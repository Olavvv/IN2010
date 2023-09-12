values = input().split(" ")

def sortWood(values):
    sorted = False
    while (sorted(values)):
        for i in range(len(values) - 1):
            if int(values[i]) > int(values[i+1]):
                print(values)

sortWood(values)