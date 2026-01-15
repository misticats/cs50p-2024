def fuel():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            calc = 100 / int(y) * int(x)
            if int(x) > int(y):
                pass
            elif calc <= 1:
                return "E"
            elif calc >= 99:
                return "F"
            else:
                return f"{round(calc)}%"
        except ValueError:
            pass
        except  ZeroDivisionError:
            pass

print(fuel())
