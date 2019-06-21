from getpass import getpass

class admin:
    def __init__(self, u, p):
        self.username = u 
        self.password = p
    def set_username(self, u):
        self.username = u
    def set_password(self, p):
        self.password = p
    def viewallcourses(self):
        print("---All Courses---")
     
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
    print("----------------------------------------------\n")

def log_in_admin():
    admin("admin","12345")
    username = input("Username: ")
    password = getpass("Password: ")
    if username == "admin" and password == '12345':
        print_admin_menu()
    else:
        print("inva;id username or password")
    menu_choice = " "
    if menu_choice == 1:
        #print all available courses
    elif menu_choice == 2:
        #select an instructor
        #print roster
    elif menu_choice == 3:
        #add a course including attributes
    elif menu_choice == 4:
        #print courses
        #select course and remove
    elif menu_choice == 5:
        #choose course and edit its information
    elif menu_choice == 6:
        #select a course 
        #select a student
        #append student to class (this needs to override capacity which is set to 25 )
    elif menu_choice == 7:
        #select course
        #select student and remove from said class
    else:
        print("Invalid Input")
    

    
