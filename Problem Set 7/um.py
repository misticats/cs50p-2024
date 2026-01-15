import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # re.findall = all occurences -> saves to a list[]
    matches = re.findall(r"(\bum\b)", s.strip(), re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
