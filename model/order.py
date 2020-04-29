import model.db_connection as db_connection
from datetime import datetime


# API to get all orders from the database for woodworker
def get_all_orders():
    """Gets all the active orders

    Returns:
        result: collection of all the active orders 
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from `CUSTOMER_ORDER`"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result


# API to get the order details for the specified user id
def get_order_details_for_user(user_name):
    """Gets all the orders for a particular user

    Arguments:
        user_name: name of the user

    Returns:
        list: collection of all the orders for a user
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from CUSTOMER_ORDER where `email_id`=%s AND `state`<>%s"
            cart_details = (user_name, 'In Cart')
            cursor.execute(sql, cart_details)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result


# API to update database on add to cart
def add_to_cart(product_id, image, quantity, wood_id, pattern_id, user_name, total_cost):
    """Creates a new order in the cart

    Arguments:
        product_id: product id
        image: customized image
        quantity: number of items
        wood_id: selected wood type
        pattern_id: selected wood pattern
        user_name: name of the user
        total_cost: cost of the final order
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            order_date = datetime.today().strftime('%Y-%m-%d')
            sql = "INSERT INTO CUSTOMER_ORDER(`product_id`,`user_id`,`email_id`,`woodtype_id`,`woodpattern_id`," \
                  "`total_cost`,`state`,`order_date`,`quantity`,`Order_Id`,`image`) VALUES(%s, null, %s, %s, %s, %s," \
                  "'In Cart', %s, %s, null, %s) "
            cart_details = (product_id, user_name, wood_id, pattern_id, total_cost, order_date, quantity, image)
            result = cursor.execute(sql, cart_details)
            order_id = cursor.lastrowid
            connection.commit()
            return result, order_id

    except Exception as e:
        print(e)

    finally:
        connection.close()
        cursor.close()


# API to get the cart details
def load_cart(user_name):
    """Load products in the cart

    Arguments:
        user_name: name of the user

    Returns:
        result: list of products in the cart
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from CUSTOMER_ORDER where `email_id`=%s AND `state`=%s"
            cart_details = (user_name, 'In Cart')
            cursor.execute(sql, cart_details)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result


# API to get order details based on order id
def get_order_details_by_id(order_id):
    """Get all the order deatils by order id

    Arguments:
        order_id: order id

    Returns:
        result: details of the order
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from `CUSTOMER_ORDER` where `ID`=%s"
            cursor.execute(sql, order_id)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()

    return result


# API to change the order status for a specific order
def update_order_status_for_order(order_status, order_id):
    """Update the order status

    Arguments:
        order_id: order id
        order_status: new order status

    Returns:
        result: updated order with updated status
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `CUSTOMER_ORDER` SET `state` = %s where `ID` = %s"
            result = cursor.execute(sql, (order_status, order_id))
            connection.commit()
    finally:
        connection.close()
        cursor.close()

    return result


# API to remove from cart
def remove_cart(product_id):
    """Remove the product from cart

    Arguments:
        product_id: product id

    Returns:
        result: 1 if the product was removed successfully else 0
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE from CUSTOMER_ORDER where `ID`=%s"
            result = cursor.execute(sql, product_id)
            connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()
        cursor.close()

    return result


# API to place order
def place_order(user_name, price, address, zipcode, card_number, expiry, cvv, contact):
    """Place an order

    Arguments:
        user_name: name of the user
        price: total payment amount
        address: shipping address
        zipcode: zipcode
        card_number: encrypted card number
        expiry: expiry date on the card
        cvv: encrypted cvv
        contact: contact numnber

    Returns:
        result: details of the order
        order_id: new id for the order
    
    """
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO ORDERS(`Address`,`Pincode`,`Contact_No`,`Card_No`,`cvv`,`expiry_date`,`total_price`) " \
                  "VALUES(%s, %s, %s, %s, %s, %s, %s) "
            cart_details = (address, zipcode, contact, card_number, cvv, expiry, price)
            result = cursor.execute(sql, cart_details)
            connection.commit()

            order_id = cursor.lastrowid
            sql1 = "UPDATE CUSTOMER_ORDER SET `Order_Id`=%s where `email_id`=%s AND `state`=%s"
            id_update = (order_id, user_name, 'In Cart')
            cursor.execute(sql1, id_update)
            connection.commit()

            sql2 = "UPDATE CUSTOMER_ORDER SET `state`=%s where `Order_Id`=%s"
            order_update = ('Order Received', order_id)
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

    return result, order_id
