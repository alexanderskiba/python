import asyncio
import time

dictionary = dict()

# На каждого клиента свое соединение
class ClientServerProtocol(asyncio.Protocol):
    # def __init__(self):
        # dictionary = dict()

    def connection_made(self, transport):
        self.transport = transport

    #метод работающий при приеме данных
    def data_received(self, data):
        resp = data.decode().rstrip('\n')
        valid = resp.split(' ')
        if valid[0] != 'put' and valid[0] != 'get' or len(valid) > 4:
            err = 'error\nwrong command\n\n'
            self.transport.write(err.encode())
        # elif valid[0] == 'get' and valid[1] == '*' and len(dictionary) == 0:
        #     self.transport.write('ok\n\n'.encode())
        else:
            #сначала метод(на стороне клиента) put, сложим данные в словарь
            if 'put' in resp:
                kek = resp.split(' ')  # делаем список разделяя по пробелу
                # print (kek)
                if not isinstance(kek[2], float) and isinstance(kek[3], float):
                    err = 'error\nwrong command\n\n'
                    self.transport.write(err.encode())
                else:
                    key = kek[1]
                    value = (float(kek[2]),int(kek[3]))

                    if key not in dictionary:
                        dictionary[key] = list()
                    dictionary[key].append(value)
                    # print(kek)
                    #отправить ответ вместо print
                    # отвечаем клиенту ok\n\n
                    self.transport.write('ok\n\n'.encode())
                    # print(dictionary)
                # метод, отправляющий клиенту значение требуемого ключа
                # get palm.cpu\n - запрос клиента
                # ok\npalm.cpu 2.0 1150864248\n
            elif 'get' in resp:
                if '*' in resp:
                    if len(dictionary) != 0:

                        self.transport.write(('ok\n').encode())
                        #вывод из словаря в формате ok\npalm.cpu 2.0 1150864248\npalm.cpu 70.0 1666677248\n\n
                        for kl, val in dictionary.items():
                            for i in val:
                                ans_str = f'{kl} {i[0]} {i[1]}\n'
                                self.transport.write(ans_str.encode())
                        self.transport.write('\n\n'.encode())

                    elif len(dictionary) == 0:
                        self.transport.write(('ok\n\n').encode())


                else:
                    if resp == 'get ' or resp == 'get  ':
                        err = 'error\nwrong command\n\n'
                        self.transport.write(err.encode())
                    else:
                        kek = resp.split(' ')  # делаем список разделяя по пробелу
                        if len(kek) ==1 or kek[1] not in dictionary:
                            err = 'error\nwrong command\n\n'
                            self.transport.write(err.encode())
                        else:
                            key = kek[1] # ключ словаря
                            # Теперь из словаря dictionary нужно достать значение и передать в формате:
                            # ok\npalm.cpu 2.0 1150864248\n
                            # возможно необходимо будет добавить условие на существование ключа в словаре

                            self.transport.write(('ok\n').encode())

                            for i in dictionary[key]:
                                answer = f'{key} {i[0]} {i[1]}\n'
                                # print(answer)
                            # get test_key
                            # < ok
                            # < test_key 13.0 1503319739 выдать в формате ключ - первый кортеж из списка,
                            # < test_key 12.0 1503319740 потом ключ - второй кортеж из списка и тд(проитерироваться по списку)
                                self.transport.write((answer).encode()) # проблема здесь write пишет только до \n!!!!!
                                #заработало, но непонятно почему

            else:
                err = 'error\nwrong command\n\n'
                self.transport.write(err.encode())



def run_server(host, port):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)
    # print('Сервер запущен')

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


# run_server('127.0.0.1', 8888)