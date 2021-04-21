from mysql.connector import connect, Error

try:
  with connect(
          host="localhost",
          user="root",
          password="shrimad01",
          database="passport"
  )as connection:
    view_records= "SELECT * FROM users"
    with connection.cursor() as cursor:
        cursor.execute(view_records)
        result = cursor.fetchall()
except Error as e:
  print(e)

user_id = input("Enter the user id that needs to be verified ")
counter=0
flag=1
for i in result:
    if i[0]==user_id:
        flag=0
        break
    counter+=1
if flag==1:
    print("User not found")
else:
    print("")
    print("These are the details of " + result[counter][2])
    print("Name : " + result[counter][2])
    print("Email Id : " + result[counter][4])
    print("Pan Card Number : " + result[counter][5])
    print("Address : " + result[counter][6])
    print("")
    verify_choice=input("Type yes to verify the documents else type no ")
    if verify_choice=="yes":
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="shrimad01",
                    database="passport"
            )as connection:
                update_record = f"""UPDATE users
                                    SET status_police="verified"
                                    WHERE user_id='{result[counter][0]}'"""
                with connection.cursor() as cursor:
                    cursor.execute(update_record)
                    connection.commit()
                    print("")
                    print("Details Verified")
        except Error as e:
            print(e)
    else:
        print("verification has been denied")