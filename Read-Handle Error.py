filename = "sample.txt"

try:
    file = open(filename, "r")

    print("Reading file content:\n")

    line_number = 1

    for line in file:
        print("Line", line_number, ":", line.strip())
        line_number += 1

    file.close()

except FileNotFoundError:
    print("Error: The file", "'" + filename + "'", "was not found.")

except Exception as e:
    print("Something went wrong while reading the file.")
    print("Details:", e)