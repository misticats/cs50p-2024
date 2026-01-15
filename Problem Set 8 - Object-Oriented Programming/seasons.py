from datetime import date, datetime
import sys
from inflect import engine


def main():
    print(get_date(input("Date of Birth: ")))


def get_date(user_input):
    try:
        birthday = datetime.strptime(user_input, "%Y-%m-%d").date()
        today = date.today()
        age_in_minutes = int((today - birthday).total_seconds() / 60)
        if age_in_minutes < 0:
            raise ValueError
        return age_to_words(age_in_minutes) + " minutes"
    except ValueError:
        sys.exit("Invalid date format")


def age_to_words(number):
    p = engine()
    return p.number_to_words(number).capitalize().replace("and ", "")


if __name__ == "__main__":
    main()
