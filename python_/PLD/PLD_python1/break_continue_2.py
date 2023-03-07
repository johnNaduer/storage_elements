for i in range(10):
    for j in range(10):
        if i == 5 or j == 5:
            break
        if i == j:
            continue
        print("({}, {})".format(i, j), end = " ")
    print()
