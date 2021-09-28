import sqlite3

# defining connection and cursor
conn = sqlite3.connect('Company.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Employee")
cursor.execute("DROP TABLE IF EXISTS Departments")

# creating Employee table
query1 = """CREATE TABLE 
Employee(Employee_Name CHAR(20) NOT NULL, Employee_Id INTEGER PRIMARY KEY NOT NULL, Salary INTEGER NOT NULL, 
Department_Id INTEGER NOT NULL,  FOREIGN KEY (Department_id) REFERENCES Departments (Department_id))"""
cursor.execute(query1)

qquery1 = """ALTER TABLE Employee ADD City CHAR(20)"""
cursor.execute(qquery1)

# inserting into Employee
cursor.execute("INSERT INTO Employee VALUES('Anagha','1', 30000, '101', 'Kottayam')")
cursor.execute("INSERT INTO Employee VALUES('Sreya','2', 40000, '102', 'Kochi')")
cursor.execute("INSERT INTO Employee VALUES('Nevin','3', 25000, '103', 'Trivandrum')")
cursor.execute("INSERT INTO Employee VALUES('Elvin','4', 30000, '104', 'Kozhikode')")
cursor.execute("INSERT INTO Employee VALUES('Beneetha','5', 50000, '105', 'Kottayam')")

# creating Departments Table
query2 = """CREATE TABLE 
Departments(Department_Id INTEGER PRIMARY KEY NOT NULL, Department_Name CHAR(20) NOT NULL)"""
cursor.execute(query2)

# inserting into Departments
cursor.execute("INSERT INTO Departments VALUES('101', 'Business')")
cursor.execute("INSERT INTO Departments VALUES('102', 'Finance')")
cursor.execute("INSERT INTO Departments VALUES('103', 'Coding')")
cursor.execute("INSERT INTO Departments VALUES('104', 'Testing')")
cursor.execute("INSERT INTO Departments VALUES('105', 'Networking')")

# printing name,id,salary from Employee
cursor.execute("SELECT Employee_Name, Employee_Id, Salary FROM Employee")
results = cursor.fetchall()
print(results)

def get_connection():
    connection = sqlite3.connect('Company.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

# printing details of Employee
def print_details(letter):
    cursor.execute("SELECT * FROM Employee WHERE Employee_Name LIKE '{}%'".format(letter))
    record = cursor.fetchall()
    if len(record) == 0:
        print(f"Employee with name starting with {letter} does not exist in the table." )
    else:
        print("Employee details are: ")
        for row in record:
            print("\nEmployee_Name: ", row[0])
            print("Employee_Id: ", row[1])
            print("Salary: ", row[2])
            print("Department_Id: ", row[3])
            print("City: ", row[4])

letter = input("Enter the First letter of Employee: ")
print_details(letter)

# printing details as per Employee_Id
def emp_print_details(e_id):
    cursor.execute("SELECT * FROM Employee WHERE Employee_Id = {} ".format(e_id))
    record2 = cursor.fetchall()
    for row in record2:
        print("\nEmployee_Name: ", row[0])
        print("Employee_Id: ", row[1])
        print("Salary: ", row[2])
        print("Department_Id: ", row[3])
        print("City: ", row[4])

e_id = input("Enter the ID of Employee for printing employee details: ")
emp_print_details(e_id)

# changing name of employee whose ID inputted by user
def change_name(new_name,emp_id):
    cursor.execute("UPDATE Employee SET Employee_Name ='{}' WHERE Employee_Id ='{}' ".format(new_name,emp_id))

emp_id = input("Enter the ID of Employee whose name has to be changed: ")
new_name = input("Enter the new name of Employee: ")
change_name(new_name,emp_id)

# printing details of Employees in a department
d = 'y'
while d == 'y':
    dept_id = input("Enter the Department ID for which you need Employee details: ")
    cursor.execute("SELECT Department_Name FROM Departments WHERE Department_Id = {} ".format(dept_id))
    record3 = cursor.fetchone()
    print(f"\nEmployees Working in {record3[0]} are:")
    cursor.execute("SELECT E.Employee_Name, E.Employee_Id, E.Salary, E.City, E.Department_Id, D.Department_Name FROM EMPLOYEE E,Departments D WHERE E.Department_Id=:id AND D.Department_Id =:id ", {"id": dept_id})
    record3 = cursor.fetchall()
    print("Employee details are: ")
    for row in record3:
            print("\nEmployee_Name: ", row[0])
            print("Employee_Id: ", row[1])
            print("Salary: ", row[2])
            print("Department_Id: ", row[3])
            print("City: ", row[4])
    d = input("Do you want to Continue Y or N:")

conn.commit()
conn.close()





