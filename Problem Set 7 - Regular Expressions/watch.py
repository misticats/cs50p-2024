import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"<iframe.+https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+).+iframe>", s, re.MULTILINE):
        return f"https://youtu.be/{matches.group(1)}"

if __name__ == "__main__":
    main()
