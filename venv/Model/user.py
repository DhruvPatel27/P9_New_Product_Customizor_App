import Model.db_connection as db_connection

def login(email,password):
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
    if(result):
        return "success"
    else:
        return "error"
    return result