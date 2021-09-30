import sqlite3

# defining connection and cursor
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Printing the names of both the Home Teams and Away Teams
query1 = """ SELECT HomeTeam,AwayTeam FROM Matches WHERE Season = 2015 AND FTHG = 5 """
cursor.execute(query1)
results1 = cursor.fetchall()
print(results1)

# Printing the details of the matches where Arsenal is the Home Team and FTR  is A
query2 = """SELECT * FROM Matches WHERE HomeTeam LIKE 'Arsenal' AND FTR LIKE 'A' """
cursor.execute(query2)
results2 = cursor.fetchall()
for row in results2:
    print("\nMatch ID: ", row[0])
    print("Div: ", row[1])
    print("Season: ", row[2])
    print("Date: ", row[3])
    print("Home Team: ",row[4])
    print("Away Team: ", row[5])
    print("FTHG: ", row[6])
    print("FTAG: ", row[7])
    print("FTR: ", row[8], '\n')

# Print all the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2
query3 = "SELECT * FROM Matches WHERE 2012 <= Season AND Season <= 2015 AND AwayTeam = 'Bayern Munich' AND FTHG > 2"
cursor.execute(query3)
results3 = cursor.fetchall()
for row in results3:
    print("\nMatch ID: ", row[0])
    print("Div: ", row[1])
    print("Season: ", row[2])
    print("Date: ", row[3])
    print("Home Team: ",row[4])
    print("Away Team: ", row[5])
    print("FTHG: ", row[6])
    print("FTAG: ", row[7])
    print("FTR: ", row[8], '\n')

# Print all the matches where the Home Team name begins with “A” and Away Team name begins with “M”
query4 = """SELECT * FROM Matches WHERE HomeTeam LIKE 'A%' AND AwayTeam LIKE 'M%' """
cursor.execute(query4)
results4 = cursor.fetchall()
print(results4)

conn.commit()
conn.close()





