import asyncio
import re


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    #метод работающий при приеме данных
    def data_received(self, data):
        resp = data.decode().rstrip('\n')
        #сначала метод put
        storage = dict()
        if 'put' in resp:
            kek = resp.split(' ')  # делаем список разделяя по пробелу
            key = kek[1]
            value = (float(kek[2]),int(kek[3]))

            if key in kek:
                if key not in storage:
                    storage[key] = list()
                storage[key].append(value)
                # print(kek)
                print(storage)

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