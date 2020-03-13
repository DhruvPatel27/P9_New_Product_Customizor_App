import Model.db_connection as db_connection

# Method to check if email id and password matches
def signup(lastname, firstname, email, password):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO USER VALUES(DEFAULT,%s,%s,%s,%s,'Customer')"
            signup_details = (lastname,firstname,email,password)
            cursor.execute(sql, signup_details)
            connection.commit()
    
    except Error as error:
        print(error)

    finally:
        connection.close()
        cursor.close()
    
