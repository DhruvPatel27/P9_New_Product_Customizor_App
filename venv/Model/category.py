import pymysql.cursors

 # Connect to the database
connection = pymysql.connect(host='database-1.cmuesaxglt7o.us-west-1.rds.amazonaws.com',
                            user='admin',
                            password='adminpassword',
                            db='db4',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


#Get product by category
def get_category_details(category):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `category`=%s"
            cursor.execute(sql, category)
            result = cursor.fetchone()
    finally:
        connection.close()

    return result

#print(get_category_details('Coaster'))
