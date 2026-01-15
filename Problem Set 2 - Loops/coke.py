def coke():
    cost = 50
    while True:
        paid = input("Insert Coin: ")
        if paid == "50" or paid == "25" or paid == "10" or paid == "5":
            cost = (cost - int(paid))
            if cost <= 0:
                print(f"Change Owed: {str(cost).lstrip("-")}")
                break
        print(f"Amount Due: {cost}")

coke()
