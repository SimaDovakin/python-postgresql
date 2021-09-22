import time

import psycopg2


time.sleep(10)

connection_string = "host='db' user='postgres' dbname='postgres'"
conn = psycopg2.connect(connection_string)

cur = conn.cursor()

cur.execute("SELECT version()")

db_version = cur.fetchone()
print("Database version is", db_version)

