from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="shrimad01"
    ) as connection:
        create_db_query = "CREATE DATABASE passport"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

try:
  with connect(
          host="localhost",
          user="root",
          password="shrimad01",
          database="passport"
  )as connection:
    test_table_query = "CREATE TABLE admins(user_id varchar(10), name varchar(40), city varchar(40) )"
    show_table="Drop table admins"
    with connection.cursor() as cursor:
      cursor.execute(show_table)
      connection.commit()
except Error as e:
  print(e)