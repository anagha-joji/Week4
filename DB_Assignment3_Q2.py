import sqlite3

# defining connection and cursor
conn = sqlite3.connect('Database.sqlite')
cursor = conn.cursor()

# Counts all the rows in the Teams table
query1 ="""SELECT COUNT(*) FROM Teams """
cursor.execute(query1)
results1 = cursor.fetchall()
for i in results1:
    print("Number of rows: ", i[0])

# Print all the unique values that are included in the Season column in the Teams table
query2 = """SELECT DISTINCT(Season) FROM Teams"""
cursor.execute(query2)
results2 = cursor.fetchall()
for i in results2:
    print("Unique Values: ",i[0])

# Print the largest and smallest stadium capacity that is included in the Teams table
query3 = """SELECT MAX(StadiumCapacity), MIN(StadiumCapacity) FROM Teams"""
cursor.execute(query3)
results3 = cursor.fetchall()
for i in results3:
    print("Max Capacity: ",i[0])
    print("Min Capacity: ", i[1])

# Print the sum of squad players for all teams during the 2014 season from the Teams table [Answer - 1164]
query4 = """SELECT SUM(KaderHome)FROM Teams WHERE Season =2014"""
cursor.execute(query4)
results4 = cursor.fetchall()
for i in results4:
    print("SUM: ", i[0])


# Query the Matches table to know how many goals did Man United score during home games on average? [Answer - 2.16]
query5 = """SELECT AVG(FTHG) FROM Matches WHERE HomeTeam LIKE 'Man United' """
cursor.execute(query5)
results5 = cursor.fetchall()
for i in results5:
    print("AVERAGE::", i[0])


conn.commit()
conn.close()