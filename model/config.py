import sys

<<<<<<< HEAD
=======

>>>>>>> master
def get_config():
    DATABASE_CONFIG = {
        'host': 'database-1.cmuesaxglt7o.us-west-1.rds.amazonaws.com',
        'user': 'admin',
        'dbname': 'db4',
        'password': 'adminpassword'
    }

    if 'test' in sys.argv:
        DATABASE_CONFIG['dbname']= 'test_db4'
    elif 'dev' in sys.argv:
        DATABASE_CONFIG['dbname']= 'db4'
    else:
        print("Please use a correct command")
        sys.exit()
    return DATABASE_CONFIG