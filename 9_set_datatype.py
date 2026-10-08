# Set:
    # It is a collecction datatype.
    # It is mutable
    # It is partially heterogenous () allows only immutable elements inside it.
    # It is unordered
    # It doesnt support Indexing
    # It doesnt allow duplicates.
    # It is created using {} or set() literal

#-----------------Create Set:
set1 = {1}
# print(set1)
# print(type(set1))

set2 = {1, 2.2, 3-4j, True, "Hello", (1, 2, 3)}
# print(set2)
# print(type(set2))

set3 = set()
# print(set3)
# print(type(set3))

#--------------- 
s1 = {1, 2, 3, 4, 52, 3, 4}
# print(s1)

s2 = {22, "Hello", False, (1, 2, 3), 0.01}
# print(s2)

#-----------------------------------------
# Set Basic Operations:

# Union |:
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# print(s1.union(s2))
# print(s1 | s2)

# Differece -:
# print(s1.difference(s2))
# print(s1-s2)

# print(s2.difference(s1))
# print(s2-s1)

# Intersection &:
# print(s1.intersection(s2))
# print(s1 & s2)

#------------------------------
s1 = {1, 2, 3}
# s1.update({4, 5})
# s1.update([6, 7])
# s1.update((9, 10))
# s1.update("ABC")
# print(s1)

#--------------------------------

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# update s1 with with its difference of s2
# s1.difference_update(s2)   #1, 2, 3
# s2.difference_update(s1)   #4, 5, 6, 7, 8

# s1.intersection_update(s2)   #4, 5
# s2.intersection_update(s1)   #4, 5

# print(s1)  
# print(s2)  

#-----------------------------
# s1.add(100)
# del s1

# print(s1)

#------------------- Subset and Superset:

aet1 = {1, 2, 3, 4, 5}  # Superset of aet2
aet2 = {1, 2}      #  Subset of aet1

# print(aet1.issuperset(aet2))
# print(aet2.issubset(aet1))