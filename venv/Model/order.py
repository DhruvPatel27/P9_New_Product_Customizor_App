import Model.db_connection as db_connection

#API to get all orders from the database
def get_allorders():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from ORDER"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result
