# LOOP:

# Why We need Loop:

# Write a program to greet.
# print("Hello Guys..!")


# Write a program to greet 5 times
# print("Hello Guys..!")
# print("Hello Guys..!")
# print("Hello Guys..!")
# print("Hello Guys..!")
# print("Hello Guys..!")


# Write a program to greet 10000 times

# for i in range(0, 10000):
#     print("Hello Guys..!")

#---------- Types of Loop:

    # while loop:
        # Manual Loop
        # It gives more control

    # for loop:
        # Automatic Loop
        # Very Less Control

#-------------------------------------------------

# While Loop:

# Write a program to print "Hello World" 5 times

# count = 0

# while count < 5:   #0, 1, 2, 3, 4, 
#     print("Hello World", count)
#     count +=1

# Write a program to print a table of 7

# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21

# count = 1

# while count <= 10:
#     print(f" 7 * {count} = {7*count}")
#     count +=1


# Write a program to print all even numbers in between 
# 21 and 37

# num = 21

# while num < 37:
#     if num % 2 == 0:
#         print(num)
#     num+=1

# Write a program to print all numbers which are divisible by
# 3 and 7 in between 1 and 100

# num = 1
# while num < 100:
#     if num % 3 == 0 and num % 7 == 0:
#         print(num)
#     num+=1

# Write a program to print greatest number from 
# bellow list

# numbers = [23, 1, 0, 56, 78, -34, 90, -120, 45]

# indx = 0
# greatest = None
# while indx < len(numbers):  #9
#     if indx == 0:
#         greatest = numbers[0]
#     if numbers[indx] > greatest:
#         greatest = numbers[indx]
#     indx+=1

# print(greatest)

#-------------------------------------------

# Write a program to print the factorial of a number. 5

# num = int(input("Enter a number: "))  # 5
# fact = 1
# while num >= 1:
#     fact *= num
#     num -=1
# print(fact)


