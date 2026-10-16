# FOR LOOP:

# Write a program using for loop to print "Hello World"
# 5 times.

# for i in range(0, 5):   # 0, 1, 2, 3, 4
#     print("Hello World")

# Write a program to print 1 to 10 numbers
# using for loop.

# for num in range(1, 11):
#     print(num)


# write a program to print table of 7
# using for loop

# for i in range(1, 11):
#     print(i*7)

# Write a program to print all the English capital alphabets
# using for loop

# for ascii_code in range(65, 91):
#     print(chr(ascii_code), end=" ")

# Write a program to print all even numbers
# from bellow list
# l1 = [4, 1, 2, 3, 6, 5, 7, 8, 9, 99, 65, 76, 87, 23, 34]

# for num in l1:
#     if num % 2 == 0:
#         print(num)


# Write  a program to print all vowels from bellow string

# str1 = 'Apple are Sweet'

# for char in str1:
#     if char in "AEIOUaeiou":
#         print(char)
        

# Write a program to print all consonents 
# from bellow string

# str2 = "98fgieplka"


# Write a program to print even numbers in between 
# 123 to 156 which are divisible by 4

# for num in range(123, 156):
#     if num % 2 == 0:
#         if num % 4 == 0:
#             print(num)


# Write a program to find all special charecters from 
# bellow string

# str3 = "vsjw72894&$@"

# for char in str3:
#     if char.isalnum():
#         pass
#     else:
#         print(char)

# Write a program using for loop to print 
# prime numbers in between 1 to 100

for num in range(1, 100):
    flag = False
    for i in range(2, num//2):
        if num % i == 0:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        print(num)