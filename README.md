# WoodsEngraved

## Setup the WoodEngraved webbapp:

1. Go to the folder where you want to create this project. 
2. Open terminal at the folder and run 
```
git clone https://github.com/DhruvPatel27/P9_New_Product_Customizor_App.git
```
3. Run 
```
source venv/bin/activate
```
4. Run 
```
python application.py dev
```
5. Go to the local host server link provided in the terminal.
6. **You are all set!!**

## Run Tests:

1. Go to the location where you checked out P9_New_Product_Customizor_App.
2. Run
```
 python -m unittest discover -s test -p '*_test.py'
```
## Generate coverage Report:

1. Go to the location where you checked out P9_New_Product_Customizor_App.
2. Run
```
coverage html -m unittest discover -s test -p '*_test.py'
```
3. Run
```
coverage html
```


## Setup Database:

### Database Information

**Database** - MySQL

**Host name** : database-1.cmuesaxglt7o.us-west-1.rds.amazonaws.com

**User name**: admin

**Password**: adminpassword

**Database name**: db4


**Tables**:
* USER
* PRODUCT
* ORDER
* MODAL
* WOOD_PATTERN
* WOOD_TYPE

### Setup:

1. Download MySQL Workbench
2. Follow step 2 and step 3 of this document to access the remote db instance. https://aws.amazon.com/getting-started/tutorials/create-mysql-db/


### Queries

**Insert queries** :

INSERT INTO `db4`.USER(LastName,FirstName,Email,Password,Role)
VALUES ('Clinton','John','john@abc.com','Password','Customer');

INSERT INTO `db4`.WOOD_TYPE(name, image)
VALUES ('Maple','');

INSERT INTO `db4`.WOOD_PATTERN(name, image)
VALUES ('Church', '');

INSERT INTO `db4`.PRODUCT(title,description,price,quantity,category,customizable,image,model_id,occasion)
VALUES ('Engraved Wood Coaster','Customize this stylish wood coaster with your favorite type of wood, a name or a message or a pattern.', '25', '50', 'Coaster', '1', '',null,'Christmas, Valentines Day, Graduation, Weddings, Mothers Day/Fathers Day');


## Release notes:

### Sprint 1:

Delivered static UI for Home, product details, occasion, login, signup, order details and wood worker pages.

### Sprint 2:

1. Created a database for product details and linked the backend with the database. 
2. Linked the frontend with backend to show data dynamically.
3. Created masks for images.

### Sprint 3:

1. User session management: Login/Register, order details
2. Woodworker’s Login Register and Order Management
3. Preview different wood type on the products in real-time
4. Pagination for product catalog page (9 products per page)

### Sprint 4:

1. Implement different types of customization for products.
2. Provide add to cart functionality for the user to make an order.
3. Provide filters for products based on a particular occasion or category.
4. Fixes for AWS hosting.
5. Provide inventory management functionality for the manager.
6. Visibility of Logged in user name on the top bar of the web application.

### Sprint 5:

1. Carpenter should be able to track orders and change the status of the order.
2. Manager should be able to remove added products
3. Manager should be able to edit the existing products
4. Fix minor UI issues
5. Customer should be able to place order
6. Implement text customization on the product

### Sprint 6:
1. Document the project
2. Improve UI for the user
3. Improve latency for customization preview
4. Add search and sort functionality to the product catalog
5. Implement Error handling to prevent a system breakdown

