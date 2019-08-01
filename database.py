import sqlite3
'''
Database to be used in CURSE
'''
database = sqlite3.connect("database")

cursor = database.cursor()
cursor.execute("drop table if exists student;")
cursor.execute("drop table if exists instructor;")
cursor.execute("drop table if exists admin;")
cursor.execute("drop table if exists course;")

sql_command = """CREATE TABLE STUDENT(
ID          int     not null,
fname       text    not null,
lname       text    not null,
username    text    not null,
password    text    not null,
major       char(4) not null,
classlvl    text    not null,
courses     text    not null,
pastcourses text    not null,
information text    not null,

constraint student_PK
primary key (ID)
);"""
cursor.execute(sql_command)

sql_command = """CREATE TABLE INSTRUCTOR(
ID          int     not null,
fname       text    not null,
lname       text    not null,
username    text    not null,
password    text    not null,
courses     text    not null,

constraint instructor_PK
primary key (ID)
);"""
cursor.execute(sql_command)

sql_command = """CREATE TABLE ADMIN(
ID          int     not null,
fname       text    not null,
lname       text    not null,
username    text    not null,
password    text    not null,

constraint admin_PK
primary key (ID)
);"""
cursor.execute(sql_command)

sql_command = """CREATE TABLE COURSE (
crn         varchar(6)  not null,
title       text    not null,
department  text    not null,
schedule    text    not null,
ID          int     not null,
semester    text    not null,
prereq      text    not null,
enrolled    text    not null,

constraint course_PK
primary key (crn)

);"""
cursor.execute(sql_command)

#Students - Up to 999 students
cursor.execute("""INSERT INTO student VALUES(001, 'Matthew', 'Alves', 'Malves', 'peaches','BSCO','Junior', 'none', '111111', 'athlete');""")
cursor.execute("""INSERT INTO student VALUES(002, 'Ralph', 'Ghannam', 'Rghannam', 'apples','BSCO','Junior', 'none', 'none', 'standard');""")
cursor.execute("""INSERT INTO student VALUES(003, 'Akshar', 'Patel', 'Apatel', 'grapes','BSCO','Junior', 'none', '111222', 'standard');""")
cursor.execute("""INSERT INTO student VALUES(004, 'Michael', 'Scott', 'Mscott', 'bananas','BSEE','Senior', 'none', 'none', 'account on hold');""")
cursor.execute("""INSERT INTO student VALUES(005, 'Dwight', 'Schrute', 'Dschrute', 'beets','BSCS','Senior', 'none', 'none', 'standard');""")
cursor.execute("""INSERT INTO student VALUES(006, 'Jim', 'Halpert', 'Jhalpert', 'pairs','BBA','Senior', 'none', 'none', 'standard');""")
cursor.execute("""INSERT INTO student VALUES(007, 'Pam', 'Beesly', 'Pbeesly', 'pineapples','BA','Sophomore', 'none', 'none', 'standard');""")
cursor.execute("""INSERT INTO student VALUES(008, 'Kevin', 'Malone', 'Kmalone', 'kiwis','BSCE','Sohpomore', 'none', 'none', 'standard');""")
cursor.execute("""INSERT INTO student VALUES(009, 'Ryan', 'Howard', 'Rhoward', 'mangoes','BBA','Sophomore', 'none', 'none', 'standard');""")
cursor.execute("""INSERT INTO student VALUES(010, 'Andy', 'Bernard', 'Abernard', 'blueberries','CS','Senior', 'none', 'none', 'standard');""")

#Instructors
cursor.execute("""INSERT INTO instructor VALUES(1000,'Donald','Trump','Dtrump','maga45', '123456');""")
cursor.execute("""INSERT INTO instructor VALUES(1001,'Barack','Obama','Bobama','yeswecan44', '234567');""")
cursor.execute("""INSERT INTO instructor VALUES(1002,'George','Bush','Gbush','warhead43', '135791');""")
cursor.execute("""INSERT INTO instructor VALUES(1003,'Bill','Clinton','Bclinton','saxman42', '456789');""")
cursor.execute("""INSERT INTO instructor VALUES(1004,'Ronald','Reagan','Rreagan','reagansmash40', '567890 246824');""")
cursor.execute("""INSERT INTO instructor VALUES(1005,'Jimmy','Carter','Jcarter','peanuts39', '345678');""")

#Admins
cursor.execute("""INSERT INTO admin VALUES(2000,'Elon','Musk','Emusk','tesla314');""")
cursor.execute("""INSERT INTO admin VALUES(2001,'Steve','Jobs','Sjobs','apple234');""")

#Courses
cursor.execute("""INSERT INTO course VALUES('123456','Calculus','Math', '7-8',1000,'Fall 2019', '111111', 'none');""")
cursor.execute("""INSERT INTO course VALUES('234567','History','Social Studies', '9-10',1001,'Fall 2019', 'none', 'none');""")
cursor.execute("""INSERT INTO course VALUES('345678','Art','Creative', '17-18', 1005,'Fall 2019', 'none', 'none');""")
cursor.execute("""INSERT INTO course VALUES('456789','Buisness','Social Studies', '10-11', 1003,'Fall 2019', '111222', 'none');""")
cursor.execute("""INSERT INTO course VALUES('567890','Algebra','Math', '14-16', 1004,'Fall 2019', 'none', 'none');""")
cursor.execute("""INSERT INTO course VALUES('135791','Biology','Science', '16-17', 1002,'Spring 2020', 'none', 'none');""")
cursor.execute("""INSERT INTO course VALUES('246824','Physics','Science', '20-21', 1004,'Spring 2020', 'none', 'none');""")

def print_student_table():
    print("\t\tStudent Table")
    with database:
        cursor.execute("""SELECT * FROM STUDENT""")
    query_result = cursor.fetchall()

    for students in query_result:
	    print(students)

def print_instructor_table():
    print("\t\tInstructor Table")
    with database:
        cursor.execute("""SELECT * FROM INSTRUCTOR""")
    query_result = cursor.fetchall()

    for instructors in query_result:
    	print(instructors)

def print_admin_table():
    print("\t\tAdmin Table")
    with database:
        cursor.execute("""SELECT * FROM ADMIN""")
    query_result = cursor.fetchall()

    for admins in query_result:
    	print(admins)


def print_course_table():
    print("\t\tCourses Table")
    with database:
        cursor.execute("""SELECT * FROM course""")
    myresult = cursor.fetchall()

    for courses in myresult:
        print(courses)

def print_all():
    print_student_table()
    print_instructor_table()
    print_admin_table()
    print_course_table()

print_all()

database.commit()
database.close()
