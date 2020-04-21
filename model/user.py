import model.db_connection as db_connection


# Method to check if email id and password matches
def login(email, password):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from USER where `Email`=%s AND `Password`=%s"
            login_details = (email, password)
            cursor.execute(sql, login_details)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()

    return result


# Method to add a guest user in the database
def signup(lastname, firstname, email, password):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO USER VALUES(DEFAULT,%s,%s,%s,%s,'Customer')"
            signup_details = (lastname, firstname, email, password)
            result = cursor.execute(sql, signup_details)
            return result

    except Exception as e:
        print(e)

    finally:
        connection.close()
        cursor.close()
