import model.db_connection as db_connection
from flask import jsonify

#API to get all orders from the database for woodworker
def get_all_orders():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from `ORDERS`"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()
        
    return result


# API to get the order details for the specified user id
def get_order_details_for_user(user_name):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from `ORDER` where `email_id`=%s"
            cursor.execute(sql, user_name)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()
        
    return result


# API to update database on add to cart
def add_to_cart(product_id, image, quantity, wood_id, pattern_id, user_name, total_cost):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO CUSTOMER_ORDER(`product_id`,`user_id`,`email_id`,`woodtype_id`,`woodpattern_id`,`total_cost`,`state`,`order_date`,`quantity`,`Order_Id`,`image`) VALUES(%s, null, %s, %s, %s, %s,'InCart', '', %s, null, %s)"
            cart_details = (product_id, user_name, wood_id, pattern_id, total_cost, quantity, image)
            cursor.execute(sql, cart_details)
            connection.commit()
            response = jsonify('Product added successfully!')
            response.status_code = 200
            return response

    except Exception as e:
        print(e)

    finally:
        connection.close()
        cursor.close()


# API to get the cart product details
def load_cart(user_name):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from CUSTOMER_ORDER where `email_id`=%s AND `state`=%s"
            cart_details = (user_name, 'InCart')
            cursor.execute(sql, cart_details)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result