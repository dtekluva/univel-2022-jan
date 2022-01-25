import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='store',
                             cursorclass=pymysql.cursors.DictCursor)

def create_customer_table():

    with connection:

        with connection.cursor() as cursor:


                command = "CREATE TABLE customer (id INT(10) AUTO_INCREMENT PRIMARY KEY  NOT NULL, name CHAR(30), address char(50));"

                cursor.execute(command)

        connection.commit()


def create_product_table():

    with connection:

        with connection.cursor() as cursor:


                command = "CREATE TABLE product (id INT(10) AUTO_INCREMENT PRIMARY KEY  NOT NULL, name CHAR(30), category char(50), price INT(7));"

                cursor.execute(command)

        connection.commit()

def create_invoice_table():

    with connection:

        with connection.cursor() as cursor:


                command = "CREATE TABLE invoice (id INT(10) AUTO_INCREMENT PRIMARY KEY  NOT NULL, code CHAR(30), invoice_date DATE);"

                cursor.execute(command)

        connection.commit()

def create_sales_table():

    with connection:

        with connection.cursor() as cursor:


                command = """
                            CREATE TABLE sales (id INT(10) AUTO_INCREMENT PRIMARY KEY  NOT NULL,
                            invoice_id INT(4), product_id INT(4), customer_id INT(4), unit  INT(5),
                            FOREIGN KEY (invoice_id) REFERENCES invoice (id),
                            FOREIGN KEY (product_id) REFERENCES product (id),
                            FOREIGN KEY (customer_id) REFERENCES customer (id)
                            );
                        """

                cursor.execute(command)

        connection.commit()

# create_customer_table()
# create_product_table()
# create_invoice_table()
create_sales_table()