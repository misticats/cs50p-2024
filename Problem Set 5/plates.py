def main():
    plate = input("Plate: ")
    res = is_valid(plate)
    if res:
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check if length is between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Check for number sequence and leading zeros
    number_started = False
    for letter in s:
        if letter.isdigit():
            if letter == '0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False

    # Check for special characters
    if not all(char.isalnum() for char in s):
        return False

    return True

if __name__ == "__main__":
    main()
