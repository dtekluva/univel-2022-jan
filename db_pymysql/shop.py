from unittest import result
from numpy import insert
import pymysql.cursors
from pprint import pprint

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


###################################################
###################################################
################## INSERTION ######################
###################################################
###################################################

def insert_customer(name, address):

        with connection:

                with connection.cursor() as cursor:


                        command = """
                                INSERT INTO customer (name, address) VALUES('{}','{}')
                                """.format(name, address)

                        cursor.execute(command)

                connection.commit()
                
def insert_product(name, category, price):

        with connection:

                with connection.cursor() as cursor:


                        command = """
                                INSERT INTO product (name, category, price) VALUES('{}','{}', '{}')
                                """.format(name, category, price)

                        cursor.execute(command)

                connection.commit()
                
def insert_invoice():

        with connection:

                with connection.cursor() as cursor:
                        invoices = [("11X100", "2021-01-28"), ("11X101", "2022-01-27")]

                        for invoice in invoices:
                                command = """
                                        INSERT INTO invoice (code, invoice_date) VALUES('{}','{}')
                                        """.format(*invoice)

                                cursor.execute(command)

                connection.commit()

def insert_sale():

        with connection:

                with connection.cursor() as cursor:
                        sales = [("1", "1", "1", 20), ("2", "1", "2", 20), ("1", "1", "2", 100)]

                        for sale in sales:
                                command = """
                                        INSERT INTO sales (invoice_id, product_id, customer_id, unit) VALUES('{}','{}','{}','{}')
                                        """.format(*sale)

                                cursor.execute(command)

                connection.commit()

def fetch_sale():

        with connection:

                with connection.cursor() as cursor:
                        command = """
                                        SELECT sales.id, invoice.code, product.name, customer.name, sales.unit from sales
                                        JOIN invoice ON sales.invoice_id = invoice.id
                                        JOIN product ON sales.product_id = product.id
                                        JOIN customer ON sales.customer_id = customer.id;
                                """

                        cursor.execute(command)
                        result_data = cursor.fetchall()
                        pprint(result_data)


# create_customer_table()
# create_product_table()
# create_invoice_table()
# create_sales_table()

# insert_customer("Kunle", "Abeokuta")
# insert_product("Iphone 13 Pro Max", "Device", 1101500)
# insert_customer("Kunle", "Abeokuta")
# insert_invoice()
# insert_sale()
fetch_sale()