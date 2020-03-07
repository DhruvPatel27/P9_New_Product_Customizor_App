import Model.db_connection as db_connection

#API to get all wood images from the database
def get_wood():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from WOOD_TYPE"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result
