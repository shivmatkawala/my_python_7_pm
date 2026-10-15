# Write a program using while loop:
# To print Fibonacci series upto user defined length.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

# upto length 100 fibonacci series.

# num_of_nums = int(input("Enter length of fibonnaci series to be generated: "))

# num1 = 0
# num2 = 1
# count = 0
# print(num1)
# print(num2)
# while count < num_of_nums-2:
#     new = num1 +num2
#     print(new)
#     num1, num2 = num2, new
#     count+=1

#---------------------------------------

# Write a program to to get the Armstrong Numbers
# in between 100 and 10000
# using while loop.

# 153 => 1**3 + 5**3 + 3**3
#     => 1+125+27
#     => 153

# num = 100

# while num < 10000:
#     str_num = str(num)
#     power = len(str_num)   # 3
#     total = 0
#     indx = 0
#     while indx < power:
#         total+=(int(str_num[indx])**power)
#         indx+=1
#     if total == num:
#         print(num)
#     num+=1

#-------------------------- 
# Write a program to using while loop:
# to get the sum of only +ve odd number from below list

# l1 = ["A", 45, -90, 23, 87, -77, True, "Apple", 45.23, 90, -35]
# #45, 23, 87

# indx = 0
# total = 0
# while indx < len(l1):
#     if type(l1[indx]) == int:
#         if l1[indx] > 0 :
#             if l1[indx] % 2 != 0:
#                 total+=l1[indx]
#     indx+=1
# print(total)


#----------------------------------------------

# Write a program to print a dictionary of repeted charecters
# from bellow string:

str1 = "hgfjnjhgdhsjkdchdnbfdhcbxnefdjfhdnxmsn"

indx = 0
dict1 = {}

while indx < len(str1):
    dict1.update({str1[indx]: str1.count(str1[indx])})
    indx +=1
print(dict1)
