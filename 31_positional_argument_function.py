# Positional Argument Functions:

def signup(firstname, lastname, email, dob, contact, password, cnf_password):
    print(f"""
            Fullname: {firstname + " " + lastname}
            Email: {email}
            Phone: {contact}
            DOB: {dob}
            Password: {password}
            Confirm Password: {cnf_password}
            """)


# signup("12/4/2026", "kumar@gmail.com", "Shiv@123", "+91 6788909023", "Shiv@123", "Siva", "Kumaran")

signup("Siva", "Kumaran", "kumar@gmail.com", "14/2/2024", "+91 6789899034", "Shiv@123", "Shiv@123")
