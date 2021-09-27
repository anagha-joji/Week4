import sqlite3

# defining connection and cursor
conn = sqlite3.connect('Medical.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Hospital")
cursor.execute("DROP TABLE IF EXISTS Doctor")

# creating hospital table
query1 = """CREATE TABLE 
Hospital(Hospital_Id INTEGER PRIMARY KEY NOT NULL, Hospital_Name CHAR(20) NOT NULL, Bed_Count INTEGER NOT NULL)"""
cursor.execute(query1)

# inserting into Hospital
cursor.execute("INSERT INTO Hospital VALUES('1', 'Mayo Clinic', 200)")
cursor.execute("INSERT INTO Hospital VALUES('2', 'Cleveland Clinic', 400)")
cursor.execute("INSERT INTO Hospital VALUES('3', 'Johns Hopkins', 1000)")
cursor.execute("INSERT INTO Hospital VALUES('4', 'UCLA Medical Center', 1500)")

# creating doctor table
query2 = """CREATE TABLE
Doctor (Doctor_Id INTEGER PRIMARY KEY NOT NULL, Doctor_Name CHAR(20) NOT NULL, Hospital_Id INTEGER, Joining_Date TEXT, Speciality CHAR(20) NOT NULL, Salary INTEGER NOT NULL, 
        Experience, FOREIGN KEY (Hospital_id) REFERENCES Hospital (Hospital_id))"""
cursor.execute(query2)

# inserting data into Doctor
cursor.execute("INSERT INTO Doctor VALUES('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL)")

def get_connection():
    connection = sqlite3.connect('Medical.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

spcl = input("Speciality: ").lower().capitalize()
sal = input("Salary: ")
query = """SELECT * from Doctor WHERE Speciality = ? AND Salary >= ?"""
cursor.execute(query, (spcl, sal))
record = cursor.fetchall()
for row in record:
    print("Doctor Id: ", row[0])
    print("Doctor Name: ", row[1])
    print("Hospital Id: ", row[2])
    print("Joining Date: ", row[3])
    print("Specialty: ", row[4])
    print("Salary: ", row[5])
    print("Experience: ", row[6], "\n")
print("\n")
Hospital_id = input("Select ID for info:")
select_query = """SELECT * from Hospital WHERE Hospital_Id = ?"""
cursor.execute(select_query, (Hospital_id,))
records = cursor.fetchone()
hospitaldetails = records[1]
sql_ = """SELECT * from Doctor WHERE Hospital_Id = ?"""
cursor.execute(sql_,(Hospital_id) )
record = cursor.fetchall()
for row in record:
    print("Doctor Name:", row[1])
    print("Hospital Id:", row[2])
    print("Hospital name",hospitaldetails, "\n")


conn.commit()
conn.close()