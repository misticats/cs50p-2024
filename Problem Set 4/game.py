import random
import sys

def main():
    while True:
        try:
            maxlevel = int(input("Maximum Level: "))
        except ValueError:
            pass
        else:
            if 0 < maxlevel < 100:
                break

    randomnr = random.randint(1, maxlevel)
    print(guess(randomnr))
    sys.exit()

def guess(level):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < level:
                print("Too small!")
            elif guess > level:
                print("Too large!")

        except ValueError:
            pass

        else:
            if guess == level:
                return "Just right!"
main()
