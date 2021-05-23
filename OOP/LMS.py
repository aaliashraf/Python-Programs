## This program is subject to be evaluated for the Technical Assessignment of ASE Position at System Plus 
import mysql.connector as mysql
mydb = mysql.connect(host="localhost",
                     user="root", password="", database="lms")
lms_db = mydb.cursor()


class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def student_login(self, username, password):

        query = (self.username, self.password, 'student')
        lms_db.execute(
            "SELECT id FROM users WHERE username = %s AND password = %s AND identity = %s", query)
        if not lms_db.fetchone():
            print("Invalid")
        else:
            id = [i[0][0] if i else None for i in lms_db.fetchon()]
            std = Student()
            std.course_enroll(id)

    def instructor_login(self, username, password):

        query = (self.username, self.password, 'instructor')
        lms_db.execute(
            "SELECT username FROM users WHERE username = %s AND password = %s AND identity = %s", query)
        if not lms_db.fetchone():
            print("Invalid")
        else:
            id = [i[0][0] if i else None for i in lms_db.fetchon()]
            inst = Instructor()
            inst.my_course(id)


class Student(User):
    def __init__(self):
        print(""" 1. View Marks
                  2. View Course
                  3. View Assignemt""")
    choice = int(input())
    if choice == 1:
        view_marks()
    elif choice == 2:
        view_course()
    elif choice == 3:
        view_assign()

    def view_marks(self, id):
        query = (self.id)
        sql = ("SELECT obt_marks,total_marks FROM marks where std_id=%d")
        lms_db.execute(sql, query)
        result = lms_db.fetchon()
        for i in result:
            return i

    def view_course(self, id):
        self.id = id
        query = (self.id)
        sql = ("SELECT course_name FROM course WHERE std_id = %d ")
        lms_db.execute(sql, query)
        result = lms_db.fetchon()
        for i in result:
            return i

    def view_assign(self, id):
        self.id = id
        query = (self.id)
        sql = ("SELECT assign FROM assignment  JOIN course on course.id=assignment.course_id where course.std_id=%d", query)
        lms_db.execute(sql)
        result = lms_db.fetchon()
        for e in result:
            return e


class Instructor(User):
    def __init__(self):
        print("""
                 1. Check MY Courses
                 2. Grade Student
        """)
    if choice == 1:
        my_course()
    elif choice == 2:
        grade()

    def my_course(self, id):
        self.id = id
        sql = ("SELECT course_name FROM course WHERE std_id = %d ")
        lms_db.execute(sql, query)
        result = lms_db.fetchon()
        for i in result:
            return i

    def grade(self, id):
        self.id = id
        student = input(str("Student ID"))
        course = input(str("Course ID"))
        obtain = float(input("Obtain Marks"))
        total = int(input("Total Marks"))
        sql = ("INSERT INTO marks (std_id,inst_id, course_id,obt_marks,total_marks) VALUES ({},{},{},{})".
               format(student, id, course, obtain, total))
        lms_db.execute(sql)
        lms_db.commit()


def main():

    print("""   === Learning Management System === 
            1. Student Login
            2. Instructor Login """)
    choice = int(input("Select Option :"))
    if choice == 1:
        print("Student Section")
        username = input(str("USERNAME :"))
        password = input(str("PASSWORD :"))
        obj = User(username, password)
        obj.student_login(username, password)

    elif choice == 2:
        print("Instructor Section")
        username = input(str("USERNAME :"))
        password = input(str("PASSWORD :"))
        obj = User(username, password)
        obj.instructor_login(username, password)


main()
