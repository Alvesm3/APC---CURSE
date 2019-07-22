import sqlite3

# Use :memory: so database can be maniuplated and dynamically change
database = sqlite3.connect(":memory:")

# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

sql_command = """CREATE TABLE STUDENT (  
ID 		    INT     NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
GRADYEAR	INT 	NOT NULL,
MAJOR		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL,

constraint studnet_pk
primary key (ID)
);"""
cursor.execute(sql_command) 

sql_command = """CREATE TABLE INSTRUCTOR (  
ID 		    INT 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
HIREYEAR	INT 	NOT NULL,
DEPT		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL,

constraint instructor_pk
primary key (ID)
);"""
cursor.execute(sql_command) 

sql_command = """CREATE TABLE ADMIN (  
ID 		    INT 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
OFFICE		TEXT 	NOT NULL,
EMAIL		text	NOT NULL,

constraint admin_pk
primary key (ID)
);"""
cursor.execute(sql_command)

#Student list
cursor.execute("""INSERT INTO STUDENT VALUES(00010001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010002, 'Marie', 'Curie', 1903, 'BSAS', 'curiem');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010003, 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010004, 'Thomas', 'Edison', 1879, 'BSEE', 'notcool');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010005, 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010006, 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010007, 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010008, 'Mark', 'Dean', 1979, 'BSCO', 'deanm');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010009, 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010010, 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea');""") 

# Instructor list
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020003, 'Galileo', 'Galilei', 'Full Prof.', 1600, 'BSAS', 'galileig');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""") 

# Admin list
cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""") 
cursor.execute("""INSERT INTO ADMIN VALUES(00030002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""") 

#----------------------------------------------------------------------------------------------------------------------------------------------#
#Assignment 7

sql_command = """create table course (
crn         INT     NOT NULL,
title       text    not null,
department  text    not null,
ID          INT     not null,
time        text   not null,
day         text    not null,
semester    text    not null,
year        INT     not null,
credits     INT     not null,

constraint course_PK
primary key (crn),

constraint course_instructor_FK
foreign key (ID)
references instructor(ID)
);"""
cursor.execute(sql_command)

cursor.execute("""INSERT INTO course VALUES(100001, 'Calculus', 'Math', '00020001', '8am - 10am', 'Mon-Tue-Thur','Fall', '2019','4');""") 
cursor.execute("""INSERT INTO course VALUES(100002, 'History', 'Social Studies', '00020002', '10am - 12pm', 'Mon-Wed','Fall', '2019','4');""") 
cursor.execute("""INSERT INTO course VALUES(100003, 'Astronomy', 'Science', '00020003', '12:30pm - 1:30pm', 'Tue-Thur-Fri','Fall', '2019','4');""") 
cursor.execute("""INSERT INTO course VALUES(100004, 'Algebra', 'Math', '00020004', '8am - 10am', 'Wed-Fri','Fall', '2019','4');""") 
cursor.execute("""INSERT INTO course VALUES(100005, 'Computers', 'Special', '00020005', '1pm - 2:30 pm', 'Mon-Wed-Fri','Fall', '2019','3');""") 


'''
def print_student_table():
def print_instructor_table():
def print_admin_table():
def print_course_table():
def print_table_input():
'''
'''Below are functions to print each respective table'''
def print_student_table():
    print("\t\tStudent Table")
    with database:
        cursor.execute("""SELECT * FROM STUDENT""")
    query_result = cursor.fetchall()
  
    for i in query_result:
	    print(i)
#print_student_table()

def print_instructor_table():
    print("\t\tInstructor Table")
    with database:
        cursor.execute("""SELECT * FROM INSTRUCTOR""")
    query_result = cursor.fetchall()
      
    for i in query_result:
    	print(i)
#print_instructor_table()

def print_admin_table():
    print("\t\tAdmin Table")
    with database:    
        cursor.execute("""SELECT * FROM ADMIN""")
    query_result = cursor.fetchall()
      
    for i in query_result:
    	print(i)
#print_admin_table()    	
    	
def print_course_table():
    print("\t\tCourses Table")
    with database:
        cursor.execute("""SELECT * FROM course""")
    myresult = cursor.fetchall()
    
    for rows in myresult:
        print(rows)
#print_course_table()

'''This function takes user input, they specify which database they want to see by typing in the table name and it prints out that table'''
def print_table_input():
    #table = input("What table would you like to view")
    print("{} Table".format(table))
    with database:
        cursor.execute("SELECT * FROM {}".format(table))
    myresult = cursor.fetchall()
        
    for rows in myresult:
        print(rows)
        
'''
This function puts all the functions above into one coherent function and adds a menu
You can select the number associated with each database 1), 2), 3), 4) or type in the
specific database you want (both will work)
What is nice about sqlite3 is that query searching IS NOT case sensitve so for example
typing student, Student, STUDENT, or StUdEnT will all yield the student table! Nice!!
'''
def print_tables():
    print("1) Student\n2) Instructor\n3) Admin\n4) Course")
    global table
    table = input("What table would you like to view ")
    if table == '1':
        print_student_table()
    elif table == '2':
        print_instructor_table()
    elif table == '3':
        print_admin_table()  
    elif table == '4':
        print_course_table()
    else:
        print_table_input()
#rint_tables()

'''
def insert():
    input: Which table would you like to add data? 1) student 2) instructor 3) admin 4) course
    input: How many insertions would you like to do?
    input: Take respective input
    execute: Update database
    print: print database to show that it is working 

#Different ways to pass in values
cursor.execute(INSERT INTO <table name> VALUES ('{}', '{}', {})".format(string, string, int)) #notice no quotations on the last {} to signify an int
or
cursor.execute(INSERT INTO <table name> VALUES (:xxxx, :yyyy, :zzzz)", {'xxxx': passin, 'yyyy': passin, 'zzzz' : passin})
or
cursor.execute(INSERT INTO <table name> VALUES (?, ?, ?)", (passin, passin, passin))
or
cursor.execute(INSERT INTO <table name> VALUES ('%s', '%s', '%s')" %(passin, passin, passin))

*Option 3 uses the least amount of characters and time is of the essence, so let's use that
*Also, using a format method is apparently vunerable to SQL injection attacks https://www.w3schools.com/sql/sql_injection.asp
'''

def insert_student():
    num = int(input("How many students would you like to add? "))
    for i in range(num):
        ID, name, surname, gradyear, major, email = input("Please enter a new student.\nA student has an ID, name, surname, graduation year, major, and email.\nSeparate your answers by commas\n").split(',')
        with database:    
            cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?)", (ID, name, surname, gradyear, major, email))
            print("Student", name, surname, "has been added")
    print_student_table() #see if student table has been updated 
#insert_student()

def insert_instructor():
    num = int(input("How many instructors would you like to add? ")) 
    for i in range(num):
        ID, name, surname, title, hireyear, dept, email = input("Please enter a new instructor.\nA instructor has an ID, name, surname, title, hire year, department, and email\nSeparate your answers by commas\n").split(',')
        with database:    
            cursor.execute("INSERT INTO instructor VALUES (?, ?, ?, ?, ?, ?, ?)", (ID, name, surname, title, hireyear, dept, email))
            print("Instructor", name, surname, "has been added")
    print_instructor_table() #see if instructor table has been updated 
#insert_instructor()

def insert_admin():  
    num = int(input("How many admins would you like to add? ")) 
    for i in range(num):
        ID, name, surname, title, office, email = input("Please enter a new admin.\nAn admin has an ID, name, surname, title, office, and email\nSeparate your answers by commas\n").split(',')
        with database:
            cursor.execute("INSERT INTO admin VALUES (?, ?, ?, ?, ?, ?)", (ID, name, surname, title, office, email))
            print("Admin", name, surname, "has been added")
    print_admin_table()#see if admin table has been updated 
#insert_admin()

def insert_course():  
    num = int(input("How many courses would you like to add? ")) 
    for i in range(num):
        crn, title, dept, time, day, sem, year, credit = input("Please enter a new course.\nA course has a crn, title, department, time, day, semester, year, and credits\nSeparate your answers by commas\n").split(',')
        print_instructor_table()
        ID = input("Please enter in the ID of the instructor who will teach this course\n ")
        with database:    
            cursor.execute("INSERT INTO course VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (crn, title, dept, ID, time, day, sem, year, credit))
            print("Course", crn, title, "has been added")
    print_course_table()#see if course table has been updated 
#insert_course()

'''Put everything together and add a menu'''
def insert():
    print("1) Student\n2) Instructor\n3) Admin \n4) Course")
    choice = int(input("Which table would you like to add values to? "))
    if choice == 1:
        insert_student()
    elif choice == 2:
        insert_instructor()
    elif choice == 3:
        insert_admin()
    elif choice == 4:
        insert_course()
#insert()

'''
def update():
    input: Which table would you like to update? 1) student 2) instructor 3) admin 4) course
    input: Take respective input
    execute: update database
    print: print database to show it is working
'''
def update_student():
    print("\tStudent Atrtibutes\nname, surname, gradyear, major, email")
    print_student_table()
    ID = input("Who would you like to update? Please enter a primary key ")
    update = input("What attribute would you like to update? ")
    change = input("What is the new value? ")
    cursor.execute("UPDATE student SET '{}' = '{}' where ID = {}".format(update, change, ID))
    print("Student table has been updated successfully!")
    print_student_table()
#update_student()

def update_instructor():
    print("\tInstructor Attributes\nname, surname, title, hireyear, dept, email")
    print_instructor_table()
    ID = input("Who would you like to update? Please enter a primary key ")
    update = input("What attribute would you like to update? ")
    change = input("What is the new value? ")
    cursor.execute("UPDATE instructor SET '{}' = '{}' where ID = {}".format(update, change, ID))
    print("Instructor table has been updated successfully!")
    print_instructor_table()
#update_instructor()

def update_admin():
    print("\tAdmin Attributes\nname, surname, title, office, email")
    print_admin_table()
    ID = input("Who would you like to update? Please enter a primary key ")
    update = input("What attribute would you like to update? ")
    change = input("What is the new value? ")
    cursor.execute("UPDATE admin SET '{}' = '{}' where ID = {}".format(update, change, ID))
    print("Admin table has been updated successfully!")
    print_admin_table()
#update_admin()

def update_course():
    print("\tCourse Attributes\ncrn, title, department, ID, time, day, semester, year, credits")
    print_course_table()
    crn = input("Who course would you like to update? Please enter a crn ")
    update = input("What attribute would you like to update? ")
    change = input("What is the new value? ")
    cursor.execute("UPDATE course SET '{}' = '{}' where crn = {}".format(update, change, crn))
    print("Course table has been update successfully!")
    print_course_table()
#update_course()

'''Put everything together and add a menu'''
def update():
    print("1) Student\n2) Instructor\n3) Admin \n4) Course")
    choice = int(input("Which table would you like to update values to? "))
    if choice == 1:
        update_student()
    elif choice == 2:
        update_instructor()
    elif choice == 3:
        update_admin()
    elif choice == 4:
        update_course()
#update()

'''
def delete():
    input: Which table would you like to delete from? 1) student 2) instructor 3) admin 4) course
    input: Take respective input
    execute: remove tuple from database
    print: print database to show that it is working
'''
def delete_student():
    print("\tStudent Atrtibutes\nname, surname, gradyear, major, email")
    print_student_table()
    ID = input("Who would you like to delete? Please enter a primary key ")
    with database:
        cursor.execute("DELETE FROM student where ID = ?", (ID,))
        print("Student", ID, "has been deleted successfully!")
    print_student_table()
#delete_student()

def delete_instructor():
    print("\tInstructor Attributes\nname, surname, title, hireyear, dept, email")
    print_instructor_table()
    ID = input("Who would you like to delete? Please enter a primary key ")    
    with database:
        cursor.execute("DELETE FROM instructor where ID = ?", (ID,))
        print("Instructor", ID, "has been deleted successfully!")
    print_instructor_table()
#delete_instructor()

def delete_admin():
    print("\tAdmin Attributes\nname, surname, title, office, email")
    print_admin_table()
    ID = input("Who would you like to delete? Please enter a primary key ")
    with database:
        cursor.execute("DELETE FROM admin where ID = ?", (ID,))
        print("Admin", ID, "has been deleted successfully!")
    print_admin_table()
#delete_admin()

def delete_course():
    print("\tCourse Attributes\ncrn, title, department, ID, time, day, semester, year, credits")
    print_course_table()
    crn = input("Who course would you like to delete? Please enter a crn ")
    with database:
        cursor.execute("DELETE FROM course where crn = ?", (crn,))
        print("Course", crn, "has been deleted successfully!")
    print_course_table()
#delete_course()

'''Put everything together into a menu...yadda yadda yadda you know the drill'''  
def delete():
    print("1) Student\n2) Instructor\n3) Admin \n4) Course")
    choice = int(input("Which table would you like to delete values from? "))
    if choice == 1:
        delete_student()
    elif choice == 2:
        delete_instructor()
    elif choice == 3:
        delete_admin()
    elif choice == 4:
        delete_course()
#delete()


def main():
    switch = int(input("Press 1 to print a specific table\nPress 2 to insert data into tables\nPress 3 to update data in tables\nPress 4 to delete data from tables\nPress 0 to quit\n"))
    while switch != 0:
        if switch == 1:
            print_tables()
            switch = int(input("Press 1 to print a specific table\nPress 2 to insert data into tables\nPress 3 to update data in tables\nPress 4 to delete data from tables\nPress 0 to quit\n"))
        elif switch == 2:
            insert()
            switch = int(input("Press 1 to print a specific table\nPress 2 to insert data into tables\nPress 3 to update data in tables\nPress 4 to delete data from tables\nPress 0 to quit\n"))
        elif switch == 3:
            update()
            switch = int(input("Press 1 to print a specific table\nPress 2 to insert data into tables\nPress 3 to update data in tables\nPress 4 to delete data from tables\nPress 0 to quit\n"))
        elif switch == 4:
            delete()
            switch = int(input("Press 1 to print a specific table\nPress 2 to insert data into tables\nPress 3 to update data in tables\nPress 4 to delete data from tables\nPress 0 to quit\n"))
        else:
            print("invalid input...try again")
            switch = int(input("Press 1 to print a specific table\nPress 2 to insert data into tables\nPress 3 to update data in tables\nPress 4 to delete data from tables\nPress 0 to quit\n"))
            

if __name__=="__main__":
    main()


'''
If you are to save this to a .db file then you need to uncomment database.close()
You don't need database.commit() because "with database:" was used to excute (change) values in each function therefore just leave it blocked out
'''
#database.commit() 
#database.close()


















