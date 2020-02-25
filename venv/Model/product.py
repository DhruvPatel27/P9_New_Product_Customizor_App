import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='database-1.cmuesaxglt7o.us-west-1.rds.amazonaws.com',
                            user='admin',
                            password='adminpassword',
                            db='db4',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

# API to get the product details for the specified product id
def get_product_details(product_id):
    
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `Product_id`=%s"
            cursor.execute(sql, product_id)
            result = cursor.fetchone()
    finally:
        connection.close()
    
    return result
