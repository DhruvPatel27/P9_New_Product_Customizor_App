import Model.db_connection as db_connection
from flask import jsonify
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

# Method to add a guest user in the database
def signup(lastname, firstname, email, password):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO USER VALUES(DEFAULT,%s,%s,%s,%s,'Customer')"
            signup_details = (lastname,firstname,email,password)
            cursor.execute(sql, signup_details)
            connection.commit()
            response = jsonify('User added successfully!')
            response.status_code=200
            return response
    
    except Exception as e:
        print(e)

    finally:
        connection.close()
        cursor.close()