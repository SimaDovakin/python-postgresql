import csv

import psycopg2

from util.insert_data import (
    create_hosts_table, 
    create_rooms_table, 
    create_reviewers_table, 
    create_reviews_table
)
from util.check_data import check_table_data


connection_string = "host='db' user='postgres' dbname='postgres'"
conn = psycopg2.connect(connection_string)

cur = conn.cursor()

# inserting all data

cur.execute("SELECT COUNT(*) FROM hosts;")
hosts_count = cur.fetchone()

if hosts_count[0] <= 0:
    with open('datasets/listings.csv', 'r') as data:
        reader = csv.reader(data)
        header = next(reader)

        create_rooms = False
        cur.execute("SELECT COUNT(*) FROM rooms;")
        rooms_count = cur.fetchone()
        if rooms_count[0] <= 0:
            create_rooms = True
        

        for row in reader:
            row = [i.strip() for i in row]
            hosts_fields = (row[2], row[3])
            print("Reviews count:", row[11])
            if row[11].strip() == '0':
                rooms_fields = tuple(row[:3] + row[4:12] + row[14:])
            else:
                rooms_fields = tuple(row[:3] + row[4:])

            if create_rooms:
                create_hosts_table(hosts_fields, cur)
                create_rooms_table(rooms_fields, cur)
            else:
                create_hosts_table(hosts_fields, cur)


cur.execute('SELECT COUNT(*) FROM reviewers;')
reviewers_count = cur.fetchone()

if reviewers_count[0] <= 0:
    with open('datasets/reviews_detailed.csv', 'r') as data:
        reader = csv.reader(data)
        header = next(reader)

        cur.execute('SELECT COUNT(*) FROM reviews;')
        reviews_count = cur.fetchone()

        create_reviews = True if reviews_count[0] <= 0 else False

        for row in reader:
            reviewer_fields = tuple(row[3:5])

            create_reviewers_table(reviewer_fields, cur)
            if create_reviews:
                review_fields = tuple(row[:4] + row[5:])
                create_reviews_table(review_fields, cur)
            

conn.commit()
cur.close()
conn.close()

