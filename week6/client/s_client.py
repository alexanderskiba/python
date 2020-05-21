import socket
import time

with socket.create_connection(("127.0.0.1", 8888)) as sock:
    key = 'palm.cpu'
    value = 23.7
    timestamp = 1150864248
    key1 = 'palm.cpu'
    value1 = 25
    timestamp1 = 1000064248
    key2 = 'palm.cpu'
    value2 = 70
    timestamp2 = 1666677248
    key0 = 'eardrum.cpu'
    value0 = 66.6
    timestamp0 = 3336667778

    sock.sendall(f"put {key0} {value0} {timestamp0}\n".encode())
    time.sleep(1)
    sock.sendall(f"put {key1} {value1} {timestamp1}\n".encode())
    time.sleep(1)
    sock.sendall(f"put {key2} {value2} {timestamp2}\n".encode())

    response = sock.recv(1024).decode()
    print(response)
#    sock.sendall("Hello".encode("utf8"))
