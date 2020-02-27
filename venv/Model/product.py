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
    
# API to get the product details for the specified product id
def get_product_details(product_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `Product_id`=%s"
            cursor.execute(sql, product_id)
            result = cursor.fetchone()
    finally:
        connection.close()
    return result

#API to get products by occasion
def get_occasion_details(occasion):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where occasion like %s"
            cursor.execute(sql, '%'+occasion+'%')
            result = cursor.fetchall()
    finally:
        connection.close()

    return result

#API to get products by category
def get_category_details(category):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `category`=%s"
            cursor.execute(sql, category)
            result = cursor.fetchall()
    finally:
        connection.close()

    return result