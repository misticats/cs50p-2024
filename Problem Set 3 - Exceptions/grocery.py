def grocery():
    buylist = {}
    while True:
        try:
            item = input("")
            if item in buylist:
                buylist[item] += 1
            else:
                buylist[item] = 1
        except EOFError:
            for key, value in sorted(buylist.items()):
                print(value, key.upper())
            break

grocery()

