
def check_table_data(table_name, db_cursor):
    db_cursor.execute("SELECT COUNT(*) FROM %s;", (table_name,))
    count = db_cursor.fetchone()

    return True if count > 0 else False

