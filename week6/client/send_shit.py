import socket

with socket.create_connection(("127.0.0.1", 8888)) as sock:
    key = 'palm.cpu'
    value = 'aaa'
    timestamp = 1150864247
    key0 = ''
    keyp = ' '
    key2 = ' 1 2'
    #put palm.cpu 23.7 1150864247 34\n
    sock.sendall(f"put {key} {value} {timestamp} 34\n".encode())
    response = b""
    count = 0
    while True:
        response += sock.recv(1024)
        count += 1
        if count == 3:
            break
    print(response.decode())