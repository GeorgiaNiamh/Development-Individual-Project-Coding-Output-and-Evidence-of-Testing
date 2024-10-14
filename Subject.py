class Subject():
#create a subject class
    def __init__(self, name):
        self.name = name
        self.teacher = None
        self.students = []
#adds a teacher to a subject
    def assign_teacher(self,teacher):
        self.teacher = teacher
        print("Teacher ", teacher, " has been assigned to ", self.name)
#adds a student to a subject
    def add_student(self, student):
        self.students.append(student)
        print("Student ", student, " has been added to ", self.name)