import Model.db_connection as db_connection

# Method to check if email id and password matches
def login(email, password):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from USER where `Email`=%s AND `Password`=%s"
            login_details = (email,password)
            cursor.execute(sql, login_details)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()
    
    return result


# Method to fetch the user details
def get_user_details(user_name):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from USER where `Email`=%s"
            cursor.execute(sql, user_name)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()
    return result
