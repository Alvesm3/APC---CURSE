import classes
import functions
import sqlite3

def main():
    database = sqlite3.connect("database")
    cursor = database.cursor()
    users = []
    courses = []

    #pick a school semester to log into
    semester = ""
    while semester != "Fall 2019" and semester != "Spring 2020":
        print("Pick a Semester: Fall 2019 / Spring 2020")
        semester = input()
        if semester != "Fall 2019" and semester != "Spring 2020":
            print("This answer is invalid")

    #Start by taking the data out of the database:
    cursor.execute("Select * From Student")
    results = cursor.fetchall()
    for result in results:
        users.append(classes.student(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9]))
    cursor.execute("Select * From Instructor")
    results = cursor.fetchall()
    for result in results:
        users.append(classes.instructor(result[0], result[1], result[2], result[3], result[4], result[5]))
    cursor.execute("Select * From Admin")
    results = cursor.fetchall()
    for result in results:
        users.append(classes.admin(result[0], result[1], result[2], result[3], result[4]))
    cursor.execute("Select * From Course Where semester = '" + semester + "'")
    results = cursor.fetchall()
    for result in results:
        courses.append(classes.course(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))


    response, noStudent = 1, 1 #variables: user's response to UI,
    ID, f, l, m, CRN, u, p,  = "", "", "", "", "", "", ""
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
                            users[userIndex].view_all_courses(courses)
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
                    while response != "9":
                        functions.print_admin_menu()
                        response = input()
                        if response == "1":
                            users[userIndex].view_all_courses(courses)
                        elif response == "2":
                            users[userIndex].view_instructor_roster(users, courses)
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
                        elif response == "8":
                            users[userIndex].view_all_students(users, courses)
################################################################################


    # Commit changes to the database
    cursor.execute("Delete From Student")
    cursor.execute("Delete From Instructor")
    for user in users:
        if user.get_user_type() == "student":
            CRNtoDatabase = ""
            if not user.courseCRN:
                CRNtoDatabase = "none"
            else:
                for CRN in user.courseCRN:
                    CRNtoDatabase = CRNtoDatabase + CRN + " "
            pastCRNtoDatabase = ""
            if not user.pastCourses:
                pastCRNtoDatabase = "none"
            else:
                for CRN in user.pastCourses:
                    pastCRNtoDatabase = pastCRNtoDatabase + CRN + " "
            cursor.execute("Select * From Student Where ID = " + str(user.ID))
            result = cursor.fetchall()
            cursor.execute("Insert Into Student Values (" + str(user.ID) + ", '" + user.firstName + "' ,'" + user.lastName + "' ,'" + user.username + "' ,'" + user.password + "' ,'" + user.major + "' ,'" + user.classLevel + "' ,'" + CRNtoDatabase + "' ,'" + pastCRNtoDatabase + "' ,'" + user.information + "')")
            database.commit()
        elif user.get_user_type() == "instructor":
            CRNtoDatabase = ""
            if not user.courseCRN:
                CRNtoDatabase = "none"
            else:
                for CRN in user.courseCRN:
                    CRNtoDatabase = CRNtoDatabase + CRN + " "
            cursor.execute("Select * From Instructor Where ID = " + str(user.ID))
            result = cursor.fetchall()
            cursor.execute("Insert Into Instructor Values (" + str(user.ID) + ", '" + user.firstName + "' ,'" + user.lastName + "' ,'" + user.username + "' ,'" + user.password + "' ,'" + CRNtoDatabase + "')")
            database.commit()

            # admins don't change

    cursor.execute("Delete From Course Where semester = '" + semester + "'")
    for course in courses:
        scheduleToDatabase = str(course.schedule[0] + "-" + str(course.schedule[1]))
        prereqToDatabase = ""
        if not course.prerequisites:
            prereqToDatabase = "none"
        else:
            for prereq in course.prerequisites:
                prereqToDatabase = prereqToDatabase + prereq + " "
        enrolledToDatabase = ""
        if not course.studentList:
            enrolledToDatabase = "none"
        else:
            for enrolled in course.studentList:
                enrolledToDatabase = enrolledToDatabase + str(enrolled) + " "
        cursor.execute("Insert Into Course Values ('" + course.CRN + "', '" + course.title + "', '" + course.department + "', '" + scheduleToDatabase + "', " + str(course.instructorID) + ", '" + course.semester + "', '" + prereqToDatabase + "', '" + enrolledToDatabase + "')")
        database.commit()


    database.commit()
    database.close()


if __name__ == "__main__":
    main()
