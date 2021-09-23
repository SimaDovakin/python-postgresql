
def create_hosts_table(fields: tuple, db_cursor):
    """
    :param: fields     tuple with host_id and host_name
    :param: db_cursor     just a cursor of db
    """

    query_to_select_one = """
        SELECT host_id FROM hosts WHERE host_id = %s;
    """

    sql_query = """
        INSERT INTO hosts
            (host_id, host_name)
            SELECT %s, %s WHERE
                NOT EXISTS (
                    SELECT host_id FROM hosts WHERE host_id = %s
                );
    """

    host = db_cursor.execute(query_to_select_one, (fields[0],))

    if host:
        return

    db_cursor.execute(sql_query, (*fields, fields[0]))


def create_rooms_table(fields: tuple, db_cursor):
    """
    :param: fields     tuple with fields for rooms table
    :param: db_cursor     just a cursor of db
    """

    sql_query = """
        INSERT INTO rooms (
            id,
            name,
            host_id,
            neighbourhood_group,
            neighbourhood,
            latitude,
            longitude,
            room_type,
            price,
            minimum_nights,
            number_of_reviews,
            last_review,
            reviews_per_month,
            calculated_host_listings_count,
            availability_365
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s 

        );
    """

    db_cursor.execute(sql_query, fields)

