import sys
from PIL import Image, ImageOps
import os


def main():
    inputfile, outputfile = check_arg()
    check_filetype(inputfile, outputfile)
    check_fileexist(inputfile)
    tshirt(inputfile, outputfile)


def check_arg():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    else:
        return sys.argv[1], sys.argv[2]


def check_filetype(inputfile, outputfile):
    extensions = [".jpg", ".jpeg", ".png"]
    root1, ext1 = os.path.splitext(inputfile)
    root2, ext2 = os.path.splitext(outputfile)

    if ext1 not in extensions or ext2 not in extensions:
        sys.exit("Wrong file type")
    elif not ext1 == ext2:
        sys.exit("Input and output are not of the same file type")


def check_fileexist(inputfile):
    try:
        with open(inputfile) as file:
            pass
    except FileNotFoundError:
        sys.exit("File not found")


def tshirt(inputfile, outputfile):
    input_open = Image.open(inputfile)
    shirt = Image.open("shirt.png")

    # Open inputfile and resize/crop to match the shirt
    cropped_input = ImageOps.fit(input_open, shirt.size, method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    # Overlay shirt onto image (image to paste, position, image to make it transparent?)
    cropped_input.paste(shirt, (0, 0), shirt)
    # save the pasted image
    cropped_input.save(outputfile, format=None)


if __name__ == "__main__":
    main()
