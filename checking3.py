import socket
import os
import time
HOST = '127.0.0.1'
PORT = 6958

while True:
    # create a TCP socket and bind it to the specified address and port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(1)  # allow only one client to connect at a time
    # wait for a client to connect
    print('Waiting for connection...')
    conn, addr = sock.accept()
    print('Connected by', addr)

    # execute the specified commands
    os.system("/etc/init.d/logmein-hamachi restart")
    time.sleep(10)
    os.system("/usr/bin/hamachi logon")
    print('Executed commands')

    # close the connection with the client
    conn.close()
    sock.close()

