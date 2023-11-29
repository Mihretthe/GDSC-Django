def menu():
    print("1. Length of the First Name")
    print("2. Make it Uppercase and print it")
    print("3. Check if the full name contains smith")
    print("4. Exit")
    choose = int(input())
    if choose == 1:
        print(length(fname))
    elif choose == 2:
        print(capital(fname, lname))
    elif choose == 3:
        print(checkSmith(fname, lname))
    else:
        exit()
    menu()

def length(name):
    return len(name)
def capital(fname, lname):
    return fname.upper() + lname.upper()
def checkSmith(fname, lname):
    s = fname +" " + lname
    s.lower()
    if "smith" in s:
        return "Smith is here"
    return "No Smith"
print("==============Welcome=========")
fname = input("Enter First Name:")
lname = input("Enter Last Name:")
menu()