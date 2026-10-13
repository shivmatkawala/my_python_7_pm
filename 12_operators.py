# Expression:
            # Operators and Operands
            # Operator => Defines operation type
            # Operands => Elements upon which operation is gonna performed.

            # Ex: 6 * 5 = 30  
            # Ex: a / b = 3

# ------------------------------------
# Operators:
        # Arithmetic Operators:  [INT, FLOAT, COMPLEX, BOOL]
x = 5
y = 3
            # Addition +
# print(f"Addition: {x+y}")

            # Substraction -
# print(f"Subbstraction: {x-y}")

            # Multiplication *
# print(f"Multiplication: {x*y}")

            # True Divide /
# print(f"True Division: {x / y}")

            # Floor Divide //
# print(f"Floor Division: {x//y}")

            # Exponentiation (Power) **
# print(f"Power: {x ** y}")

            # Modulus %
# print(f"Mod: {x % y}")

        # Assignment Operators:
            # Assign =
# num1 = 34
            # Add and Assign +=
# num1 = num1 + 6
# num1+=6
            # Substract and Assign -=
# num1 = num1-10
# num1-=10
            # Multiply and Assign *=
# num1 = num1 * 5
# num1*=5
            # True Divide and Assign /=
# num1 = num1 / 7
# num1 /=7
            # Floor Divide and Assign //=
# num1 = num1 // 7
# num1//=7
            # Power and Assign **=
# num1 = num1 ** 3
# num1 **= 3
            # Mod and Assign %=
# num1  = num1 % 200
# num1 %= 200

# print(num1)
        # Comparision Operators:  (Returns Bool)
a = 45
b = 30
c = 23

            # Greater than >
# print(a > b)
# print(b > c)
# print(c > a)
# print(a > b > c)
# print(a < b > c)

            # Lesser than <
# print(a> b < c)
# print(c < b > a)

            # Equal to ==
# print(a == b == c)
# print((b+c) == a > b)

            # Not Equal to !=
# print(a != b > c)

            # Greater than or Equal to >=  
# print(a >= b > c)

            # Lees than or Equal to <=
# print(b <= a < c)
            

        # Membership Operators:
str1 = "DFGHHduyejdghjewyuikndbnsmshyeuh38euyh"

            # in
# print("z" in str1)
# print("m" in str1)
# print("ndb" in str1)

s1 = {1, 5, 2, 4, 0, 8, 1, 3}
# print(False in s1)
# print(True in s1)
# print(12 in s1)

            # not in
# print(False not in s1)
# print(1 not in s1)
# print(11 not in s1)

        # Identity Operators:
                # is
        
                # is not
# x = [1, 2, 3]
# y = x

# print(id(x))
# print(id(y))
# print(x is y)

# x = [1, 2, 3]

# y = x.copy()
# print(x, y)
# print(id(x))
# print(id(y))
# print(x is y)

        # Logical Operators:
            # and
# print(True and True and True)
# print(True and True and True and False)
# print(False and False and False)

            # or
# print(True or True or True)
# print(True or True or True or False)
# print(False or False or True)

            # not
# print(not(True) and (False - False) or (True -True) and False and not(True))

        # Ternary Operators:
                # Single Line Expressions.
                # Faster
                # To get conditional output
# Write a program to print the meaning of users favourate
# primary color:
# Primary: Red Blue Green
                # Red => Sacrifice
                # Blue => Peace
                # Green => Nature

# fav_prim_color = input("Enter your favourate primary color: ")
# result = "Sacrifice" if fav_prim_color == "Red" else "Peace" if fav_prim_color == "Blue" else "Nature" if fav_prim_color == "Green" else "Invalid color"
# print(result)

            # if
            # else

        # Bitwise Operators:
            # &   (AND)
            # |   (OR)
            # ^   (XOR)
# x = 25   # 11001
# y = 35   # 100011

# print(x & y)  #34
# print(25 | 35)
# print(25 ^ 35)

# print(bin(59))
# print(int("111011", 2))
