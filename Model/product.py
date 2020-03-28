import Model.db_connection as db_connection
import Model.utils as utils
from PIL import Image

#API to get all products from the database
def get_products():
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result
    
# API to get the product details for the specified product id
def get_product_details(product_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `Product_id`=%s"
            cursor.execute(sql, product_id)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()
    return result

#API to get products by occasion
def get_products_by_occasion(occasion):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where occasion like %s"
            cursor.execute(sql, '%'+occasion+'%')
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result

#API to get products by category
def get_products_by_category(category):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from PRODUCT where `category`=%s"
            cursor.execute(sql, category)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result

#API to get product mask by Model id
def get_products_mask(model_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from MODAL where `ID`=%s"
            cursor.execute(sql, model_id)
            result = cursor.fetchall()
    finally:
        connection.close()
        cursor.close()

    return result


# API to get the product title, description and price for the specified product id
def get_product_details_cart(product_id):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT Product_id, title, description, image, price from PRODUCT where `Product_id`=%s"
            cursor.execute(sql, product_id)
            result = cursor.fetchone()
    finally:
        connection.close()
        cursor.close()
    return result

# Method to add multiple products to the catalog
def add_products(data_xls):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO PRODUCT(`Product_id`,`title`,`description`,`price`,`category`,`customizable`,`occasion`,`image`,`model_id`) VALUES(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s)"
            for i,row in data_xls.iterrows():
                img1 = "No File"
                img2 = "No file"
                img3 = "No File"
                with open(tuple(row)[6], "rb") as image_file:
                    img1 = utils.image_encoding(image_file)
                with open(tuple(row)[7], "rb") as image_file:
                    img2 = utils.image_encoding(image_file)
                with open(tuple(row)[8], "rb") as image_file:
                    img3 = utils.image_encoding(image_file)
                if img1 == "No File":
                    Exception("Please specify correct path")
                row['product_image'] = img1
                modal_id = add_modal(img3, img2)
                product = tuple(row[:7],) + (modal_id,)
                cursor.execute(sql, product)
                connection.commit()
    finally:
        connection.close()
        cursor.close()
    return


# Method to add mask and modal to database
def add_modal(modal_mask, image_mask):
    connection = db_connection.get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO MODAL VALUES(DEFAULT,%s,%s)"
            mask = (modal_mask,image_mask)
            cursor.execute(sql, mask)
            connection.commit()
            return cursor.lastrowid
    except Exception as e:
        print(e)
    finally:
        connection.close()
        cursor.close()
