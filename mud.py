from constants import debug, clients
import socket
import threading
from classes import heartbeat
from engine.login import login
from engine.start_mud import StartMud

HOST = ""
PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

import threading
import time

StartMud()

timer = heartbeat.Heartbeat().start()

if debug.debug:
    if __name__ == "__main__":
        login()
else:
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        while True:
            conn, addr = server_socket.accept()
            clients.clients[conn] = addr
            new_thread = threading.Thread(target=login, args=(conn, addr))
            new_thread.start()
    finally:
        server_socket.close()
