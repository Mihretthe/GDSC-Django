s = input("Please enter the word: ")
if s == s[::-1]:
    print(f"The word {s} is a palindrome.")
else:
    print(f"The word {s} is not a palindrome,\nbecause {s[::-1]} is not equal to {s}.")