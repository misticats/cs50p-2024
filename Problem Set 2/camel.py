def camel():
    res = ""
    user_input = input("camelCase: ")
    for letter in user_input:
        if letter.isupper():
            res += "_"
        res += letter.lower()

    print(res)


camel()
