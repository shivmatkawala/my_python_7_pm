# Nested Condtions:

# Write a program where you ask user to enter a number
# fram a range of -10 to 10.
# And you will display what type of number is this.

# -3 => -ve Number, Odd Number
# 4  => +ve Number, Even Number
# 0  => Even Number

# number = int(input("Enter a number: "))

# if number > 0:
#     print("+ve Number")
#     if number % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# elif number < 0:
#     print("-ve Number")
#     if number % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# else:
#     print("Zero, And Even Number")

#-------------------------------------------------------

# Write a program where you ask user to enter a English 
# Charecter.
# Display what type of charecter is this.

# A => Alphabet, Upper, Vowel
# d => Alphabet, Lower, Consonent
# 5 => Number, +ve, Odd
# & => Special Charecter

# char = input("Enter Charecter: ")

# if char.isalpha():
#     print("Alphabet")
#     if char.isupper():
#         print("Upper")
#         if char in "AEIOU":
#             print("Vowel")
#         else:
#             print("Consonent")
#     else:
#         print("Lower")
#         if char in "aeiou":
#             print("Vowel")
#         else:
#             print("Consonent")

# elif (len(char) == 1 and char.isdigit()) or (len(char) > 1 and not(char[0].isdigit()) and char[1::].isdigit()) or (char.isdigit()):
#     print("Number")
#     if int(char) > 0:
#         print("+ve")
#         if int(char) % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#     elif int(char) < 0:
#         print("-ve")
#         if int(char) % 2 == 0:
#             print("Even")
#         else:
#             print("odd")
#     else:
#         print("Zero, Even")

# else:
#     print("Special Charecter")


#----------------------------------------------------------
