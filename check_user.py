from mysql.connector import connect, Error

'''see the records in the table'''
try:
    with connect(
              host="localhost",
              user="root",
            password="shrimad01",
            database="passport"
    )as connection:
        show_records="SELECT * FROM  users"
        with connection.cursor() as cursor:
            cursor.execute(show_records)
            result=cursor.fetchall()
            print(result)
except Error as e:
    print(e)