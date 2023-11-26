import sqlite3
from tabulate import tabulate

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

def createTable(name):
    sql = f"Create Table If not exists {name}(id Integer Primary Key, name Text,age Integer, grade Text)"
    cursor.execute(sql)

def addStudents():
    print("Add Students")
    name = input("Enter Name:")
    age = input("Enter Age:")
    grade = input("Enter Grade:")

    sql = "Insert Into students (name, age, grade) values (?, ?, ?)"
    data = (name, age, grade)
    cursor.execute(sql, data)

def displayAll():
    cursor.execute("Select * from students")
    columns = [i[0] for i in cursor.description]
    row = cursor.fetchall()
    table = tabulate(row, headers = columns, tablefmt = 'fancy_grid')
    print(table)


def search():
    n = input("Enter the Name of the Student you want to search:")
    sql = "Select * from students where name = ?"
    n = (n,)
    cursor.execute(sql,n)

    row = cursor.fetchall()
    for i in row:
        a,b,c,d = i
        print("Id:", a)
        print("Name:", b)
        print("Age:", c)
        print("Grade:", d)

def update():
    id = input("Enter the Id of the Student You want to update:")
    age = input('Enter age:')
    grade = input('Enter Grade:')
    sql = "Update students Set age = ?, grade = ? where id = ? "
    cursor.execute(sql, (age, grade, id))

def delete():
    id = input("Enter the Id you want to delete:")
    sql = "Delete from students where id = ?"
    cursor.execute(sql, (id,))
def menu():
    print("===============Welcome===========")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    n = input("Choose:")
    if n == "1":
        addStudents()
    elif n == "2":
        search()
    elif n == "3":
        displayAll()
    elif n == "4":
        delete()
    elif n == "5":
        update()
    elif n == "6":
        exit()
    else:
        y = input("Choose the correct number. If you want to continue press y else any: ")
        y = y.lower()
        if y == 'y':
            menu()
        else:
            exit()
    menu()
createTable("students")
menu()



connection.commit()
cursor.close()
connection.close()