character = input("Please enter the pattern to be printed: ")
vowels = "aeiouAEIOU"

i = 1

while i <= 9:
    if character in vowels:
        print("Vowels are not allowed in the input.")
        break
    elif len(character) > 1:
        print("The length of character should be 1.")
        break
    print(character * i)
    i += 2
