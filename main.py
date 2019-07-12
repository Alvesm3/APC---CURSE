import classes
import functions

def main():
    response, noStudent = 1, 1 #variables: user's response to UI,
    ID, f, l, m, CRN, u, p,  = "", "", "", "", "", "", ""
    users = []
    courses = []
################################################################################
    #hardcoding admin:
    newAdmin = classes.admin(0, "Ralph", "Ghannam", "ghannamr", "password")
    users.append(newAdmin)
################################################################################
    while response != "0": #main loop
        print("Welcome to CURSE \n")
        print("----------------------------------------------\n")
        userIndex = -1 #variable that determines the user's index in the list, currently not holding a value
        while userIndex == -1: #while the user isn't determined
            functions.print_login_menu()
            response = input()
            if response == "1":
                userIndex = functions.log_in(users) #gets user index
            elif response == "2":
                userIndex = functions.sign_up(users)
            elif response == "0":
                break
            else:
                print("invalid response")

            if userIndex != -1: #fixes a small bug
################################################################################
        #STUDENT COMPONENT
                if users[userIndex].get_user_type() == "student": #student section
                    while response != "4":
                        functions.print_student_menu(users[userIndex])
                        response = input()
                        if response == "1": #add courses
                            CRN = input("Enter the course number\n")
                            users[userIndex].add_course(CRN, courses)
                        elif response == "2": #drop courses
                            CRN = input("Enter the course number\n")
                            users[userIndex].remove_course(CRN, courses)
                        elif response == "3": #print schedule
                            users[userIndex].view_schedule(courses)
################################################################################
        #INSTRUCTOR COMPONENT
                elif users[userIndex].get_user_type() == "instructor":
                    while response != "3":
                        functions.print_instructor_menu(users[userIndex])
                        response = input()
                        if response == "1": #view schedule
                            users[userIndex].view_schedule(courses)
                        elif response == "2":
                            users[userIndex].view_roster(users, courses)
################################################################################
        #ADMIN COMPONENT
                elif users[userIndex].get_user_type() == "admin":
                    while response != "8":
                        functions.print_admin_menu()
                        response = input()
                        if response == "1":
                            users[userIndex].view_all_courses(courses)
                        elif response == "2":
                            users[userIndex].view_roster(users)
                        elif response == "3":
                            users[userIndex].add_course(users, courses)
                        elif response == "4":
                            users[userIndex].remove_course(users, courses)
                        elif response == "5":
                            users[userIndex].edit_course(users, courses)
                        elif response == "6":
                            users[userIndex].add_student(users, courses)
                        elif response == "7":
                            users[userIndex].remove_student(users, courses)
################################################################################


if __name__ == "__main__":
    main()
