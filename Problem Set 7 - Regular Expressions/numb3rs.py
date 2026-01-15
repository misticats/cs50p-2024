import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        return all(int(matches.group(groupmatch)) <= 255 for groupmatch in range(1, 5))
    else:
        return False


if __name__ == "__main__":
    main()
