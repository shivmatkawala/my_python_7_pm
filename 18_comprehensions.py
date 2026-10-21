# Comprehension:
    # It is a single line expression.
    # used to create a collection.

# Types of Comprehension:
    # List Comprehension
    # Tuple Comprehension (Generator)
    # Set Comprehension
    # Dictionary Comprehension

# List Comprehension:
    # It creates a list collection.

# Write a list comprehension to get the table of 3
# 3, 6, 9, 12, 15, 18, 21, 24, 27, 30

# table_of_3 = [num* 3 for num in range(1, 11)]
# print(table_of_3)

# Write a list comprehension to to get alist of all
# those numbers which are divisible 3 and 7 in between 
# of 1 and 100

# nums_divisible_by_3_and_7 = [num for num in range(1, 100) if num % 3 ==0 and num % 7 == 0]
# print(nums_divisible_by_3_and_7)

# Write a list comprehension to get the vowels from string

# str1 = "ApleTuqeNOlS34*&"
# vowels = [char for char in str1 if char.lower() in "aeiou"]
# print(vowels)

# Write a list comprehension to get the list of
# all those strings which are less than 5 charecters.
# str_list = ["Apple", "Bob", "Grapes", "Cat", "Lucky", "Ramallah", "Davidoff"]
# small_strings = [string for string in str_list if len(string) < 5]
# print(small_strings)

# Write a list comprehension to get the list of those
# numbers which are odd negative from bellow tupple

# tup1 = (23, 90, -56, -22, -1, -7, 6, 0, -33)

# odd_negatives = [num for num in tup1 if num < 0 and num % 2 != 0]
# print(odd_negatives)

# Write a list comprehension to get those words 
# which do contain special charecters from bellow string.

# str2 = "Apple Bana$na Hell*o Dav&id cat6Rina Mallick Ti@er"

# sp_words = [word for word in str2.split(" ") if not(word.isalnum())]
# print(sp_words)

# print(not("Bana%na".isalnum()))

#-------------------- Tuple Comprehension (Generator)

# Write a tuple comprehension to get the all even numbers
# in between a and 10000
# odd_nums = (num for num in range(1, 10000) if num % 2 == 0)
# # print(odd_nums)

# for n in odd_nums:
#     print(n)


#------------------ Set Comprehension:
# Using set comprehnsion get all consonents from 
# bellow string 
# str3 = "sdfghj iyg^&UHbnvcdghi jdiejesojoenebw wehdwiudqiGUY"
# unique_consonents = {char for char in str3 if char.lower() not in "aeiou" and char.isalpha()}
# print(unique_consonents)


#---------------------- Dict Comprehension:
# Write a dictionary comprehension which will get 1 to 10 numbers
# as keys and  there cubes as values.

# cubes = {num:num**3 for num in range(1, 11)}
# print(cubes)

