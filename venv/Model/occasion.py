import db_connection

#API to get products by occasion
def get_occasion_details(occasion):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where occasion like %s"
            cursor.execute(sql, '%'+occasion+'%')
            result = cursor.fetchone()
    finally:
        connection.close()

    return result

#print(get_occasion_details('Valentine'))