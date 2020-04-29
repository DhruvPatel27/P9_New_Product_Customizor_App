import pymysql.cursors
import model.config as config


def get_connection():
    # Connect to the database
    """Connects to the database

    Returns:
        connection: a pymysql connection object after the connection is established
    
    """
    con = config.get_config()
    connection = pymysql.connect(host=con['host'],
                            user=con['user'],
                            password=con['password'],
                            db=con['dbname'],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    return connection
