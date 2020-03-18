import Model.db_connection as db_connection
#API to get all products from the database
def get_products():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

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
        cursor.close()
    return result

#API to get products by occasion
def get_products_by_occasion(occasion):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where occasion like %s"
            cursor.execute(sql, '%'+occasion+'%')
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result

#API to get products by category
def get_products_by_category(category):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `category`=%s"
            cursor.execute(sql, category)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result

#API to get product mask by Model id
def get_products_mask(model_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from MODAL where `ID`=%s"
            cursor.execute(sql, model_id)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result