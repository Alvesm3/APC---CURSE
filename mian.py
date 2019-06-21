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
        if response == 1:
            userIndex = functions.log_in(users) #gets user index
        elif response == 2:
            userIndex = functions.sign_up(users)
        else:
            print("Can you read?")
    while response != "0": #start of the main loop

        if user[userIndex].get_user_type() == "student": #student section
            while response != "4":
                functions.print_sub_menu(st)
                response = input()
                if response == "1": #add courses
                    CRN = input("Enter the course number\n")
                    st.add_class(CRN, courses)
                elif response == "2": #drop courses
                    CRN = input("Enter the course number\n")
                    st.remove_class(CRN, courses)
                elif response == "3": #print schedule
                    st.view_schedule()
        elif user[userIndex].get_user_type() == "instructor"
            #add instructor funcctions
        elif user[userIndex].get_user_type() == "admin"
            #add admin functions



if __name__ == "__main__":
    main()
