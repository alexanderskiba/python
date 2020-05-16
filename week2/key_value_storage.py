import argparse
import os
import tempfile

# В функцию будем передавать ключ и значение, по ключу может быть несколько значений
#
def key_value(key1,val1):
    storage = dict()
    if key1 and value1:
        storage[key1] = val1 # добавление в словарь значения при условии существования и ключа и значения
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        with open(storage_path, 'w') as f:
            f.write(storage)

    elif key1:
# Использование библиотеки argparse для получения аргументов (ключа и значения словаря)
parser = argparse.ArgumentParser()
parser.add_argument("--key", help="input key")
parser.add_argument("--val", help="input value")
args = parser.parse_args()

key_value(args.key,args.val) # Передача в функцию аргументов из консоли(ключа и значения)

#https://www.coursera.org/learn/diving-in-python/programming/nc6Ce/key-value-khranilishchie/discussions/threads/mr_3va33EemYeA79agARxg
