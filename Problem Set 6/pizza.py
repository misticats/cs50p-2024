import sys
import csv
from tabulate import tabulate


def main():
    filepath = check_arg()
    file_exist(filepath)
    print(ascii_table(filepath))


def check_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    else:
        return sys.argv[1]


def file_exist(filepath):
    try:
        with open(filepath) as file:
            exit
    except FileNotFoundError:
         sys.exit("File does not exist")


def ascii_table(filepath):
    with open(filepath) as file:

        # variable to iterate over any line in the csv file
        # csv.reader automatically parses each row into a list
        reader = csv.reader(file)
        # specifically mark the first line as {headers}
        # goes to the next line after
        headers = next(reader)
        # go line by line
        # header already got the first line and nexted you to the 2nd line
        rows = [row for row in reader]
        # transform into ascii
        # list of lists, list of column names, ascii-form
        return tabulate(rows, headers, tablefmt="grid")


if __name__ == "__main__":
    main()
