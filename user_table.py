from mysql.connector import connect, Error


'''dropping existing table'''
try:
    with connect(
        host="localhost",
        user="root",
        password="shrimad01",
        database="passport"
    )as connection:
        drop_table_query= "DROP TABLE users"
        with connection.cursor() as cursor:
            cursor.execute(drop_table_query)
            connection.commit()
except Error as e:
    print(e)

'''creating the user table'''
try:
    with connect(
        host="localhost",
        user="root",
        password="shrimad01",
        database="passport"
    )as connection:
        create_table_query = """CREATE TABLE users(
                                user_id varchar(100),
                                choice char(15),
                                username varchar(50),
                                password varchar(50),
                                email_id varchar(70),
                                pan_card varchar(10),
                                address varchar(100),
                                status_admin char(10),
                                status_police char(10))"""
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
except Error as e:
    print(e)