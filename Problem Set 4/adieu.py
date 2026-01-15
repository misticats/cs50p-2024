import sys

def main():
    namelist = []
    while True:
        try:
            namelist.append(input("Name: "))
        except EOFError:
            break
    print(adieu(namelist))

def adieu(list):
    startstring = "Adieu, adieu, to "
    if len(list) > 2:
        list_seperated = ", ".join(list[:-1])
        return startstring + list_seperated + ", and " + list[-1]

    elif len(list) == 2:
        return startstring + list[0] + " and " + list[1]

    elif len(list) == 1:
        return startstring + list[0]

main()
