# Range:
    # It is a collection datatype
    # It generates sequential numbers on runtime
    # Range is memory friendly
    # Range is also immutable
    # Range always requires [start: end: step]
    # Range is homogenous
    # It is ordered datatype
    # It supports Indexing
    # Alwasy Range created using range()
#------------------------------------
r1 = range(5)  #range(0, 5)  default start = 0, default step =1
# print(r1)
# print(type(r1))

r2 = range(100, 1000)
# print(r2)
# print(type(r2))

r3 = range(5, 50, 5)
# print(r3)
# print(type(r3))

#-------------- Typecasting
# l1 = list(range(1, 10))
# print(l1)

# t1 = tuple(range(5, 50, 5))
# print(t1)

# s1 = set(range(23, 45, 3))
# print(s1)
#---------------------------------------------------
r11 = range(123, 520, 10)
# print(r11[3])
# print(list(r11[5:10:2]))
#-------------------------------------------------