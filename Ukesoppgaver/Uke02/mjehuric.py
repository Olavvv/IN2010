userInput = input().split(" ")
values = []

for value in userInput:
    values.append(int(value))

while (values != sorted(values)):
    if values[0] > values[1]:
        values[0], values[1] = values[1], values[0]
        print(f"{values[0]} {values[1]} {values[2]} {values[3]} {values[4]}")
    
    if values[1] > values[2]:
        values[1], values[2] = values[2], values[1]
        print(f"{values[0]} {values[1]} {values[2]} {values[3]} {values[4]}")

    if values[2] > values[3]:
        values[2], values[3] = values[3], values[2]
        print(f"{values[0]} {values[1]} {values[2]} {values[3]} {values[4]}")

    if values[3] > values[4]:
        values[3], values[4] = values[4], values[3]
        print(f"{values[0]} {values[1]} {values[2]} {values[3]} {values[4]}")
    