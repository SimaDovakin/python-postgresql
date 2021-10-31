import psycopg2


connection_string = "host='db' user='postgres' dbname='postgres'"
conn = psycopg2.connect(connection_string)

cur = conn.cursor()

create_hosts_table_query = """
    CREATE TABLE IF NOT EXISTS hosts (
        host_id INTEGER PRIMARY KEY,
        host_name VARCHAR(60)
    );
"""

create_rooms_table_query = """
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        host_id INTEGER,
        neighbourhood_group VARCHAR(80),
        neighbourhood VARCHAR(80),
        latitude NUMERIC(9, 5),
        longitude NUMERIC(9, 5),
        room_type VARCHAR(40),
        price INTEGER,
        minimum_nights SMALLINT,
        number_of_reviews INTEGER,
        last_review DATE NULL,
        reviews_per_month NUMERIC(8, 4) NULL,
        calculated_host_listings_count SMALLINT,
        availability_365 SMALLINT,
        CONSTRAINT fk_host
            FOREIGN KEY(host_id)
                REFERENCES hosts(host_id)
    ); 

"""

create_reviewers_table_query = """
    CREATE TABLE IF NOT EXISTS reviewers (
        reviewer_id INTEGER PRIMARY KEY,
        reviewer_name VARCHAR(80)
    );
"""

create_reviews_table_query = """
    CREATE TABLE IF NOT EXISTS reviews (
        listing_id INTEGER,
        id INTEGER PRIMARY KEY,
        date DATE NULL,
        reviewer_id INTEGER,
        comment TEXT,
        CONSTRAINT fk_listing
            FOREIGN KEY(listing_id)
                REFERENCES rooms(id),
        CONSTRAINT fk_reviewer
            FOREIGN KEY(reviewer_id)
                REFERENCES reviewers(reviewer_id)
    );
"""

cur.execute(create_hosts_table_query)
cur.execute(create_rooms_table_query)
cur.execute(create_reviewers_table_query)
cur.execute(create_reviews_table_query)

conn.commit()

cur.close()
conn.close()

