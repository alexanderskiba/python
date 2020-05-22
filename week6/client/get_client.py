import socket
import time

with socket.create_connection(("127.0.0.1", 8888)) as sock:
    key = 'palm.cpu'
    value = 23.7
    timestamp = 1150864248
    key0 = 'eardrum.cpu'
    value1 = 25
    timestamp1 = 1000064248
    # sock.sendall(f"put {key} {value} {timestamp}\n".encode())
    # time.sleep(1)
    # sock.sendall(f"put {key1} {value1} {timestamp1}\n".encode())
    sock.sendall(f"get {key}\n".encode())
    response = b""
    count = 0
    while True:
        response += sock.recv(1024)
        count += 1
        if count == 3:
            break
    print(response.decode())

    # response = sock.recv(1024).decode()
    # response1 = sock.recv(1024).decode()
    # response2 = sock.recv(1024).decode()
    # print(response)
    # print(response1)
    # print(response2)
