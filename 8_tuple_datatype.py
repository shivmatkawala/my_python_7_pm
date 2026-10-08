# Tuple:
    # Tuple is collectin datatype
    # Tuple is heterogenous
    # Tuple is Ordered
    # Tuple supports Indexing
    # Tuple  allows duplicates
    # Tuple is created / Initialized using () and tuple() literal.
    # Tuple is Immutable

#-------------------Create Tuple:
tup1 = ()
# print(tup1)
# print(type(tup1))

tup2 = (1, 2, 3, 4)
# print(type(tup2))
# print(tup2)

tup3 = (1, 2.2, 3+5j, False, [11, 22, 33], ("A", "B"))
# print(tup3)
# print(type(tup3))

#--------- Tuple Indexing:
# print(tup3[2])
# print(tup3[4])
# print(tup3[-3])
# print(tup3[-2][-2])

#----------- Slicing:
# print(tup3[1:4:1][::-1])

#--------------- Built In Methods:
    # .index()   # Returns Index of element
    # .count()   #  Count of total appearances of element

tup4 = (3, 2, 3, 3, 4, 5, 6, 3, 5, 3, 1)
# print(tup4.count(3))
# print(tup4.index(5))