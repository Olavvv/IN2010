def Tree(H, direction):
    root = 0
    for i in range(0, H + 1):
        root += 2**i
    calc = root

    for dir in direction:
        if dir == "L":
            calc






