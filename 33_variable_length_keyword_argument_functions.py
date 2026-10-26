# Variable Length Keyword Argument Functions:

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# student_info()
# student_info(45, "Vijay Hajare", "7th", "Pawar Madam", "Sushma Deshmukh")


student_info(roll_no=45, Fullname="Vijay Hajare", Standard="6th", class_teacher="Pawar Madam", favourate_friend="Anitha Reddy", last_year_marks=67)
