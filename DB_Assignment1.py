import sqlite3

# defining connection and cursor
conn = sqlite3.connect('vehicles.db')
cursor = conn.cursor()

# creating cars table
query = """CREATE TABLE IF NOT EXISTS
cars(car_name CHAR(20) PRIMARY KEY NOT NULL,
 owner_name CHAR(20) NOT NULL)"""
cursor.execute(query)

# add to cars

cursor.execute("INSERT INTO cars VALUES ('Benz', 'Mathew')")
cursor.execute("INSERT INTO cars VALUES ('Lamborgini', 'Cathy')")
cursor.execute("INSERT INTO cars VALUES ('Skoda', 'Jose')")
cursor.execute("INSERT INTO cars VALUES ('Kia', 'Merlin')")
cursor.execute("INSERT INTO cars VALUES ('Jeep', 'Lia')")
cursor.execute("INSERT INTO cars VALUES ('Verna', 'Aparna')")
cursor.execute("INSERT INTO cars VALUES ('Hyundai', 'Beneetha')")
cursor.execute("INSERT INTO cars VALUES ('Audi', 'Gabi')")
cursor.execute("INSERT INTO cars VALUES ('Porche', 'Joji')")
cursor.execute("INSERT INTO cars VALUES ('Maruthi', 'Ananthu')")

# get results

cursor.execute("SELECT car_name, owner_name FROM CARS")
results = cursor.fetchall()
print(results)
conn.commit()
conn.close()

