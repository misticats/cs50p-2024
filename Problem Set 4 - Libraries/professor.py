import random


def main():
    level = get_level()

    correct = 0
    for tasks in range(10):
        # Get Task
        xvalue, yvalue, = generate_integer(level)
        solution = xvalue + yvalue

        for tries in range(3):
            try:
                solve = int(input(f"{xvalue} + {yvalue} = "))
                if solve == solution:
                    correct += 1
                    break
                else:
                    if tries < 2:
                        print("EEE")
            except ValueError:
                print("EEE")
        if solve != solution:
            print(f"{xvalue} + {yvalue} = {solution}")

    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        xvalue = random.randint(0, 9)
        yvalue = random.randint(0, 9)
    elif level == 2:
        xvalue = random.randint(10, 99)
        yvalue = random.randint(10, 99)
    elif level == 3:
        xvalue = random.randint(100, 999)
        yvalue = random.randint(100, 999)
    else:
        raise ValueError

    return xvalue, yvalue

if __name__ == "__main__":
    main()
