import asyncio



class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.storage = dict()

    def connection_made(self, transport):
        self.transport = transport

    #метод работающий при приеме данных
    def data_received(self, data):
        resp = data.decode().rstrip('\n')
        #сначала метод(на стороне клиента) put, сложим данные в словарь
        if 'put' in resp:
            kek = resp.split(' ')  # делаем список разделяя по пробелу
            key = kek[1]
            value = (float(kek[2]),int(kek[3]))

            if key in kek:
                if key not in self.storage:
                    self.storage[key] = list()
                self.storage[key].append(value)
                # print(kek)
                #отправить ответ вместо print
                # отвечаем клиенту ok\n\n
                self.transport.write(''.encode())
                print(self.storage)
        # метод, отправляющий клиенту значение требуемого ключа
        # get palm.cpu\n - запрос клиента
        # ok\npalm.cpu 2.0 1150864248\n
        # if 'get' in resp:


        self.transport.write(resp.encode())


def run_server(host, port):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)
    print('Сервер запущен')

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


run_server('127.0.0.1', 8888)