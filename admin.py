from getpass import getpass #this module allows you to hide a password which would be useful for an admin

'''
Coded by Matthew Alves
This is a barebones python file where the functions are hardcoded to test functionality and use cases.
One thing to note is that many of the input arguments are asking for a number associated with a 
course, student, and eventually instructor because in my opinion it is easier to look for an indexed 
number in a list/array than it is to enter in a word as typing is much more prone to errors. What do I mean by this?

For example, the admin function to remove a course asks for the indexed number associated with said course
[0 = Math, 1 = English, 2 = ?, ..., N = ?] This will be changed to course CRN later on (look at Ralphs 'class course' 
for futher info) Once the user chooses a number, the remove keyword can handle the rest. This is easier 
than typing out the course title and checking to see if that course title is in the global list, and then 
removing it.

Other thing to note is that since an admin can write to lists, updating a students schedule can effect an instructors
rosters therefore these cases need to be accounted for and hanngled
'''

#basic course with CRN parameter to test creating a course
#Courses will need more attributes (See Raplh's classes.py line 1)
class course:
    def __init__(self, CRN):
        self.CRN = CRN #course CRNs are always made of 6 characters
        
#I have decided to make admin simple by creating a username and password
#attribute. There is only one admin, so no need to overcomplicate its
#attributes
class admin: #note it does not inherit from user
    def __init__(self, u, p):
        self.username = u 
        self.password = p
    def set_username(self, u):
        self.username = u
    def set_password(self, p):
        self.password = p
    def get_user_type(self): #To distinguish from other types of users in Main (See main.py line 39 (subject to change))
        return "admin"
    '''
    Need to populate admin functions here to help streamline code!
    '''
#simple print function that outlines evetyhing that an admin can do
#Refer to Use-Case diagram for help
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
    print("Press 8 to exit")
    print("----------------------------------------------\n")
'''
Three lists to help test admin functionality.
Need to talk to Ralph and Akshar about how they are structing their 
lists in their classes. Reading, Writing, and appedning theses lists 
are critical for complete effiecency of the program!
Also, students, courses, and instructors have more attributes (see classes.py)
'''
students = ["Jim","Pam"] 
courses = ["Math","English"]
instructors = ["Professor Scott", "Professor Schrute"]

#admin function that will need to get called in main (see main.py line 40 (subject to change))
def admin_test():
    admin("admin","12345") #create an admin object where the username is admin and password is 12345
    i = 0 
    while(True):
        username = input("Username: ")
        password = getpass("Password: ") #getpass function allows us to hide the password when typing it in
        if username == "admin" and password == '12345': #The username and password that that the admin enters must equal the predeifned username and password
            print_admin_menu() #print all that an admin can do
            break 
        else: #otherwise, you entered either the username or password wrong
            print("invalid username or password")
        i+=1        #lines 65,66,74-76 is written to give the admin 3 tries to enter in a correct username and password before exiting
        if(i > 2):
            break
        '''
        if the admin exceeds the number of attempts, what happens? locked out? 
        '''    
    menu_choice = int(input("Please enter an option: "))
    if menu_choice == 1:
        #print all the courses avaliable to students
        for index in range(len(courses)):
            print(index, courses[index])
            
    elif menu_choice == 2:
        #print all the courses
        for index in range(len(instructors)):
            print(index, instructors[index])
        #admin chooses which instructor he wants to view
        print("\nWhich instructor's roster would you like to view?\n")
        choice = int(input("Please enter in the number associated with the instructor: "))
        for index in range(len(instructors)):
            if choice == instructors[index]:
                print("blank") #need link the instructors class 
   
    elif menu_choice == 3:
        print("Courses need\n[1] a 6-digit CRN \n[2] a title \n[3] Description of the course \n[4] space avaliable/25 \n[5] The schedule times\n")
        #try and except is for error catching
        try:
            CRN = int(input("Please specify a CRN: "))
            #Need to check length of CRN, and wheter or not it has been already created
            if len(str(CRN)) > 6 or len(str(CRN)) < 6:
                print("Course numbers are 6-digits!\n")
            #elif CRN in self.courseCRN:
                #print(CRN, "has already been created \n")
            else:#if it hasn't been created, well then create a new course object!
                new_course = course(CRN) #course(CRN,...more attributes) (see classes.py lines 2-8)
                print(new_course.CRN, "created successfully")
        except ValueError as err: #you entered in not what you were supposed 
            print(err)
   
    elif menu_choice == 4:
        #print courses (need to make this a function my fingers are getting tired from typing it out so many times)
        for index in range(len(courses)):
            print(index, courses[index])
        #removes course by indexing and not through word comparision
        choice = int(input("What course would you like to remove? \n"))
        for choice in courses:
            if choice == courses[index]:
                courses.remove(choice)
        #print courses again to now that you have successfully removed a course
        for index in range(len(courses)):
            print(index, courses[index])
    
    elif menu_choice == 5:
        #choose course and edit its information
        for index in range(len(courses)):
            print(index, courses[index])
            edit_info = int(input("Which course would you like to edit its attributes? \n"))        
        '''
        Since courses have mutliple attributes I will need to code this later
        '''
        
        '''
        The next two functions (force add, and force drop) can be coded as now
        because Ralph, Akshar, and I have not figured out how to link courses with
        students and vice versa yet.
        '''
        
    elif menu_choice == 6:
        print("Force add a student")
        #select a course (CRN)
        #select student (ID)
        #append student to selected course (this needs to override capacity which is set to 25 )
    
    elif menu_choice == 7:
        print("Force drop a student7")
        #select a course (CRN)
        #print its roster
        #select a student from roster (ID)
        #remove student from selected course
    
    elif menu_choice == 8:
        print("exit or go back?")
    
    else:
        print("Invalid Input")

#calling function see (admin.py line 63 (subject to change)
admin_test()
    
