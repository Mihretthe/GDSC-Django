sum = 0
count = 0

for i in range(1, 51):
    if i % 2 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print("Three, Five") 
            count += 1           
        elif i % 3 == 0:
            print("Three")
            count += 1  
        elif i % 5 == 0:
            print("Five")
            count += 1  
        sum += i
print(f"Total sum = {sum}, and The count of numbers replaced = {count}")


