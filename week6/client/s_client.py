import socket
import time

with socket.create_connection(("127.0.0.1", 8888)) as sock:
    key = 'palm.cpu'
    value = 23.7
    timestamp = 1150864248
    key1 = 'palm.cpu'
    value1 = 25
    timestamp1 = 1000064248
    sock.sendall(f"put {key} {value} {timestamp}\n".encode())
    time.sleep(1)
    sock.sendall(f"put {key1} {value1} {timestamp1}\n".encode())
#    sock.sendall("Hello".encode("utf8"))
