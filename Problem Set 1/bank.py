def bank():
    greeting = input("Say your greetings: \n").lower().lstrip()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

bank()
