import socket

with socket.create_connection(("127.0.0.1", 8888)) as sock:
    key = 'palm.cpu'
    key_all ='*'
    sock.sendall(f"get {key_all}\n".encode())
    response = b""
    count = 0
    while True:
        response += sock.recv(1024)
        count += 1
        if count == 4: #обратить внимание на количество, чтобы работа завершалась
            break
    print(response.decode())
