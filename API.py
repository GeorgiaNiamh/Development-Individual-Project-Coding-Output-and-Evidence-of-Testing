import socket
import threading
import time
import sys
#import from the sms
from SMS import SMS

def save_logfile(strings):
  with open("./logfile.txt", 'w') as f:
    for string in strings:
      f.write(string + '\n')

def handle_client(client_socket, addr, sms, log):
    while True:
        try:
            print("Try")
            data = client_socket.recv(1024)
            if not data:
                break
            query = data.decode()
            print("Users query was: ", query)
            log.append(query)
            save_logfile(log)
            try:
                output = str(eval(query))
            except Exception as e:
                output = f"Error: {e}"
            print("Response sent to user was: ", output)
            client_socket.send(output.encode())
        except ConnectionResetError:
            print("Exception caught")
            break

    client_socket.close()
    print("Client disconnected:", addr)
    sms.log_out()

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen()
    print("Server listening on port 12345")

    sms = SMS()
    print("SMS has been created")

    log = []

    while True:
        client_socket, addr = server_socket.accept()
        print("Client connected:", addr)
        threading.Thread(target=handle_client, args=(client_socket, addr, sms, log)).start()