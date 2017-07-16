# Computer Science Sample Coursework #
# Mainul Sarder #
# L33m4n Beta #

# Log-in credentials #
username = "leeman"
password = "password"
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Log-in system #
username_input = input("Enter the username: ")
password_input = input("Enter the password: ")
while username_input != username:
    print("Incorrect credentials. Try again.")
    username_input = input("Enter te username: ")
    password_input = input("Enter the password: ")
    while password_input != password:
        print("Incorrect credentials. Try again.")
        username_input = input("Enter the username: ")
        password_input = input("Enter the password: ")
print("Logged in.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# First Menu Options #
print("Option 1: Display student emails.")
print("Option 2: Display student addresses.")
print("Option 3: Displau student phones.")
print("Option 4: Display student date of birth.")
print("Option 5: Display student ID numbers.")
print("Option 6: Display student genders.")
print("Option 7: Display student tutor group.")
print("Option 8: Enter new student details.")
print("Option 9: Log out.")
user_choice = int(input("Enter the desired option: "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Functions #
def emails():
    file = open("database.txt", "r")
    for line in file:
        if "Email" in line:
            print(line)
def addresses():
    file = open("database.txt","r")
    for line in file:
        if "Address" in line:
            print(line)
def phones():
    file = open("database.txt","r")
    for line in file:
        if "Phone" in line:
            print(line)
def dob():
    file = open("database.txt","r")
    for line in file:
        if "DOB" in line:
            print(line)
def studentID():
    file = open("database.txt","r")
    for line in file:
        if "ID" in line:
            print(line)
def gender():
    file = open("database.txt","r")
    for line in file:
        if "Gender" in line:
            print(line)
def tutor():
    file = open("database.txt","r")
    for line in file:
        if "Form" in line:
            print(line)
def new_student():
    new_name = input("Enter student's full name: ")
    new_email = input("Enter student's email: ")
    new_address = input("Enter student's address: ")
    new_phone = input("Enter student's phone: ")
    new_dob = input("Enter the student's date of birth (dd/mm/yy): ")
    new_gender = input("Enter the student's gender: ")
    new_form = input("Enter the student's form: ")
    file = open("database.txt", "a")
    file.write ("\n")
    file.write (new_name)
    file.write (" - Email: ")
    file.write (new_email)
    file.write ("\n")
    file.write (new_name)
    file.write (" - Address: ")
    file.write (new_address)
    file.write ("\n")
    file.write (new_name)
    file.write (" - Phone: ")
    file.write (new_phone)
    file.write ("\n")
    file.write (new_name)
    file.write (" - DOB: ")
    file.write (new_dob)
    file.write ("\n")
    file.write (new_name)
    file.write (" - Gender: ")
    file.write (new_gender)
    file.write ("\n")
    file.write (new_name)
    file.write (" - Form: ")
    file.write (new_form)
    print("Student added.")

def logout():
    print("Goodbye.")

# Executing options #
if user_choice == int(1):
    emails()
elif user_choice == int(2):
    addresses()
elif user_choice == int(3):
    phones()
elif user_choice == int(4):
    dob()
elif user_choice == int(5):
    studentID()
elif user_choice == int(6):
    gender()
elif user_choice == int(7):
    tutor()
elif user_choice == int(8):
    new_student()
elif user_choice == int(9):
    logout()
