import Model.db_connection as db_connection

#API to get all orders from the database for woodworker
def get_all_orders():
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
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql1 = "SELECT `ID` from USER where `Email`=%s"
            cursor.execute(sql1, user_name)
            user_id = cursor.fetchone()
            sql = "SELECT * from `ORDER` where `user_id`=%s"
            cursor.execute(sql,user_id['ID'])
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()
        
    return result

# API to get order details based on order id
def get_order_details_by_id(order_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from `CUSTOMER_ORDER` where `ID`=%s"
            
            cursor.execute(sql,order_id)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()
        
    return result

# API to change the order status for a specific order
def update_order_status_for_order(order_status,order_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `CUSTOMER_ORDER` SET `state` = %s where `ID` = %s"
            cursor.execute(sql,(order_status,order_id))
            connection.commit()            
    finally:
        connection.close()
        cursor.close()
    
    return