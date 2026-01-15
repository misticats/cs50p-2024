import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
    if not matches:
        raise ValueError

    start_hour, start_minute, start_time, end_hour, end_minute, end_time = matches.groups()
    start_hour = int(start_hour)
    end_hour = int(end_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_minute = int(end_minute) if end_minute else 0

    if not 1 <= start_hour <= 12 or not 1 <= end_hour <= 12:
        raise ValueError("Invalid hour")
    if not 0 <= start_minute < 60 or not 0 <= end_minute < 60:
        raise ValueError("Invalid minute")

    if start_time == "PM" and start_hour != 12:
        start_hour += 12
    elif start_time == "AM" and start_hour == 12:
        start_hour = 0
    if end_time == "PM" and end_hour != 12:
        end_hour += 12
    elif end_time == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"


if __name__ == "__main__":
    main()
