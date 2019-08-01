import classes
import sqlite3
from getpass import getpass

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
    print("Press 3 to view your schedule\n")
    print("Press 4 to log out\n")
    print("----------------------------------------------\n")

def print_instructor_menu(user):
    print("----------------------------------------------\n")
    print("Welcome ", user.get_firstName(), "!\n")
    print("Press 1 to view your schedule\n")
    print("Press 2 to veiw your roster\n")
    print("Press 3 to log out\n")
    print("----------------------------------------------\n")

def print_admin_menu():
    print("----------------------------------------------\n")
    print("Welcome Admin!\n")
    print("Press 1 to view all courses\n")
    print("Press 2 to view a specific instructors roster\n")
    print("Press 3 to add a course\n")
    print("Press 4 to remove a course\n")
    print("Press 5 to edit course attributes\n")
    print("Press 6 to force add a student to a course\n")
    print("Press 7 to force drop a student from a course\n")
    print("Press 8 to view all students\n")
    print("Press 9 to log out\n")
    print("----------------------------------------------\n")


def print_login_menu():
    print("----------------------------------------------\n")
    print("press 1 to sign in\n")
    print("press 2 to sign up\n")
    print("press 0 to exit\n")

def log_in(users): #function takes in the user's credentials and returns the index to main
    username = input("Username: ")
    password = getpass("Password: ")
    for user in users:
        if user.username == username and user.password == password:
            return users.index(user)
    print("Incorrect Credentials")
    return -1 #returns failiure

def sign_up(users): #function to sign up both students and instructors and return the indext to main
    if not users:                   #checks if the list is empty
        ID = 1000                   #starts IDs at 1000
    else:                           #if users is not empty
        ID = users[len(users) - 1].get_ID() + 1 #gets the last ID for a user and adds the next ID
    studentOrInstructor = input("Press 1 for student and 2 for instructor: ")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    if studentOrInstructor == '1':
        major = input("major: ")
    username = input("Username: ")
    password1 = getpass ("Password: ")
    password2 = getpass("Retype Password: ")
    if password1 == password2:
        if studentOrInstructor == '1':
            newUser = classes.student(ID, fName, lName, username, password1, major, 'freshman', 'none', 'none')
        else:
            newUser = classes.instructor(ID, fName, lName, username, password1, 'none')
        users.append(newUser)
        return (len(users) - 1) #returns the last index
    else:
        print("The passwords do not match. Please try again.")
    return -1 #returns failiure
