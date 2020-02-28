# WoodsEngraved

## Setup the WoodEngraved webbapp:

1. Go to the folder where you want to create this project. 
2. Open terminal at the folder and run 
```
git clone https://github.com/DhruvPatel27/P9_New_Product_Customizor_App.git
```
3. Run cd source 
```
venv/bin/activate
```
4. Run 
```
python application.py
```
5. Go to the local host server link provided in the terminal.
6. **You are all set!!**

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

