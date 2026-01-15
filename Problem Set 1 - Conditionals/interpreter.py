def interpreter():
    x, y, z = input("Arithmetic expression: \n").split(" ")

    if y == "+":
        return float(x) + float(z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    else:
        return float(x) / float(z)

print(interpreter())
