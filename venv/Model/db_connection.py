import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='database-1.cmuesaxglt7o.us-west-1.rds.amazonaws.com',
                            user='admin',
                            password='adminpassword',
                            db='db4',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


def get_connection():
    return connection

