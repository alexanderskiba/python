import socket

with socket.create_connection(("127.0.0.1", 8888)) as sock:
    key = 'palm.cpu'
    key0 = ''
    keyp = ' '
    key2 = ' 1 2'
    sock.sendall(f"get{key0}\n".encode())
    response = b""
    count = 0
    while True:
        response += sock.recv(1024)
        count += 1
        if count == 3:
            break
    print(response.decode())
