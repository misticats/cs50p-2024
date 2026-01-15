import validators


def main():
    usermail = input("What's your email address? ")
    if validators.email(usermail) == True:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
