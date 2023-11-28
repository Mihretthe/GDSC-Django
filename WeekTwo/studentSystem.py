from tabulate import tabulate

students = {}

def addStudents():
    name = input("Enter Name:").strip()
    age = input("Enter Age:").strip()
    grade = input("Enter Grade:").strip()
    students[name] = [name, age, grade]
def view(name):
    if name in students:
        return students[name]
    return "No one with this name"
def listAll():
    columns = ["Name","Age","Grade"]
    row = [values for values in students.values()]
    table = tabulate(row, headers = columns, tablefmt= "fancy_grid")
    print(table)
def update(name):
    if name in students:
        n = input("Enter Name:")
        a = input("Enter Age:")
        g = input("Enter Grade:")    
        if n.strip() != "":
            students[name][0] = n
        if a.strip() != "":
            students[name][1] = a
        if g.strip() != "":
            students[name][2] = g
    else:
        print("No data with this name")
def delete(name):
    if name in students:
        del students[name]

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
        name = input("Enter Name:").strip()
        view(name)
    elif n == "3":
        listAll()
    elif n == "4":
        name = input("Enter Name:").strip()
        delete(name)
    elif n == "5":
        name = input("Enter Name:").strip()
        update(name)
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

menu()
    

    
