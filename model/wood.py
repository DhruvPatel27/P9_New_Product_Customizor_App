import model.db_connection as db_connection


# API to get wood images by id from the database
def get_wood_by_id(wood_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from WOOD_TYPE where `ID`=%s"
            cursor.execute(sql, wood_id)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()

    return result


# API to get all wood images from the database
def get_wood():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from WOOD_TYPE"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result

# API to get wood design images by id from the database
def get_design_by_id(design_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from WOOD_PATTERN where `ID`=%s"
            cursor.execute(sql, design_id)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()

    return result


# API to get all wood images from the database
def get_design():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from WOOD_PATTERN ORDER BY ID DESC;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result