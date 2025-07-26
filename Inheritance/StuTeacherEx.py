class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id
    def login(self):
        print(f"{self.name} logged in using {self.email}")
class Student(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.enrolled_courses = []
    def enroll_course(self, course_name):
        self.enrolled_courses.append(course_name)
        print(f"{self.name} has enrolled in {course_name}")
    def login(self):
        print(f"Student {self.name} logged in using {self.email}")
class Teacher(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.created_courses = []
    def create_course(self, course_name):
        self.created_courses.append(course_name)
        print(f"{self.name} has created a course: {course_name}")
    def login(self):
        print(f"Teacher {self.name} logged in using {self.email}")
student1 = Student("Harsha", "harshan3101@gmail.com", "AND654")
teacher1 = Teacher("Shamsheera", "shamsheera@gmail.com", "AND101")
student1.login()
teacher1.login()
student1.enroll_course("Web Programming in python")
teacher1.create_course("Machine Learning")


        
              
