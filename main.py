import classes
import functions

def main():
    response, noStudent = 1, 1 #variables: user's response to UI,
    ID, f, l, m, CRN, u, p,  = "", "", "", "", "", "", ""
    users = []
    courses = []

    print("Welcome to CURSE \n")
    print("----------------------------------------------\n")
    userIndex = -1 #variable that determines the user's index in the list, currently not holding a value
    while userIndex == -1: #while the user isn't determined
        functions.print_login_menu()
        response = input()
        if response == "1":
            userIndex = functions.log_in() #gets user index
        elif response == "2":
            userIndex = functions.sign_up()
        else:
            print("Can you read?")
    while response != "0": #start of the main loop

        if users[userIndex].get_user_type() == "student": #student section
            while response != "4":
                functions.print_student_menu(users[userIndex])
                response = input()
                if response == "1": #add courses
                    CRN = input("Enter the course number\n")
                    users[userIndex].add_course(CRN)
                elif response == "2": #drop courses
                    CRN = input("Enter the course number\n")
                    users[userIndex].remove_course(CRN)
                elif response == "3": #print schedule
                    users[userIndex].view_schedule()
        elif users[userIndex].get_user_type() == "instructor":
            while response != "3":
                print_instructor_menu(users[userIndex])
                response = input()
                if response == "1": #view schedule
                    users[userIndex].view_schedule()
                if response == "2":
                    users[userIndex].view_roster()
            #add instructor funcctions
        elif users[userIndex].get_user_type() == "admin"
            #add admin functions



if __name__ == "__main__":
    main()
