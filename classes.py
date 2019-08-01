class course:
    '''
    --------------------------------------------------------------------------------
    Description:
    A class for the courses offered within CURSE
    --------------------------------------------------------------------------------
    Variables:
    - CRN(string), which represents the course's unique identification number
    - title(string), which is the course's name
    - description(string)
    - capactiy(integer), which is the maximum number of students allowed to register
    - schedule(list of integers)
    - studetnList(list of integers), which is the list of IDs of students registered
      for the class
    - instructorID(integer), which is the ID of the course's instructor
    --------------------------------------------------------------------------------
    Functions:
    - constructor
    - usual get set functions for all variables
    --------------------------------------------------------------------------------
    '''

    def __init__(self, CRN, title, department, sch, instID, semester, prereq, enrolled):
        self.CRN = CRN #course CRNs are always made of 6 characters
        self.title = title
        self.department = department
        self.capacity = 25
        self.schedule = sch.split("-") #sch has to be an array of size 2 containing start and end of the period (for this version at least)
        self.studentList = [] if enrolled == 'none' else enrolled.split(" ")
        for studentID in self.studentList: #turn it all into integer
            studentID = int(studentID)
        self.instructorID = int(instID)
        self.semester = semester
        self.prerequisites = [] if prereq == 'none' else prereq.split(" ")
    def set_title(self, t):
        self.title = t
    def set_department(self, d):
        self.department = d
    def set_capacity(self, c):
        self.capacity = c
    def set_schedule(self, start, end):
        self.schedule[0] = start
        self.schedult[1] = end
    def set_instructorID(self,ID):
        self.instructorID = ID
    def get_title(self):
        return self.title
    def get_department(self):
        return self.department
    def get_capacity(self):
        return self.capacity
    def get_schedule_start(self):
        return self.schedule
    def print_schedule(self):
        print("from ", self.schedule[0], " to ", self.schedule[1])
    def get_CRN(self):
        return self.CRN
    def add_student(self, ID):
        self.studentList.append(ID)
    def remove_student(self, ID):
        self.studentList.remove(ID)
    def get_instructorID(self):
        return self.instructorID
    def get_prereq(self):
        return self.prerequisites


###Under Development
##########
class schedule:
    '''
    --------------------------------------------------------------------------------
    Description:
    A class that holds the data for a user's schedule
    --------------------------------------------------------------------------------
    Variables:
    - courseCRN(list of strings), which represents the user's courses
    - courseDays(list of integers), which gives the number of days each course
      takes place on (used to help navigate the arrays in the functions)
    - day(string), which represents the days of the week the course takes
      place
    - start(integer), which represents the time the course starts on a
      particular day
    - end(integer), which represents the time the course ends on a
      particular day
    --------------------------------------------------------------------------------
    Functions:
    - constructor
    - add_course function, used to add course schedule to the list
    - remove_course function, used to remove a course schedule from the list
    - get_schedule function, used to print the schedule
    --------------------------------------------------------------------------------
    '''

    def __init__(self, days, start, end):
        self.courseDays = days
        self.startTime = start
        self.endTime = end

    def print_schedule(self):
        for day in self.days:
            print(day + ": from " + self.startTime[self.days.index(day)] + " to " + self.endTime[self.days.index(day)])

    def check_for_conflict(self, otherSchedule):
        for day in self.days:
            if day in otherSchedule.days:
                if self.startTime[self.days.index(day)] > otherSchedule.startTime[self.days.index(day)] and self.startTime[self.days.index(day)] < otherSchedule.endTime[self.days.index(day)]:
                    return True
                if self.endtTime[self.days.index(day)] > otherSchedule.startTime[self.days.index(day)] and self.endTime[self.days.index(day)] < otherSchedule.endTime[self.days.index(day)]:
                    return True
        return False


#########


class user:
    '''
    --------------------------------------------------------------------------------
    Description:
    A parent class for the users accessing CURSE
    --------------------------------------------------------------------------------
    Variables:
    - ID(integer), which represents the user's unique identification number
    - firstName(string), which is the user's first name
    - lastName(string), which is the user's last name
    - username(string) , which is the user's unique username
    - password(string, but might change to int when encoded)
    --------------------------------------------------------------------------------
    Functions:
    - constructor
    - usual get set functions for all variables
    --------------------------------------------------------------------------------
    '''

    def __init__(self, ID, f, l, u, p):
        self.ID = ID
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p
    def set_username(self, u):
        self.username = u
    def set_firstName(self, f):
        self.firstName = f
    def set_lastName(self, l):
        self.lastName = l
    def set_ID(self, ID):
        self.ID = ID
    def set_password(self, p):
        self.password = p
    def get_username(self):
        return self.username
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_ID(self):
        return self.ID

class admin(user):
    def __init__(self, ID, f, l, u, p):
        self.ID = ID
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p
    def get_user_type(self): #To distinguish from other types of users in Main (See main.py line 39 (subject to change))
        return "admin"

    def view_all_courses(self, courses):
        for course in courses:
            print(course.get_title(), ' | Course CRN:', course.get_CRN(), ' | Course Instructor ID:', course.get_instructorID(), '\n---------------\n', course.get_department(), ' | Prereqs: ', course.get_prereq(), '\n------------------------------\n')

    def view_instructor_roster(self, users, courses):
        for user in users:
            if user.get_user_type() == 'instructor':
                print(user.get_firstName(), ' ', user.get_lastName(), ' | ', user.get_ID())
        ID = int(input('Enter the instructor\'s ID to view the roster: '))
        for user in users:
            if user.get_user_type() == 'instructor' and ID == user.get_ID():
                user.view_roster(users, courses)
                return
        print("This instructor does not exist \n")

    def add_course(self, users, courses):
        t = input("Enter the course's title: ")
        d = input("Enter the course's description: ")
        start = input("Enter the course's start time: ")
        end = input("Enter the course's end time: ")
        sch = start + "-" + end
        instID = int(input("Enter the course's instructor's ID: "))
        CRN = input("Finally, enter a unique 6 character CRN for the course: ")
        for course_ in courses:
            if course_.get_CRN() == CRN:
                print("the CRN already exists")
                return
        newCourse = course(CRN, t, d, sch, instID)
        courses.append(newCourse)
        for user in users: #adds the CRN to the instructors list of courses
            if instID == user.get_ID():
                user.courseCRN.append(CRN)


    def remove_course(self, users, courses):
        CRN = input("Enter the course's CRN: ")
        for course in courses:
            if CRN == course.get_CRN():
                print("are you sure you would like to remove ", CRN, ": ", course.get_title(), "? (y/n) ")
                answer = input()
                if answer == 'y' or answer == 'Y':
                    #remove the course from the instructor's roster:
                    for user in users:
                        if course.get_instructorID() == user.get_ID():
                            user.courseCRN.remove(CRN)
                    #remove the course from the students' schedules:
                    for studentID in course.studentList:
                        for user in users:
                            if studentID == user.get_ID():
                                user.courseCRN.remove(CRN)
                                break #to make it more time efficient efficient
                    courses.remove(course)
                    print("Course Removed")
                    return
                else:
                    return
        print("The course does not exist")

    def edit_course(self, users, courses):
        CRN = input("Enter the course's CRN: ")
        for course in courses:
            if CRN == course.get_CRN():
                attribute = input("Enter the attribute to edit (title/department/instructor): ")
                if attribute == 'title':
                    t = input("enter a new title: ")
                    course.set_title(t)
                    return
                elif attribute == 'department':
                    d = input("enter a new department: \n")
                    course.set_department(d)
                    return
                elif attribute == 'instructor':
                    ID = int(input("enter an instructor ID:"))
                    for user in users:
                        if user.get_ID() == ID and user.get_user_type() == 'instructor':
                            for user2 in users: #updates the previous instructor by removing the class from his roster
                                if course.get_instructorID() == user2.get_ID():
                                    user2.courseCRN.remove(course.get_CRN())
                            course.set_instructorID(ID) #sets course's instructor ID
                            users[users.index(user)].courseCRN.append(CRN) #adds course to the instructor's list
                            return
                    print("The instructor does not exist")
                    return
                else:
                    print("Attribute invalid")
                    return
        print("The course does not exist")

    def add_student(self, users, courses):
        ID = int(input("Enter the student's ID: "))
        for user in users:
            if ID == user.get_ID() and user.get_user_type() == 'student':
                CRN = input("Enter the course's CRN: ")
                for course in courses:
                    if CRN == course.get_CRN():
                        if ID in course.studentList:
                            print("This student is already registered for the course")
                            return
                        else:
                            course.add_student(ID)
                            print("Student added to CRN: ", CRN)
                            return
                print("This course does not exist")
                return
        print("This student does not exist")

    def remove_student(self, users, courses):
        ID = int(input("Enter the student's ID: "))
        for user in users:
            if ID == user.get_ID() and user.get_user_type() == 'student':
                CRN = input("Enter the course's CRN: ")
                for course in courses:
                    if CRN == course.get_CRN():
                        if ID in course.studentList:
                            course.remove_student(ID)
                            print("Student removed from CRN: ", CRN)
                            return
                        else:
                            print("This student is not registered for the course")
                            return
                print("This course does not exist")
                return
        print("This student does not exist")

    def view_all_students(self, users, courses):
        for user in users:
            if user.get_user_type() == "student":
                print("Student ID: ", user.ID, " | ", user.firstName, user.lastName, " |  Student year and major: ", user.major, user.classLevel, "\nCurrent Courses: ", user.courseCRN, "\nPast Courses: ", user.pastCourses, "\nMore Information: ", user.information)
                print("---------")
class student(user):
    '''
    --------------------------------------------------------------------------------
    Description:
    A class derived from the user class. This class is for student users accessing
    CURSE
    --------------------------------------------------------------------------------
    Variables:
    - ID(integer), which represents the user's unique identification number
    - firstName(string), which is the user's first name
    - lastName(string), which is the user's last name
    - username(string) , which is the user's unique username
    - password(string, but might change to int when encoded)
    - major(string), which is the student's major of study
    - courseCRN(list of strings), which is the list of courses the student is
      registered for
    --------------------------------------------------------------------------------
    Functions:
    - constructor
    - usual get set functions for all variables
    - get_user_type function, used to identify the user's type (student, instructor,
      or admin) in the CURSE's main function.
    - add_course, used to add a course to the student's list
    - remove_course, used to remove a course from the student's list
    - print_all, unsused at the moment
    - view_schedule, used to print the student's schedule
    --------------------------------------------------------------------------------
    '''

    def __init__(self, ID, f, l, u, p, m, classlvl, courses, pastcourses, information):
        self.ID = ID
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p
        self.major = m
        self.classLevel = classlvl
        self.courseCRN = [] if courses == 'none' else courses.split(" ")
        self.pastCourses = [] if pastcourses == 'none' else pastcourses.split(" ")
        self.information = information
    def set_major(slef, m):
        self.majorc = m
    def get_major(self):
        return self.major
    def get_user_type(self): # SHOULD ADD TO ALL USER TYPES TO HELP MAIN DIFFERENTIATE
        return "student"

    def view_all_courses(self, courses):
        for course in courses:
            print(course.get_title(), ' | Course CRN:', course.get_CRN(), ' | Course Instructor ID:', course.get_instructorID(), '\n---------------\n', course.get_department(), ' | Prereqs: ', course.get_prereq(), '\n------------------------------\n')

    def add_course(self, CRN, courses):
        if len(CRN) > 6 or len(CRN) < 6 :
            print("This course number is invalid \n")
        else:
            if CRN in self.courseCRN:
                print(CRN, " is already registered for \n")
            else:
                foundCourse = 0
                for course in courses:
                    if CRN == course.get_CRN():
                        foundCourse += 1
                        for registeredCRN in self.courseCRN: #start by checking for timing conflicts
                            for registeredCourse in courses:
                                if registeredCourse.CRN == registeredCRN:
                                    if (course.schedule[0] > registeredCourse.schedule[0] and course.schedule[0] < registeredCourse.schedule[1]) or (course.schedule[1] < registeredCourse.schedule[1] and course.schedule[0] > registeredCourse.schedule[0]):
                                        print("This course does not fit in your schedule and conflicts with: ", registeredCourse.get_title(), " ", course.get_CRN())
                                        return
                        self.courseCRN.append(CRN) #add the course if there are no conflicts
                        course.add_student(self.ID) #updates the course with a new student
                if foundCourse == 1:
                    print(CRN, " has been added to ", self.firstName, " ", self.lastName, "'s list of courses \n")
                else:
                    print(CRN, "does not exist in the available courses for this semester")
                #note: course capacity is not taken into consideration for the first version

    def remove_course(self, CRN, courses):
        if len(CRN) > 6 or len(CRN) < 6 :
            print("This course number is invalid \n")
        else:
            if CRN in self.courseCRN:
                self.courseCRN.remove(CRN) #removes class from student's list
                for course in courses:
                    if CRN == course.get_CRN(): #update course roster
                        course.remove_student(self.ID)
                print(CRN, " has been dropped \n")
            else:
                print(CRN, " is not registered for \n")

    def print_all(self): #needs an update for the newer version
        print("Student Name: ", self.firstName, " ", self.lastName, "\n")
        print("Registered Classes: | ")

        for cl in self.courseCRN:
            print(cl, " | ")
        print("\n")

    def view_schedule(self, courses): #very primitive function, will be updated soon to print a table
        numberOfCourses = 0
        for CRN in self.courseCRN:
            for course in courses:
                if CRN == course.get_CRN():
                    print(course.get_CRN(), ", ", course.get_title(), ": ")
                    course.print_schedule()
                    numberOfCourses +=1
        if numberOfCourses == 0:
            print("You don't have access to any classes")
        return

class instructor(user):
    '''
    --------------------------------------------------------------------------------
    Description:
    A class derived from the user class. This class is for instructor users
    accessing CURSE
    --------------------------------------------------------------------------------
    Variables:
    - ID(integer), which represents the user's unique identification number
    - firstName(string), which is the user's first name
    - lastName(string), which is the user's last name
    - username(string) , which is the user's unique username
    - password(string, but might change to int when encoded)
    - courseCRN(list of strings), which is the list of courses the instructor is
      teaching
    --------------------------------------------------------------------------------
    Functions:
    - constructor
    - usual get set functions for all variables
    - get_user_type function, used to identify the user's type (student, instructor,
      or admin) in the CURSE's main function.
    - view_schedule, used to print the instructor's schedule
    - view_roster, used to print the instructor's roster for every class
    --------------------------------------------------------------------------------
    '''

    def __init__(self, ID, f, l, u, p, courses):
        self.ID = ID
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p
        self.courseCRN = [] if courses == 'none' else courses.split(" ")
    def get_user_type(self): # SHOULD ADD TO ALL USER TYPES TO HELP MAIN DIFFERENTIATE
        return "instructor"

    #  def print_courses(self)

    def view_schedule(self, courses): #very primitive function, will be updated soon to print a table
        if not self.courseCRN:
            print("You have no access to any courses.")
        else:
            for CRN in self.courseCRN:
                for course in courses:
                    if CRN == course.get_CRN():
                        print(course.get_title(), " ", course.print_schedule(), "\n")
        return

    def view_roster(self, users, courses):
        if not self.courseCRN:
            print("You have no access to any courses.")
        else:
            for CRN in self.courseCRN:
                for course in courses:
                    if CRN == course.get_CRN():
                        print("------------")
                        print(course.get_CRN(), ' ', course.get_title(), ':\n')
                        if not course.studentList:
                            print("No students have registered yet.")
                        else:
                            for ID in course.studentList:
                                for user in users:
                                    if ID == user.get_ID():
                                        print(user.get_ID(), ' ', user.get_firstName(), ' ', user.get_lastName())
                        print("------------")
