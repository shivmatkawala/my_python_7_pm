# Dictionary:
    # It is also a collection datatype
    # We can store pairs of key and value
    # Dictionary is unordered
    # Dictionary can be indexed using its "Keys"
    # Dictionray is created using {} or dict() literal
    # Dictionary can allow duplicate values but dont alllow duplicate keys
    # Dictionary is mutable
    # Dictionary is heterogeneous
#----------------------------------------------
# Create Dict:

dict1 = {}
# print(dict1)
# print(type(dict1))

dict2 = dict()
# print(dict2)
# print(type(dict2))

# dict3 = {"A": 65, "B": 66, "C": 67, "D": 68}
# dict4 = {1:1, 2:4, 3:9, 4:16, 5:25}
# dict5 = {"Ravi": 70, "Sanjana": 90, "Kirthana": 50, "Krishna": 95}
# dict6 = {1:"Odd", 2:"Even", 3:"Odd", 4:"Even"}
# print(f"{dict3}\n{dict4}\n{dict5}\n{dict6}")

dict7 = {
    "Chemistry": 50,
    "Physics":80,
    "Mathematics": 40
}
# print(dict7)
# print(type(dict7))


# dict8 = {
#     "Paremshwar": ["Male", "Bsc", "Karnataka", "Farmer", "Data Analytics"],
#     "Swara": (12, 23, 34, 45),
#     "Gajanan": {1, True, "Hello"}
# }
# print(dict8)
# print(type(dict8))

dict9 = {
    "Rama": {"City": "Bidar", "State": "Karnataka", "Qualification": "Bsc"},
    "Vidya":{"Fav_heros":["Parmeshwar", "Akshay", "Nani"], "fav_food": ["A", "B"]}
}

# print(dict9)
# print(type(dict9))

#--------------------------------------------------------
# Dictionary Value acces:

dict10 = {
    "Apple": "Fruit",
    "Hyderabad": "City", 
    "Samntha":"Model", 
    "Parmeshwar": "Hero"
}

# How to access values:
# print(dict10["Apple"])
# print(dict10["Parmeshwar"])
# print(dict10["Hyderabad"])
# print(dict10["Samntha"])

# dict10["Iphone"] = "Mobile"
# dict10["Hyderabad"] = "Metro Ciry"

# print(dict10.get("Samntha"))  # Safe (returns None if key is not there)
# print(dict10["Samantha"])     # Not safe (throws error if key is not there)

# print(dict10)

#-----------------------------------------
students = ["Ajay", "Swara", "Arti", "Bhavani"]
marks = [60, 70, 40, 90]

# students_marks = dict(zip(students, marks))
# print(students_marks)

#-----------------------------------

students = ["Ajay", "Swara", "Arti", "Bhavani"]
studets_result = dict.fromkeys(students, "Fail")
# print(studets_result)

#-------------------------------------------------

# IN-Built Methods of Dictionary:

dict11 = {
    "Apple": "Kasmir",
    "Banana": "Nashik",
    "Grapes": "Tirupati",
    "Avocado": "America",
    "Dragon Fruit": "China"
}

# print(list(dict11.keys()))
# print(list(dict11.values()))
# print(list(dict11.items()))
#-------------------------------------------

dict11.update({"Papaya": "Asam", "Kaju": "Goa", "Coffee": "Karnataka"})

# dict11.pop("Banana")
# dict11.popitem()
# dict11.clear()

# dict12 = dict11.copy()
# dict11.setdefault("Papaya", "Himachal")
#---------------------------------------------

# dict13 = {"Papaya": "Asam"}
# dict13.setdefault("Papaya", "Himachal")
# print(dict13)