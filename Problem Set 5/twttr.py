def main():
    userinput = input("Input: ").lower()
    print(shorten(userinput))


def shorten(word):
    res = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter.lower() not in vowels:
            res += letter
    return res


if __name__ == "__main__":
    main()
