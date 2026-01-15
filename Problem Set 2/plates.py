def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    check1 = two_letters(s)
    check2 = max_min(s)
    check3 = number_check(s)
    check4 = specials(s)

    if all([check1, check2, check3, check4]):
        return True
    else:
        return False

def two_letters(string):
    counter = 0
    for i in range(1):
        if string[i].isalpha() == False:
            return False

    return True

def max_min(string):
    if len(string) > 6 or len(string) < 2:
        return False
    else:
        return True

def number_check(string):
    number_started = False

    for letter in string:
        if letter.isdigit():
            if letter == '0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False

    return True

def specials(string):
    for letter in string:
        if letter.isalpha() or letter.isdigit():
            continue
        else:
            return False

    return True

main()
