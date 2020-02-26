import db_connection

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