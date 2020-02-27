import db_connection

#API to get all products from the database
def get_occasion_details():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()

    return result