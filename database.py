import sqlite3 
'''
Database to be used in CURSE
'''
database = sqlite3.connect(":memory:")

cursor = database.cursor()

sql_command = """CREATE TABLE STUDENT(
ID          int     not null,
fname       text    not null,
lname       text    not null,
username    text    not null,
password    text    not null,
major       char(4) not null,
classlvl    text    not null,   

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
crn         int(6)  not null,
title       text    not null,
department  text    not null,
ID          int     not null,
schedule    text    not null,

constraint course_PK
primary key (crn),

constraint course_instructor_FK
foreign key (ID)
references instructor(ID)
);"""
cursor.execute(sql_command)

#Students - Up to 999 students
cursor.execute("""INSERT INTO student VALUES(001, 'Matthew', 'Alves', 'Malves', 'peaches','BSCO','Junior');""") 
cursor.execute("""INSERT INTO student VALUES(002, 'Ralph', 'Ghannam', 'Rghannam', 'apples','BSCO','Junior');""") 
cursor.execute("""INSERT INTO student VALUES(003, 'Akshar', 'Patel', 'Apatel', 'grapes','BSCO','Junior');""") 
cursor.execute("""INSERT INTO student VALUES(004, 'Michael', 'Scott', 'Mscott', 'bananas','BSEE','Senior');""") 
cursor.execute("""INSERT INTO student VALUES(005, 'Dwight', 'Schrute', 'Dschrute', 'beets','BSCS','Sophomore');""") 
cursor.execute("""INSERT INTO student VALUES(006, 'Jim', 'Halpert', 'Jhalpert', 'pairs','BBA','Freshman');""") 
cursor.execute("""INSERT INTO student VALUES(007, 'Pam', 'Beesly', 'Pbeesly', 'pineapples','BA','Freshman');""") 
cursor.execute("""INSERT INTO student VALUES(008, 'Kevin', 'Malone', 'Kmalone', 'kiwis','BSCE','Sohpomore');""") 
cursor.execute("""INSERT INTO student VALUES(009, 'Ryan', 'Howard', 'Rhoward', 'mangoes','BBA','Senior');""") 
cursor.execute("""INSERT INTO student VALUES(010, 'Andy', 'Bernard', 'Abernard', 'blueberries','BSB','Senior');""") 

#Instructors
cursor.execute("""INSERT INTO instructor VALUES(1000,'Donald','Trump','Dtrump','maga45');""")
cursor.execute("""INSERT INTO instructor VALUES(1001,'Barack','Obama','Bobama','yeswecan44');""")
cursor.execute("""INSERT INTO instructor VALUES(1002,'George','Bush','Gbush','warhead43');""")
cursor.execute("""INSERT INTO instructor VALUES(1003,'Bill','Clinton','Bclinton','saxman42');""")
cursor.execute("""INSERT INTO instructor VALUES(1004,'Ronald','Reagan','Rreagan','reagansmash40');""")
cursor.execute("""INSERT INTO instructor VALUES(1005,'Jimmy','Carter','Jcarter','peanuts39');""")

#Admins
cursor.execute("""INSERT INTO admin VALUES(2000,'Elon','Musk','Emusk','tesla314');""")
cursor.execute("""INSERT INTO admin VALUES(2001,'Steve','Jobs','Sjobs','apple234');""")

#Courses
cursor.execute("""INSERT INTO course VALUES(123456,'Calculus','Math','1000','Mon - Wed');""")
cursor.execute("""INSERT INTO course VALUES(234567,'History','Social Studies','1001','Mon - Tue - Thur');""")
cursor.execute("""INSERT INTO course VALUES(345678,'Art','Creative','1005','Tue - Thur');""")
cursor.execute("""INSERT INTO course VALUES(456789,'Buisness','Social Studies','1003','Mon - Wed - Thur');""")
cursor.execute("""INSERT INTO course VALUES(567890,'Algebra','Math','1004','Wed - Fri');""")
cursor.execute("""INSERT INTO course VALUES(135791,'Biology','Science','1002','Mon - Tue - Thur');""")
cursor.execute("""INSERT INTO course VALUES(246824,'Physics','Science','1004','Tue - Thur');""")

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
