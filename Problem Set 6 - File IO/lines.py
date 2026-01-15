import sys


def main():
    filepath = check_arg()
    check_file((filepath))
    print(check_lines(filepath))


def check_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    else:
        return sys.argv[1]


def check_file(filepath):
    try:
        with open(filepath) as file:
            exit
    except FileNotFoundError:
         sys.exit("File does not exist")


def check_lines(filepath):
    codelines = 0
    with open(filepath) as file:
        for line in file:
            if not line.lstrip().startswith("#") and not line.strip() == "":
                codelines += 1
    return codelines


if __name__ == "__main__":
    main()
