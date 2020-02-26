import db_connection

#API to get products by category
def get_category_details(category):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `category`=%s"
            cursor.execute(sql, category)
            result = cursor.fetchone()
    finally:
        connection.close()

    return result

print(get_category_details('Coaster'))
