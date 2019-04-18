import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123abc",
    auth_plugin='mysql_native_password',
    database = "testDb"
     )

my_cursor=mydb.cursor()

my_cursor.execute("CREATE DATABASE test0850")

my_cursor.execute("show databases")
my_cursor.execute("DROP TABLE users")

my_cursor.execute("""CREATE TABLE users (name VARCHAR(255),
                        email VARCHAR(255),
                        age INTEGER(10),
                        userId Integer NOT NULL AUTO_INCREMENT,
                         PRIMARY KEY(userId))""")

insert = "INSERT INTO users (name, email, age) VALUES (%s,%s,%s)"
records = [("Tim", "tim@tim.com", 32) , ("Mary", "Mary@mary.com" , 18),]
records1=("Ka","yang@yang.com",34)
try:
    my_cursor.execute(insert, records1)
    my_cursor.executemany(insert,records)
    mydb.commit()

except mysql.connector.Error as err:
    print(err.msg)

my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%'")
#my_cursor.execute("SELECT * FROM users WHERE name LIKE 'T%'")

for i in my_cursor:
    print(i)

delete1 = "DELETE FROM users where name='Ka'"
my_cursor.execute(delete1)
mydb.commit()