def main():
    userinput = input("X/Y: ")
    roundedfuel = convert(userinput)
    print(gauge(roundedfuel))


def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    x, y = fraction.split("/")

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError
    else:
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        else:
            res = round(x / y * 100)
            if res > 100:
                res = 100
            elif res < 0:
                res = 0
            return res


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
