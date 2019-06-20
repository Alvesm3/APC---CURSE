class user:

    def __init__(self, f, l, u, p):
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p

class student(user):

    def __init__(self, f, l, m):
        self.firstName = f
        self.lastName = l
        self.username = u
        self.password = p
        self.major = m
        self.classes = []

    def set_firstName(self, f):
        self.firstName = f

    def set_lastName(self, l):
        self.lastName = l

    def set_major(slef, m):
        self.majorc = m

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

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


def print_main_menu():
    print("----------------------------------------------\n")
    print("Press 1 to add a student\n")
    print("Press 2 to access a student\n")
    print("Press 0 to exit\n")
    print("----------------------------------------------\n")

def print_sub_menu(st):
    print("----------------------------------------------\n")
    print("Welcome!\n")
    st.print_all()
    print("Would you like to change your courses?\n")
    print("Press 1 to add a course\n")
    print("Press 2 to remove a course\n")
    print("Press 3 to go back\n")
    print("----------------------------------------------\n")

def main():
    response, noStudent = 1, 1
    f, l, m, CRN = "", "", "", ""
    students = []
    courses = [course1]
    print("Welcome to the Student Registration UI \n")
    print("----------------------------------------------\n")
    while response != "0":
        print_main_menu()
        response = input()
        if response == "1":
            f, l, m = input("Enter the student's first name, last name, and major\n").split()
            newStudent = student(f, l, m)
            students.append(newStudent)
            print("Student added\n")
        elif response == "2":
            if len(students) == 0:
                print("There are no students registered yet")
            else:
                f, l, m = input("Enter the student's first name, last name, and major\n").split()
                for st in students:
                    if st.get_firstName() == f and st.get_lastName() == l and st.get_major() == m:
                        while response != "3":
                            noStudent = 0
                            print_sub_menu(st)
                            response = input()
                            if response == "1":
                                CRN = input("Enter the course number\n")
                                st.add_class(CRN)
                            elif response == "2":
                                CRN = input("Enter the course number\n")
                                st.remove_class(CRN)
                            elif response == "3":
                                break
                if noStudent == 1:
                    print("This student is not registered\n")
                noStudent = 1


if __name__ == "__main__":
    main()
