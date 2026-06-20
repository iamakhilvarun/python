import csv

csv_filename = "OlympicMedals_2020.csv"

with open(
    csv_filename, encoding="utf-8", newline=""
) as csv_file:

    # Reads the first line as a string,
    # removes the newline character,
    # then splits it at commas.
    # split() returns a list.
    headers = csv_file.readline().strip("\n").split(",")

    print(f"Column headers: {headers}")

    # Creates a csv reader object.
    # Each time we iterate, it returns the next row as a list.
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)