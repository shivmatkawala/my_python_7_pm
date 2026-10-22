file = open("./data/ecommerce.txt", "w")
file.write("Hello from mars..!")
file.close()

file2 = open("./data/maintenance.txt", "w")
file2.writelines(["This is building maintenance department\n", "We are working at aparna buildings cyberabad\n", "if there is any problem related buildings please let us know"])
file2.close()


file3 = open("./data/ecommerce.txt", "w")
file3.write("Woww.. This is awesome.")
file3.close()

file4 = open("./data/ecommerce.txt", "a")
file4.write("\nThis is third line..")
file4.close()


file5 = open("./data/maintenance.txt", "r")
content = file5.read()
# print(content)
file5.close()


# file6 = open("./data/maintenance.txt", "+r")
# file6.write("\nThis is fourth line\n")
# con = file6.read()
# print(con)

# file7 = open("./data/mycode.py", "w")
# file7.write("print('Hello World')")
# file7.close()


