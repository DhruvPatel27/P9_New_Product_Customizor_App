import Model.db_connection as db_connection

#API to get all orders from the database for woodworker
def get_allorders():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from ORDER"
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
