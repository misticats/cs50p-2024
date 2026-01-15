import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] not in figlet.getFonts():
                sys.exit("Invalid usage")
            else:
                figlet.setFont(font=sys.argv[2])
        else:
             sys.exit("Invalid usage")

    elif len(sys.argv) == 1:
        figlet.setFont(font=random.choice(figlet.getFonts()))

    else:
        sys.exit("Invalid usage")

    usertext = input("Input: ")
    return figlet.renderText(usertext)

print(main())
