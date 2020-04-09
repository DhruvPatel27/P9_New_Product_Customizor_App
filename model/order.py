import model.db_connection as db_connection
from flask import jsonify
from datetime import datetime

# API to get all orders from the database for woodworker
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
            sql = "SELECT * from CUSTOMER_ORDER where `email_id`=%s AND `state`<>%s"
            cart_details = (user_name, 'InCart')
            cursor.execute(sql, cart_details)
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
            sql = "INSERT INTO CUSTOMER_ORDER(`product_id`,`user_id`,`email_id`,`woodtype_id`,`woodpattern_id`," \
                  "`total_cost`,`state`,`order_date`,`quantity`,`Order_Id`,`image`) VALUES(%s, null, %s, %s, %s, %s," \
                  "'InCart', '', %s, null, %s) "
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


# API to get the cart details
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


# API to remove from cart
def remove_cart(user_name, product_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE from CUSTOMER_ORDER where `email_id`=%s AND `state`=%s AND `product_id`=%s"
            cart_details = (user_name, 'InCart', product_id)
            cursor.execute(sql, cart_details)
            connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()
        cursor.close()


# API to place order
def place_order(user_name, price, address, zipcode, card_number, expiry, cvv, contact):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO ORDERS(`Address`,`Pincode`,`Contact_No`,`Card_No`,`cvv`,`expiry_date`,`total_price`) " \
                  "VALUES(%s, %s, %s, %s, %s, %s, %s) "
            cart_details = (address, zipcode, contact, card_number, cvv, expiry, price)
            cursor.execute(sql, cart_details)
            connection.commit()

            order_id = cursor.lastrowid
            sql1 = "UPDATE CUSTOMER_ORDER SET `Order_Id`=%s where `email_id`=%s AND `state`=%s"
            id_update = (order_id, user_name, 'InCart')
            cursor.execute(sql1, id_update)
            connection.commit()

            sql2 = "UPDATE CUSTOMER_ORDER SET `state`=%s where `Order_Id`=%s"
            order_update = ('Recieved', order_id)
            cursor.execute(sql2, order_update)
            connection.commit()

            order_date = datetime.today().strftime('%Y-%m-%d')
            sql2 = "UPDATE CUSTOMER_ORDER SET `order_date`=%s where `Order_Id`=%s"
            date_update = (order_date, order_id)
            cursor.execute(sql2, date_update)
            connection.commit()
    except Exception as e:
        print(e)

    finally:
        connection.close()
        cursor.close()
