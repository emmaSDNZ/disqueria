import mysql.connector

mydb = mysql.connector.connect(
   host = 'localhost',
            port = 3306,
            user = 'root',
            password = "1234",
            db = 'disqueria'
)

mycursor = mydb.cursor()


