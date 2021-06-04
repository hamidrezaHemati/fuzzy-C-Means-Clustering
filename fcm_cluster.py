import csv
dataFile = 'data1.csv'


def extract_input():
    with open(dataFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        col_num = len(next(csv_reader))  # Read first line and count columns
        csv_file.seek(0)  # go back to beginning of file
        line_count = 0
        print(col_num)
        for row in csv_reader:
            print(f'{", ".join(row)}')
            line_count += 1
        print(line_count)


def main():
    extract_input()


main()


