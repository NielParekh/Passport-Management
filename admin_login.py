from mysql.connector import connect, Error


def admin_login():
    try:
        with connect(
                host="localhost",
                user="root",
                password="shrimad01",
                database="passport"
        )as connection:
            view_records = "SELECT * FROM admins"
            with connection.cursor() as cursor:
                cursor.execute(view_records)
                result = cursor.fetchall()
    except Error as e:
        print(e)
    access = 1
    flag = 1
    counter = 0
    username = input("Enter username : ")
    for i in result:
        if i[0] == username:
            flag = 0
            break
        counter += 1
    if flag == 0:
        password = input("Enter password : ")
        if password == result[counter][1]:
            access = 0
            return "access granted to " + result[counter][0], access
        else:
            return "access denied", access
    else:
        return "User not found as an admin", access