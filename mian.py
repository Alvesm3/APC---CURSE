import classes
import functions

def main():
    response, noStudent = 1, 1
    ID, f, l, m, CRN, u, p,  = "", "", "", "", "", "", ""
    students = []
    courses = []

    print("Welcome to the Student Registration UI \n")
    print("----------------------------------------------\n")

    while response != "0":
        print_login_menu()      # CONTINUING HERE

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
