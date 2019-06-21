class instructor():
    def __init__(self, ID, f, l, u, p):
        self.ID = ID
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p
    def set_username(self, u):
        self.username = u
    

students = ['Mike','Sally','Nick']       #hard coding students even though I dont use it in the code
courses = ['Math', 'English', 'Science']  # also hardcoding the courses that can be selected for the student and professor

'''
Mike signs up for math and Sally but Nick does not sign up for Math class
Nick sign up for English and Science
'''

def print_menu():
    print("\n1. View courses\n")      #This is the menu for when the instructor properly entered in their credentials
    print("2. Print Roster\n")




def instructor_function():
    new_instructor = instructor("1045", "Aaron", "Carepenter", "acarp1", "abcd123")  #hardcoded the instructor information
    username = input("Username: \n")
    password = input("Password: \n")
    i = 0
    while True:
        if username == new_instructor.username and password == new_instructor.password:
            print_menu()
            break
        else:
            print("Invalid Input, Please try again") 
        i+=1
        if(i<3):
            break
    choice = int(input(""))
    if choice == 1:
        print(courses)
    elif choice == 2:
        print("blah blah blah")
        #student has signed up for a course which has been assinged to an instructor 
        #the instructor is also teaching a class that has students 
        #using this information we can make it so that the inctructor gets the kids that are for his class. 
 
instructor_function()
