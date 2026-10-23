# Error & Exception:

# Write a program to multiply 2 different numbers:

# num1 = int(input("Enter Number1: "))
# num2 = int(input("Enter Number2: "))
# print(f"Product of {num1} and {num2} is: {num1*num2}")


#----------------------------- Different Types of Errors:
#  print("Hello World") IndentationError: unexpected indent
# print(1+"7") TypeError: unsupported operand type(s) for +: 'int' and 'str'
# PRINT("HEllo World") NameError: name 'PRINT' is not defined
# print([1, 2, 3][7]) IndexError: list index out of range
# for i in range(1, 11)   SyntaxError: expected ':
# print(6/0) ZeroDivisionError: division by zero

#----------------------------------------------------

# Write a program to multiply 2 different numbers:

# try:
#     num1 = int(input("Enter Number1: "))
#     num2 = int(input("Enter Number2: "))
# except ValueError:
#     print("Not a Number.. Please enter a number.")
# else:
#     print(f"Product of {num1} and {num2} is: {num1*num2}")
# finally:
#     print("Program successfully Completed")


# Write a program where user asks to enter numerator 
# and denominator, and performs true division
# import time
# start = time.perf_counter()
# try:
#     numerator = eval(input("Enter a numerator: "))
#     denominator = eval(input("Enter a denominator: "))
#     ans = numerator/denominator
# except NameError:
#     print("Please Enter only Numbers.")
# except SyntaxError:
#     print("Please Enter Numbers with no special charecters or alphabets.")
# except ZeroDivisionError:
#     print("Please do not provide 0 as denominator.")
# else:
#     print(f"True Division of {numerator}/{denominator}: {ans:.2f}")
# finally:
#     print("Program completed Successfully")
#     end = time.perf_counter()
#     print(f"{end-start:.2f} Seconds it took to complete the program.")

# # NameError, SyntaxError, ZeroDivisionError

#-----------------------------------

# Exception:

# Write a program to check eligibility of marriage:

# Country, Gender, age
class NegativeAgeError(Exception):
    pass

class GenderError(Exception):
    pass

try:
    country = input("Enter country: ")
    gender = input("Enter gender: ")
    age = int(input("enter age: "))

    ans = None
    if country.title() == "India":
        if gender[0].lower() not in "mf":
            raise GenderError("Must Enter only Male or Female as gender")
        elif gender[0].lower() == "m":
            if age < 0:
                raise NegativeAgeError("Must enter positive age.")
            elif age >= 22:
                ans ="Eligible" 
            else:
                ans = "Not Eligible"
        elif gender[0].lower() == "f":
            if age < 0:
                raise NegativeAgeError("Must enter positive age.")
            if age >= 18:
                ans = "Eligible"
            else:
                ans = "Not Eligible"
        
    else:
        ans = "We dont know oversease citizens age criteria for marriage. thanks..!"
                    
except ValueError:
    print("Enter Numeric age value.")
except GenderError:
    print("Gender mut be Male or Female only.")
except NegativeAgeError:
    print("Age cant be Negative.")
else:
    print(ans)
finally:
    print("Program completed..!")
