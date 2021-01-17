import mysql.connector

db = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="tvbtvb123",
       database="recipes"
)

mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE recipes")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE TABLE entries (Name VARCHAR(255), Type VARCHAR(255), Ingredients VARCHAR(255))")
# mycursor.execute("ALTER TABLE entries ADD Website VARCHAR(255) NOT NULL")

# sqlFormula = "INSERT INTO entries (Name, Type, Ingredients, Website) VALUES (%s, %s, %s, %s)"
# entry = ("a", "a", "a", "a")
# mycursor.execute(sqlFormula, entry)

# sql = "DELETE FROM entries WHERE Name = 'a'"
# mycursor.execute(sql)

db.commit()