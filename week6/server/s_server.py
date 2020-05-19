# сервер
import socket

with socket.socket() as sock:
    sock.bind(("", 8888))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        with conn:
            while True:

                data = conn.recv(1024)
                if not data:
                    break
                storage = dict()
                resp = data.decode().rstrip('\n')
                if 'put' in resp:
                    kek = resp.split(' ')  # делаем список разделяя по пробелу
                    key = kek[1]
                    value = (float(kek[2]), int(kek[3]))

                    if key in kek:
                        if key not in storage:
                            print('if')
                            storage[key] = list()
                        storage[key].append(value)
                        # print(kek)
                        print(storage)
