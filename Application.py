from encryption import *
from SMS import SMS
from time import sleep
import socket
#create a connect
class ClientConnection:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 12345))
#send a query to the server
    def query_server(self, string_to_run):
        print("Sending query: ", string_to_run)
        self.client_socket.send(string_to_run.encode())
        response = self.client_socket.recv(1024).decode()
        print("Response recieved: ", response)

        if response.lower() in ['true', 'false']:
            response = bool(response.lower() == 'true')
        return response
#displays the log in menu    
def login_menu(cc):
    while cc.query_server("sms.current_user") == "null":
        user_input = input("Please select one of the following: \n1-Log in \n2-Create new user ")
        if user_input == '1':
            log_in(cc)
        elif user_input == '2':
            create_user(cc)
        else:
            print("Invalid Input")
#allows the user to log in
def log_in(cc):
    username = str(input("Please enter a username: "))
    if cc.query_server(f"sms.verify_username('{username}')"):
        password = input("Please enter a password: ")
        if cc.query_server(f"sms.log_in('{username}', '{password}')"):
            return True
        else:
            print("Please enter a valid Password")
            return False
    else:
        print("Please enter a valid username: ")
        return False
 #allows the user to create a user   
def create_user(cc):
    username = input("Please enter a user name for your new user:")
    if  cc.query_server(f"sms.verify_username('{username}')"):
        print("That username is already taken.")
        return False
    else:
        password = input("Enter a password: ")
        cc.query_server(f"sms.add_user('{username}', '{password}')")
        return True
#allows for different roles to be assigned to different users   
def assign_role(cc):
    print("Which user would you like to assign a role to? Please enter a username")
    search = input()
    if cc.query_server(f"sms.verify_username('{search}')"):
        print("Which role would you like " , search, " to be assigned to?")
        change_role = input()
        print(cc.query_server(f"sms.assign_role('{search}', '{change_role}')"))
    else: 
        print("That user cannot be found")
#displays the roles of different users
def display_roles(cc):
    reponse = cc.query_server("sms.display_roles()")
    print(reponse)

#menu for the role editor
def role_editor(cc):
    if cc.query_server("sms.verify_admin()"):
        print("Welcome to role editor!")
        print("Choose an option below:")
        print("1- Change a user's role")
        print("2- Print all current users and their roles")
        print("3- Delete a user")
        print("4- Return to main menu")
        choice = int(input())
        if choice == 1:
            assign_role(cc)
        elif choice == 2:
            display_roles(cc)
        elif choice == 3:
            delete_user(cc)
        elif choice == 4:
            return
    else:
        print("You do not have access to role editor. You will be returned to the main menu")
#allows for a subject to be added
def add_subject(cc):
    name = input("What would you like the new subject to be called?")
    cc.query_server(f"sms.add_subject('{name}')")

#allows for all the subjects to be printed    
def print_all_subjects(cc):
    response = cc.query_server("sms.print_all_subjects()")
    print(response)
#prints the subjects of the current user
def print_your_subjects(cc):
    response = cc.query_server("sms.print_your_subjects()")
    print(response)
#deletes a user
def delete_user(cc):
    username = input("Which user would you like to delete?")
    if (cc.query_server(f"'{username}' in sms.users.keys()")):
        response = cc.query_server(f"sms.delete_user('{username}')")
        print(response)
    else:
        print(f"'{username}' does not exist and cannot be deleted.")

#assigns a teacher to a subject
def assign_teacher_to_subject(cc):
    teacher = input("Which teacher would you like to assign?")
    if cc.query_server(f"'{teacher}' not in sms.users.keys()"):
        print(teacher, " is not a known username.")
        return
    else:
        if cc.query_server(f"sms.get_users_role('{teacher}') == 'teacher'"):
            print("Which subject would you like to add ", teacher, " to?")
            subject_to_assign = input()
            response = cc.query_server(f"sms.assign_teacher_to_subject('{teacher}','{subject_to_assign}')")
            print(response)
        else:
            print(teacher, "is not a teacher.")
            return
#adds a student to a subject
def assign_student_to_subject(cc):
    student = input("Which student would you like to add to a subject?")
    if cc.query_server(f"'{student}' not in sms.users.keys()"):
            print(student, " is not a known username.")
            return
    else:
        if cc.query_server(f"sms.get_users_role('{student}') == 'student'"):
            print("Which subject would you like to add ", student, " to?")
            subject_to_assign = input()
            response = cc.query_server(f"sms.assign_student_to_subject('{student}', '{subject_to_assign}')")
            print(response)
        else:
            print(student, "is not a student.")
            return
# allows for a user to be removed from a subject        
def delete_user_from_subject(cc):
    print("Please enter the name username of someone you wish to remove:")
    username = input()
    if cc.query_server(f"'{username}' in sms.users.keys()"):
        print("Which subject would you like them to be removed from?")
        selected_subject = input()
        if (cc.query_server(f"sms.verify_subject_exists('{selected_subject}')")):
            response = cc.query_server(f"sms.delete_user_from_subject('{username}', '{selected_subject}')")
            print(response)
        else:
            print("That subject doesn't exist")
    else:
        print("That user doesn't exist")
#menu for subject editor        
def subject_editor(cc):
    if cc.query_server("sms.verify_admin() or sms.verify_teacher()"):
        print("Welcome to subject editor!")
        print("Choose an option below:")
        print("1- Add a subject")
        print("2- Print all subjects")
        print("3- Print your subjects")
        print("4- Assign Teacher to subject")
        print("5- Assign Student to subject")
        print("6- Remove teacher or student from a subject")
        print("7- Return to main menu")
        choice = int(input())
        if choice == 1:
            add_subject(cc)
        elif choice == 2:
            print_all_subjects(cc)
        elif choice == 3:
            print_your_subjects(cc)
        elif choice == 4:
            assign_teacher_to_subject(cc)
        elif choice == 5:
            assign_student_to_subject(cc)
        elif choice == 6:
            delete_user_from_subject(cc)
        elif choice == 6:
            return
    else:
        print("You do not have access to role editor. You will be returned to the main menu")
#allows for security to be switched on or off
def security_manager(cc):
    if cc.query_server("sms.verify_admin()"):
        security_on = input("Do you want to security settings to be <on> or <off>?")
        if security_on in ["on", "ON", "On"]:
            print("Security is on")
        elif security_on in ["off", "Off", "OFF"]:
            print("Security is off, system is vulnerable.")
        else:
            print("Invalid response. You will be returned to the main menu")
    else:
        print("You do not have access to security settings manager. You will be returned to the main menu")

# main menu is defined
def main_menu():

    cc = ClientConnection()

    login_menu(cc)

    while True:
        sleep(1)
        print("\nSchool management system main menu:")
        print("\n1- View users and their roles")
        print("\n2- Role Editor")
        print("\n3- Manage Subjects")
        print("\n4- View your subjects")
        print("\n5- Update Security Settings")
        print("\n6- Log Out")

        choice = input("\nEnter what you want to do (1-6):")
        if choice == '1':
            response = cc.query_server("sms.display_roles()")
            print(response)
        elif choice == '2':
            role_editor(cc)
        elif choice == '3':
            subject_editor(cc)
        elif choice == '4':
            response = cc.query_server("sms.display_subjects()")
            print(response)
        elif choice == '5':
            security_manager(cc)
        elif choice == '6':
            cc.query_server("sms.log_out()")
            login_menu(cc)
        else:
            print("\nThat was an invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()