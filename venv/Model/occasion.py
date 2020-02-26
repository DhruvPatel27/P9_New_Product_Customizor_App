import pymysql.cursors

 # Connect to the database
connection = pymysql.connect(host='database-1.cmuesaxglt7o.us-west-1.rds.amazonaws.com',
                            user='admin',
                            password='adminpassword',
                            db='db4',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


#Get product by occasion
def get_occasion_details(occasion):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where occasion like %s"
            cursor.execute(sql, '%'+occasion+'%')
            result = cursor.fetchone()
    finally:
        connection.close()

    return result

#print(get_occasion_details('Valentine'))