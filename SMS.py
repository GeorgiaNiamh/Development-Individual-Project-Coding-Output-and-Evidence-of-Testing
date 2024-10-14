from encryption import *
from Subject import Subject

class SMS():
    """the sms class"""
    def __init__(self, security_on=True):
        print("SMS Created")
        self.current_role = "null"
        self.current_user = "null"

        self.security_on = security_on
        #dict of users, starts empty or with an admin
        #keys are usernames, hashed passwords are values
        default_password = "password"
        self.users = {
            "defaultstudent": encrypt_password(default_password),
            "defaultteacher": encrypt_password(default_password),
            "defaultadmin": encrypt_password(default_password)
        }
        self.roles = {
            "student": ["defaultstudent"],
            "teacher": ["defaultteacher"],
            "admin": ["defaultadmin"]
         }
        
        self.subjects = [Subject("English"), Subject("French")]

    def add_user(self, username, password):
        """create a function to add a user"""   
        hashed_password = encrypt_password(password)
        self.users.update({username : hashed_password})
        self.roles["student"].append(username)
        return True
       
    def verify_username(self, username):
        """function to check if the username is already taken"""
        if username in self.users.keys():
            return True
        else:
            return False
    
    def delete_user(self, username):
        """function to delete a user"""
        for subject in self.subjects:
            self.delete_user_from_subject(username, subject.name)
        for role in self.roles.keys():
            if username in self.roles[role]:
                self.roles[role].remove(username)
        del self.users[username]

        return f"{username} has been removed from the database."

    def log_in(self, username, password):
        """function that allows the user to log in by checking username and password"""
        if check_password(password, self.users[username]):
            self.current_user = username
            self.current_role = self.get_users_role(username)
            return True
        else:
            return False
       
    def log_out(self):
        """log the user out"""
        self.current_role = "null"
        self.current_user = "null"

    def verify_teacher(self):
        """check if the current user is a teacher"""
        if self.security_on == False:
            return True
        elif self.current_role == "teacher":
            return True
        else:
            return False

    def verify_admin(self):
        """checks if the current user is an admin"""
        if self.security_on == False:
            return True
        elif self.current_role == "admin":
            return True
        else:
            return False

    def get_users_role(self, user):
        """checks the users role or adds them to the student role"""
        for role in self.roles.keys():
            if user in self.roles[role]:
                return role
            else:
                continue
        self.roles["student"].append(user)
        return "student"

    def assign_role(self, user, role):
        """assigning roles"""
        if role in self.roles.keys():
            self.roles[self.get_users_role(user)].remove(user)
            self.roles[role].append(user)
            return f"{user}, has been assigned the role of {role}."
        else:
            return "That is not a valid role!"


    def display_roles(self):
        """print all users and their roles"""
        return f"Below is a list of all roles and their users: {self.roles}"

    def add_subject(self, name):
        """adds a new subject"""
        self.subjects.append(Subject(name))

    def print_all_subjects(self):
        """prints all the current subjects out"""
        base_string = "Below is a list of all subjects:\n"
        for sub in self.subjects:
            base_string += f"{sub.name}\n"
        return base_string

    def verify_subject_exists(self, subject_name):
        """checks if a subject exists"""
        for s in self.subjects:
            if s.name == subject_name:
                return True
        return False

    def get_subject_by_name(self, subject_name):
        """searches for a subject by name"""
        for s in self.subjects:
            if s.name == subject_name:
                return s
        return False

    def print_your_subjects(self):
        """prints out all the subjects a user is registered in"""
        base_string = "Below is a list of your subjects:\n"
        for sub in self.subjects:
            if self.current_user in sub.students:
                base_string += f"{sub.name} as student.\n"
            if self.current_user == sub.teacher:
                base_string += f"{sub.name} as teacher.\n"
        return base_string

    def assign_teacher_to_subject(self, teacher, subject_to_assign):
        """adds a teacher to a subject"""
        for subject in self.subjects:
            if subject_to_assign == subject.name:
                subject.assign_teacher(teacher)
                return(f"{teacher} has been assigned as a teacher to {subject_to_assign}")
        return(f"{subject_to_assign} is not the name of a subject.")
        

    def assign_student_to_subject(self, student, subject_to_assign):
        """adds a student to a subject"""
        subject = self.get_subject_by_name(subject_to_assign)
        if subject:
            subject.add_student(student)
            return f"{student} has been added as a student to {subject_to_assign}"
        else:
            return f"{subject} is not the name of a subject."

    def display_subjects(self):
        """displays all the subjects for the current user"""
        if self.current_user in self.roles['teacher']:
            response = "These are the classes you teach: \n"
            for subject in self.subjects:
                if self.current_user == subject.teacher:
                    response += f"{subject.name}\n"
            return response
        elif self.current_user in self.roles['student']:
            response = "These are the classes you are a student in: "
            for subject in self.subjects:
                if self.current_user in subject.students:
                    response += f"{subject.name}\n"
            return response
        else:
            return f"You don't have any classes because your role is {self.current_role}"

    def delete_user_from_subject(self, user, subject_name):
        """removes a user from a subject can be student or teacher."""
        subject_to_remove_from = None
        for subject in self.subjects:
            if subject.name == subject_name:
                subject_to_remove_from = subject
        if subject_to_remove_from is None:
            return f"{subject_name} does not exist."
        if user == subject_to_remove_from.teacher:
            subject_to_remove_from.teacher = None
            return(f"{user} has been removed as a teacher from {subject_name}")
        elif user in subject_to_remove_from.students:
            subject_to_remove_from.students.remove(user)
            return(f"{user} has been removed as a student from {subject_name}")
        else:
            return(f"{user} was not found in that subject")
