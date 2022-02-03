import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='univelcity',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:

    # CREATE TABLE
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "CREATE TABLE laptops (name CHAR(40), manufacturer CHAR(25), color CHAR(20))"
    #     cursor.execute(sql)

    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()
  
    # # INSERT INTO TABLE
    # with connection.cursor() as cursor:

    #     sql = "INSERT INTO laptops (name, manufacturer, color) VALUES('{}','{}','{}')".format("Legion", "Lenovo", "Grey")
    #     cursor.execute(sql)

    # connection.commit()

    # INSERT MULTIPLE INTO TABLE
    with connection.cursor() as cursor:

        laptops = [("gram", "lg", "Red"), ("katana", "msi", "grey"), ("spectre", "hp", "silver")]
        students = [("john", "m", "sassy"), ("vivian", "f", "Cheeky"), ("Lola", "F", "Witty")]

        # for laptop in laptops:

            # sql = "INSERT INTO laptops (name, manufacturer, color) VALUES('{}','{}','{}')".format(*laptop)
            # sql = "INSERT INTO laptops (name, manufacturer, color) VALUES('{}','{}','{}')".format(laptop[0], laptop[1], laptop[2])

            # cursor.execute(sql)

        for name, maker, color in laptops:

            sql = "INSERT INTO laptops (name, manufacturer, color) VALUES('{}','{}','{}')".format(name, maker , color)

            cursor.execute(sql)

    connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #     cursor.execute(sql, ('webmaster@python.org',))
    #     result = cursor.fetchone()
    #     print(result)