months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def outdated():
    while True:
        try:
            userinput =  input("Date in month-day-year e.g. 9/8/1636: \n")
            if "/" in userinput:
                month, day, year = userinput.strip().split("/")
                day = int(day)
                month = int(month)
                if month >= 12:
                    raise ValueError

            elif "," in userinput:
                month, day, year = userinput.split(" ")
                day = int(day.rstrip(","))
                month = months.index(month)
                month += 1

            else:
                raise ValueError

            if day >= 31:
                raise ValueError

        except ValueError:
            print("Invalid Date")
        else:
            break

    day = f"{day:02}"
    month = f"{month:02}"
    print(f"{year}-{month}-{day}")

outdated()

# 9/8/1636
# 1636-09-08

# September 8, 1636
# 1636-09-08

# 23/6/1912
# Reprompt

# December 80, 1980
# Reprompt

# September 8 1636
# Reprompt
