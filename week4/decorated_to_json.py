# from json import loads, dumps
# from functools import wraps
#
# def to_json(func):
#     @wraps(func)
#     def new_func(*args, **kwargs):
#         return dumps(func(*args, **kwargs))
#     return new_func
#
# @to_json
# def get_data():
#     return {
#         'data': 42
#     }
#
# print()
# get_data()  # вернёт '{"data": 42}'
# print(get_data.__name__)
import json
import functools

def to_json(func):
    def wrapped(*args,**kwargs):
        result = json.dumps(func(*args,**kwargs))
        return result
    return wrapped

@to_json
def get_data():
    return {'data': 42}

print(get_data())

