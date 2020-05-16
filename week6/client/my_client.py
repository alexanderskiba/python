import socket
import time

class ClientError(Exception):
    '''Пользовательское исключение'''

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((host, port),timeout)

    def put(self, key, value, timestamp =None):
        data = {}
        # data[key] = list()
        # data[key].append((value,timestamp))
        if timestamp == None:
            timestamp = int(time.time())
        send_string = f'put {key} {value} {timestamp}\n'
        self.sock.sendall(send_string.encode("utf-8"))
        # if not self.sock.sendall(send_string.encode("utf-8")):
        #     raise ClientError
        response = self.sock.recv(1024).decode()
        if response =="error\nwrong command\n\n":
            raise ClientError

        # ClientError - если отправка неудачна

    def get(self,key): #Пока рабочий только этот метод
        #принять только данные того ключа, который передали на сервер
        data = {}
        self.sock.sendall(('get '+ key + '\n').encode("utf-8"))
        response = self.sock.recv(1024).decode() # ответ от сервера : 'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
        #если невалидный ответ, то ClientError
        #обработаем ответ:
        kek = response.split('\n')  # делаем список разделяя по переносу строки
        #Проверим валидность

        if response[:2] != 'ok' or 'error' in response or response =="error\nwrong command\n\n" or 'wrong' in response:
            raise ClientError
        # получаем ['ok', 'palm.cpu 10.5 1501864247', 'eardrum.cpu 15.3 1501864259', '', '']
        data = dict()
        if key != '*':
            for i in kek:  # перебираем полученный список
                if key in i:  # если переданный ключ есть в элементе, то дальше работаем только с этим элементом
                    list_i = i.split(' ')  # строку опять разделяем на список по пробелу
                    if key not in data:
                        data[key] = list()
                    data[key].append((int(list_i[2]), float(list_i[1])))  # и запишем в словарь {ключ: [(время,значение метрики), (время2,значение метрики2)]} (list_i[1],list_i[2])]

            return data
        elif key == '*':
            for i in kek:  # перебираем полученный список
                list_i = i.split(' ')  # строку опять разделяем на список по пробелу
                if list_i[0] != 'ok' and list_i[0] != '': # в полученном списке будет лишнее говно типа пустых значений и ок, избавимся от этого
                    key = list_i[0] # получаем чистые значения типа palm.cpu, eardrum.cpu и тд делаем их ключами нашего словаря
                    data[key] = list() # в любом случае значение словаря будет список, в который складываем кортежи
                    data[key].append((int(list_i[2]), float(list_i[1])))  # и запишем в словарь {ключ: [(время,значение метрики), (время2,значение метрики2)]} (list_i[1],list_i[2])]

            return data

    # def get(self, data_key):
    #     """ Receiving data from the server """
    #
    #     if data_key == '*':
    #         self.sock.sendall('get *\n'.encode("utf8"))
    #         data_r = self.sock.recv(1024)
    #     else:
    #         data = 'get {}\n'.format(data_key)
    #         self.sock.sendall(data.encode("utf8"))
    #         data_r = self.sock.recv(1024)
    #
    #     if data_r.decode('utf8') == "error\nwrong command\n\n":
    #         raise ClientError
    #
    #     if data_r.decode('utf8') == "ok\n\n":
    #         return {}
    #     else:
    #         try:
    #             fin_data = dict()
    #             data_r = data_r.decode('utf8').split('\n')
    #             for line in data_r:
    #                 if line and (line not in 'ok'):
    #                     metrica, numb_val, timestamp = line.split()
    #                     # print(metrica, numb_val, timestamp)
    #                     if fin_data.get(metrica):
    #                         fin_data[metrica].append((int(timestamp), float(numb_val)))
    #                     else:
    #                         fin_data[metrica] = [(int(timestamp), float(numb_val))]
    #
    #             for met in fin_data:
    #                 fin_data[met] = sorted(fin_data[met], key=lambda typ: typ[0])
    #
    #             return fin_data
    #         except:
    #             raise ClientError