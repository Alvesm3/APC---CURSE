class course:
    def __init__(self, CRN, t, d, sch):
        self.CRN = CRN #course CRNs are always made of 6 characters
        self.title = t
        self.description = d
        self.capacity = 25
        self.schedule = sch #sch has to be an array of size 2 containing start and end of the period (for this version at least)
        studentList = []
    def set_title(self, t):
        self.title = t
    def set_description(self, d):
        self.description = d
    def set_capacity(self, c):
        self.capacity = c
    def set_schedule(self, start, end):
        self.schedule[0] = from
        self.schedult[1] = to
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_capacity(self):
        return self.capacity
    def get_schedule_start(self):
        return self.schedule
    def print_schedule(self):
        print("from ", self.schedule[0], " to ", self.schedule[1])
    def get_CRN(self):
        return self.CRN
    def add_student(self, ID)
        self.studentList.append(ID)
    def remove_student(self, ID)
        self.studentList.remove(ID)

class user:
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

class student(user):
    def __init__(self, ID, f, l, u, p, m):
        self.ID = ID
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p
        self.major = m
        self.courseCRN = []
    def set_major(slef, m):
        self.majorc = m
    def get_major(self):
        return self.major
    def get_user_type(self): # SHOULD ADD TO ALL USER TYPES TO HELP MAIN DIFFERENTIATE
        return "student"

    def add_class(self, CRN, courses):
        if len(CRN) > 6 or len(CRN) < 6 :
            print("This course number is invalid \n")
        else:
            if CRN in self.courseCRN:
                print(CRN, " is already registered for \n")
            else:
                for course in courses:
                    if CRN == course.get_CRN():
                        newCourseIndex = courses.index(course) #place the new course under this variable to access in the next part
                for registeredCourses in courseCRN: #start by checking for timing conflicts
                    for course in courses:
                        if registeredCourses == course.get_CRN():
                            if (courses[newCourseIndex].schedule[0] >= course.schedule[0] and courses[newCourseIndex].schedule[0] <= course.schedule[1]) or (courses[newCourseIndex].schedule[1] <= course.schedule[1] and courses[newCourseIndex].schedule[0] >= course.schedule[0]):
                                print("This course does not fit in your schedule and conflicts with: ", course.get_title(), " ", course.get_CRN())
                                return
                self.courseCRN.append(CRN) #add the course if there are no conflicts
                courses[newCourseIndex].add_student(self.ID) #updates the course with a new student
                print(CRN, " has been added to ", self.firstName, " ", self.lastName, "'s list of courses \n")
                #note: course capacity is not taken into consideration for the first version

    def remove_class(self, CRN, courses):
        if len(CRN) > 6 or len(CRN) < 6 :
            print("This course number is invalid \n")
        else:
            if CRN in self.courseCRN:
                self.courseCRN.remove(CRN) #removes class from student's list
                for course in courses:
                    if CRN == course.get_CRN(): #update course roster
                        course.remove(self.ID)
                print(CRN, " has been dropped \n")
            else:
                print(CRN, " is not registered for \n")

    def print_all(self):
        print("Student Name: ", self.firstName, " ", self.lastName, "\n")
        print("Registered Classes: | ")

        for cl in self.classes:
            print(cl, " | ")
        print("\n")

    def view_schedule(self, courses): #very primitive function, will be updated soon to print a table
        for CRN in courseCRN:
            for course in courses:
                if CRN == course.get_CRN():
                    print(course.get_title(), " ", course.print_schedule(), "\n")
        return
