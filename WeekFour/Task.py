def greet(name):
    print("Hello", name)

greet("Mihret")

def add_numbers(x, y):
    return x + y
print(add_numbers(1,2))

def print_args(*args):
    for arg in args:
        print(arg)
print_args("Mihret","Tekalgn", "Hailemariam")        

def calculate_average(*args):
    sum = 0
    length = 0
    for arg in args:
        sum += arg
        length += 1
    return sum / length

print(calculate_average(1,2,3,4))
    

sum = lambda x, y : x + y
square = lambda x : x ** 2
isEven = lambda x : x % 2 == 0

print(sum(1,3))
print(square(9))
print(isEven(9))


nums = [1,2,3,4,5,6]
nums_filtered = list(filter(isEven, nums))
print(nums_filtered)

nums_mapped = list(map(lambda x : x * 2, nums))
print(nums_mapped)

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b: "))
    print(a + b)

except Exception as e: 
    print("Not Integers")


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b: "))   
    print(a/b)


except ZeroDivisionError as e: 
    print("B can not be 0")
except Exception as e:
    print("Not Integers")

    


