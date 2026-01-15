import sys
import csv


def main():
    inputfile, outputfile = check_arg()
    students = input_file(inputfile)
    output_file(students, outputfile)


def check_arg():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    else:
        return sys.argv[1], sys.argv[2]


def input_file(inputfile):
    try:
        with open(inputfile) as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                # {"name": "Abbott, Hannah", "house": "Gryffindor"}
                lastname, firstname = row["name"].split(", ")
                students.append({'last': lastname,'first': firstname, 'house': row["house"]})
            return students
    except FileNotFoundError:
        sys.exit("File not found")


def output_file(students, outputfile):
    with open(outputfile, 'w') as file:
        # first,last,house
        # fieldnames, specifies the order of the keys
        fieldnames = ["first", "last", "house"]
        # tell the DictWriter to write in order as specified in fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
           writer.writerow(student)


if __name__ == "__main__":
    main()
