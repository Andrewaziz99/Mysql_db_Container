import mysql.connector

# Connect to the database  

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="my-secret-pw",
    port="4444"
)

# Create a cursor object

mycursor = mydb.cursor()

# Execute the query

mycursor.execute("USE university")
mycursor.execute("INSERT INTO students (Id, Name) VALUES (1, 'John')")
mycursor.execute("INSERT INTO students (Id, Name) VALUES (2, 'Mary')")
mycursor.execute("INSERT INTO students (Id, Name) VALUES (3, 'Peter')")
mycursor.execute("INSERT INTO students (Id, Name) VALUES (4, 'Kate')")
mycursor.execute("INSERT INTO students (Id, Name) VALUES (5, 'Jane')")
mycursor.execute("INSERT INTO students (Id, Name) VALUES (6, 'Bob')")


#fetch all the rows from the database

mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()

print(myresult)