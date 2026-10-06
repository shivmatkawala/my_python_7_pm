# String Built In Methods:

    # Case Conversion Methods:
        # .upper()
# str1 = "hello world 123 @ HYDERABAD"
# print(str1.upper())   #HELLO WORLD 123 @ HYDERABAD

        # .lower()
# print(str1.lower())   #hello world 123 @ hyderabad

        # .capitalize()
# print(str1.capitalize())  #Hello world 123 @ hyderabad

        # .title()
# print(str1.title())   #Hello World 123 @ Hyderabad

        # .swapcase()
# print(str1.swapcase())  #HELLO WORLD 123 @ hyderabad

    # Search and find Methods:
        # .index()
str2 = "PYTHON IS GREAT"
# print(str2.index("P")) #0
# print(str2.index("T")) #2
# print(str2.index("Z"))   #ValueError: substring not found

        # .rindex()
# print(str2.rindex("T")) #14
# print(str2.rindex("S"))

        # .find()
# print(str2.find("P"))
# print(str2.find("T"))
# print(str2.find("Z"))   #-1

        # .rfind()
# print(str2.rfind("T"))
# print(str2.rfind("P"))
# print(str2.rfind("Z"))

    # is Methods:
        # .isalpha()
str3 = "applesaresweet"
# print(str3.isalpha())   # only alphabets

        # .isdigit()
str4 = "1234567890"
# print(str4.isdigit())

        # .isalnum()
str5 = "123ALPHA"
# print(str5.isalnum())   # only alphabetic or numeric or alphabetic cum numeric

        # .isspace()
str6 = "        "
# print(str6.isspace())


    # Other Methods:
        # .split()     # on the provided separator it will cut the string and create list of pieces
str7 = "PYTHON IS GREAT LANGUAGE"
# print(str7.split(" "))  #['PYTHON', 'IS', 'GREAT', 'LANGUAGE']
# print(str7.split("T"))
# print(str7.split(""))  #ValueError: empty separator


        # .strip()        # Remove left and right side empty spaces
str8 = "   Hari is Awesome  "
print(str8)
print(str8.strip())


        # .lstrip()   # Removes left side empty space
print(str8.lstrip())

        # .rstrip()   # Removes right side empty space
print(str8.rstrip())
