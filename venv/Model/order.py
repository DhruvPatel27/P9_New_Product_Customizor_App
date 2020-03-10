import Model.db_connection as db_connection


# API to get the order details for the specified user id
def get_order_details_for_user(user_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from ORDER where `user_id`=%s"
            cursor.execute(sql, user_id)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()
    return result
