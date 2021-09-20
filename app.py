import csv


hosts = set()
rooms_num = 0

with open('datasets/listings.csv', 'r') as table:
    reader = csv.reader(table)

    heading = next(reader)

    for row in reader:
        hosts.add(row[2])
        rooms_num += 1

print(len(hosts), rooms_num)

