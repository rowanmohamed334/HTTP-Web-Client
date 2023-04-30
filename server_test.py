import socket

# import thread module
import time
from _thread import *
import threading
import os.path
from os import path

print_lock = threading.Lock()


# thread function
def threaded(c):
    while True:
        # time.sleep(10)
        # data received from client
        data = c.recv(1024)
        # print("check data", type(data))
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break
        # decode and parse the data received
        decoded_data = bytes.decode(data)
        # print("parse", type(decoded_data))
        command_list = decoded_data.split("/")
        command_list[1], unused = command_list[1].split()
        # print("test list:", command_list)

        # find out which command 'GET or POST'
        if command_list[0] == 'GET':
            print("GET is received")
            if path.exists(command_list[1]):
                req_file = open(command_list[1], mode="r")
                content = req_file.read()
                file_response = f'HTTP/1.0 200 OK\r\n\r\n{content}\r\n'
                c.send(file_response.encode('utf-8'))
            else:
                c.send(b"HTTP/1.0 404 Not Found\\r\\n\\r\\n")
            # finally:
            #     req_file.close()
        elif command_list[0] == 'POST':
            c.send(b"HTTP/1.0 200 OK\\r\\n\\r\\n")
            reqb, data = decoded_data.split(f'\r\n\r\n')
            f = open(f'{command_list[1]}.output', 'w+')
            f.write(data)
            f.close()

        # # send back reversed string to client
        # c.send(data)

        # connection closed
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)
    # time.sleep(10)
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '_main_':
    Main()