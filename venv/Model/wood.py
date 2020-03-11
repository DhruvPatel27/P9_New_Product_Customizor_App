import Model.db_connection as db_connection

#API to get all wood images from the database
def get_wood(wood_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from WOOD_TYPE where `ID`=%s"
            cursor.execute(sql,wood_id)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()

    return result
