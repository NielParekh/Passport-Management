from mysql.connector import connect, Error
import uuid

uuid_user = uuid.uuid4()
choice = input("Enter new or renew ")
username = input("Enter username ")
password = input("Enter password ")
email_id = input("Enter email id ")
pan_card = input("Enter pan card ")
address = input("Address ")
status_admin = "pending"
status_police = "pending"

'''adding record to the table'''
try:
    with connect(
              host="localhost",
              user="root",
            password="shrimad01",
            database="passport"
    )as connection:
        add_records=f"INSERT INTO users(user_id,choice,username,password,email_id,pan_card,address,status_admin,status_police) VALUES('{uuid_user}','{choice}','{username}','{password}','{email_id}','{pan_card}','{address}','{status_admin}','{status_police}')"
        with connection.cursor() as cursor:
            cursor.execute(add_records)
            connection.commit()
except Error as e:
    print(e)