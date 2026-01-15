def convert(givenstring):
    return givenstring.replace(":)", "\U0001F642").replace(":(","\U0001F641")


def main():
    user_input = input("Please give me a string: \n")
    print(convert(user_input))

main()
