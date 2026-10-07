# LIST:
    # List is a collection datatype.
    # List is is hetrogeneous in nature
    # List is mutable
    # List is ordered
    # List supports Indexing
    # List is created/ initialized using [] and also list literal "list()"
    # List allows duplicates

#-----------------------------------------------
# list1 = []
# print(list1)
# print(type(list1))

# list2 = list()
# print(list2)
# print(type(list2))

# list3 = [1, 2.2, 3-4j, "Hello", True, [100, 200, 300]]
# print(list3)
# print(type(list3))

#-----------------------------------------------
# Indexing On List:

# l1 = [12, 23, 34, 45, 56, 78, 89, 90]
# print(l1[2])
# print(l1[-6])

# Nested Indexing:
# l2 = [1, 2.2, "PYTHON", True, [12, "Alpha", False]]
# print(l2[0])
# print(l2[3])
# print(l2[2])
# print(l2[2][2])
# print(l2[2][5])
# print(l2[-1][1][0])

#----------------------------------------------
# SLICING:
# print(l2[1:3])
# print(l2[3:0:-1])
# print(l2[-2:-5:-1])

#-----------------------------------
# Built-In Functions of List:

# l3 = [1, 2, 3]

    # insertion functions:
        # .append()
# l3.append(4)   #[1, 2, 3, 4]

        # .extend()
# l3.extend([4, 5, 6, 6, 6, 7])

        # .insert()
# l3.insert(0, 0)
# l3.insert(3, 5000)

    # deletion function:
        # .pop()
# l3.pop(6)
# l3.pop()

        # .remove()
# l3.remove(6)   # value

        # .clear()
# l3.clear()

    # searching functions:
        # .index()
# l4 = [12, "Hello", True, [1, 2, 3, 4]]
# print(l4.index(12))
# print(l4.index(True))
# print(l4.index([1, 2, 3, 4]))
# print(l4.index(3))

    # other methods:
        # .copy()
l5 = [1, 2, 3, 4, 5, 3, 7, 8, 3, 3, 0, 9, 3]

# l6 = l5.copy()   # shallow copy
# print(l6)
        # .count()
# print(l5.count(3))

        # .sort()
# l5.sort(reverse=True)
# print(l5)

        # .reverse()
# l5.reverse()
# print(l5)

# print(l3)

#----------------------------------------
# Some Other Operations on List:
    # Packing & Unpacking:
# x, y, z = [1, 2, 3]
# print(x)
# print(y)
# print(z)

    # List Concatination:

lis1 = [1, 2, 3, 4]
lis2 = [100, 200, 300, 400]
print(lis1 + lis2)

    # Repetation of List:
# ll1 = [1, 2, 3]
# print(ll1*5)

#----------------------- Some Intermediate Questions:

s1 = "Python Is Awesome"     # awesome is python
# print(s1[::-1])

# list_of_s1 = s1.split()
# list_of_s1.reverse()
# reversed_s1 = " ".join(list_of_s1)
# print(reversed_s1.lower())

#--------------------------------
str_num1 = '23'
str_num2 = '5'

# print(int(str_num1) * int(str_num2))

t1 = (1, 2, 3, 4)
# print(t1, type(t1))
l1 = list(t1)
print(l1, type(l1))