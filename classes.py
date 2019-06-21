class course:
    def __init__(self, CRN, t, d, sch):
        self.CRN = CRN
        self.title = t
        self.description = d
        self.capacity = 25
        self.schedule = sch
    def set_title(self, t):
        self.title = t
    def set_description(self, d):
        self.description = d
    def set_capacity(self, c):
        self.capacity = c
    def set_schedule(self, sch):
        self.schedule = sch
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_capacity(self):
        return self.capacity
    def get_schedule(self):
        return self.schedule


class user:
    def __init__(self, ID, f, l, u, p):
        self.ID = ID
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = pass
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
        self.classes = []
    def set_major(slef, m):
        self.majorc = m
    def get_major(self):
        return self.major
    def add_class(self, CRN):
        if len(CRN) > 6 or len(CRN) < 6 :
            print("This course number is invalid \n")
        else:
            if CRN in self.classes:
                print(CRN, " is already registered for \n")
            else:
                self.classes.append(CRN)
                print(CRN, " has been added to ", self.firstName, " ", self.lastName, "'s list of courses \n")

    def remove_class(self, CRN):
        if len(CRN) > 6 or len(CRN) < 6 :
            print("This course number is invalid \n")
        else:
            if CRN in self.classes:
                self.classes.remove(CRN)
                print(CRN, " has been dropped \n")
            else:
                print(CRN, " is not registered for \n")

    def print_all(self):
        print("Student Name: ", self.firstName, " ", self.lastName, "\n")
        print("Registered Classes: | ")

        for cl in self.classes:
            print(cl, " | ")
        print("\n")
