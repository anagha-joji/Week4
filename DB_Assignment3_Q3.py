import sqlite3

# defining connection and cursor
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Write a query that returns the HomeTeam, FTHG (number of home goals scored in a game) and FTAG (number of away goals scored in a game) from the Matches table.
query1 = """SELECT HomeTeam,FTHG,FTAG FROM Matches WHERE Season = 2010 AND HomeTeam LIKE 'Aachen' ORDER BY FTHG DESC,FTAG ASC"""
cursor.execute(query1)
results1 = cursor.fetchall()
for i in results1:
    print("HomeTeam: ", i[0])
    print("FTHG: ", i[1])
    print("FTAG: ", i[2])

# Print the total number of home games each team won during the 2016 season in descending order of number of home games from the Matches table
query2 ="""SELECT HomeTeam,COUNT(FTR) FROM Matches WHERE FTR ='H' AND Season ='2016' GROUP BY HomeTeam ORDER BY COUNT(FTR)"""
cursor.execute(query2)
results2 = cursor.fetchall()
print("The no.of games won are: ", results2)


# Write a query that returns the first ten rows from the Unique_Teams table
query3 = """SELECT * FROM Unique_Teams LIMIT 10"""
cursor.execute(query3)
results3 = cursor.fetchall()
print("The first 10 rows from Unique_ Teams Table are: " , results3)

# Print the Match_ID and Unique_Team_ID with the corresponding Team_Name from the Unique_Teams and Teams_in_Matches tables. Use the WHERE statement first and then use the JOIN statement to get the same result.
query4 = """SELECT * FROM Teams_in_Matches ,Unique_Teams WHERE Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID"""
cursor.execute(query4)
results4 = cursor.fetchall()
print("Match_ID and Unique_Team_ID using WHERE statement: " , results4)

query5 = """SELECT * FROM Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID"""
cursor.execute(query5)
results5 = cursor.fetchall()
print("Match_ID and Unique_Team_ID using JOIN: " , results5)

# Write a query that joins together the Unique_Teams data table and the Teams table, and returns the first 10 rows
query6 = """SELECT * FROM Unique_Teams JOIN Teams ON Unique_Teams.TeamName =Teams.TeamName LIMIT 10"""
cursor.execute(query6)
results6 = cursor.fetchall()
print("Result after joining Unique_Teams and Teams_table is: " , results6)

# Write a query that shows the Unique_Team_ID and TeamName from the Unique_Teams table and AvgAgeHome, Season and ForeignPlayersHome from the Teams table. Only return the first five rows.
query7 = """SELECT Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.AvgAgeHome,Teams.Season,Teams.ForeignPlayersHome FROM Unique_Teams JOIN Teams ON Unique_Teams.TeamName=Teams.TeamName LIMIT 5"""
cursor.execute(query7)
results7 = cursor.fetchall()
print("Result is: " , results7)

# Write a query that shows the highest Match_ID for each team that ends in a “y” or a “r”. Along with the maximum Match_ID, display the Unique_Team_ID from the Teams_in_Matches table and the TeamName from the Unique_Teams table.
query8 ="""SELECT MAX(Match_ID),Teams_in_Matches.Unique_Team_ID,TeamName FROM Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID =Unique_Teams.Unique_TEAM_ID WHERE (TeamName lIKE '%y')OR(TeamName LIKE '%r')GROUP BY Teams_in_Matches.Unique_Team_ID,TeamName"""
cursor.execute(query8)
results8 = cursor.fetchall()
print("Required result is: " , results8)


conn.commit()
conn.close()