def print_main_menu():
    print("----------------------------------------------\n")
    print("Press 1 to access a student\n")
    print("Press 0 to exit\n")
    print("----------------------------------------------\n")

def print_student_menu(user):
    print("----------------------------------------------\n")
    print("Welcome ", user.get_firstName(), "!\n")
    print("Press 1 to add a course\n")
    print("Press 2 to remove a course\n")
    print("Press 3 to view your schedule")
    print("Press 4 to go back\n")
    print("----------------------------------------------\n")

def print_instructor_menu(user):
    print("----------------------------------------------\n")
    print("Welcome ", user.get_firstName(), "!\n")
    print("Press 1 to view your schedule\n")
    print("Press 2 to veiw your roster\n")
    print("Press 3 to go back\n")
    print("----------------------------------------------\n")

def print_login_menu():
    print("----------------------------------------------\n")
    print("press 1 to sign in\n")
    print("press 2 to sign up\n")
    print("press 0 to exit\n")

def log_in(): #function takes in the user's credentials and returns the index to main
    username = input("Username: ")
    password = input("Password: ")
    for user in users:
        if user.username == username and user.password == password:
            return students.index(student)
    print("Incorrect Credentials")
    return -1 #returns failiure

def sign_up(): #function to sign up both students and instructors and return the indext to main
    if not users:                   #checks if the list is empty
        ID = 1000                   #starts IDs at 1000
    else:                           #if users is not empty
        ID = users[-1].get_ID() + 1 #gets the last ID for a user and adds the next ID
    studentOrInstructor = input("Press 1 for student and 2 for instructor: ")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    if studentOrInstructor == 1:
        major = input("major: ")
    username = input("Username: ")
    password1 = input ("Password: ")
    password2 = input("Retype Password: ")
    if password1 == password2:
        if studentOrInstructor == 1:
            newUser = classes.student(ID, fName, lName, username, password1, major)
        else:
            newUser = classes.instructor(ID, fName, lName, username, password1)
        users.append(newUser)
        return (users.len() - 1) #returns the last index
    else:
        print("The passwords do not match. Please try again.")
    return -1 #returns failiure
