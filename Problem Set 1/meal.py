def main():
    input_time = input("What time do we have?: \n")
    converted_time = convert(input_time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    hours, mins = time.split(":")
    if mins != 0:
        converted_mins = int(mins) / 60
    var = float(hours) + float(converted_mins)

    return var


if __name__ == "__main__":
    main()
