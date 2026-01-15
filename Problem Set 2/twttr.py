def twitter():
    user_input = input("Input: ")
    output = ""
    for letter in user_input:
        print(letter.lower())
        low = letter.lower()
        if low == "a" or low == "e" or low == "i" or low == "o" or low == "u":
            continue
        else:
            output += letter

    print(output)

twitter()
