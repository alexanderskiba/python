from array import array
class Iterator:
    def __next__(self,start=0,stop,arr):
        self.start = start
        self.stop = stop
        start+=1
        if self.start >= self.stop
            raise StopIteration
        return self.arr[start]
#
# types_dict = {int: 'i', str: 'u', float: 'd'}
# class ArrayList:
#     def __init__(self,typecode,initializer=()):
#         datatype = types_dict[typecode]
#         for x in initializer:
#             if type(x) != typecode:
#                 raise Exception("Wrong initializer datatype")
#         self._arr = array(datatype, initializer)
#
#
#
#     def __getitem__(self, key):
#         return self._arr[key]
#
#     def __len__(self):
#         return self._arr.buffer_info()[1] # buffer_info return a tuple (address, length)
#
#     def __contains__(self, elem):
#         for x in range(self._arr.buffer_info()[1]):
#             if self._arr[x] == elem:
#                 return True
#
#     def __iter__(self):
#         for i in range(self.__len__()):
#             yield self._arr[i]
#
#     def __reversed__(self):
#         return self._arr[::-1]
#
#     def __index__(self,item):
#         for i, x in enumerate(self._arr):
#             if x == item:
#                 return i
#
#     def __count__(self, item):
#         c = 0
#         for x in self._arr:
#             if x == item:
#                 c += 1
#         return c
#
#
# #int
# print('int tests: ')
# print()
# a = ArrayList(int, (1,'x',5,4,3,5,64,43,6))
#
# print('getitem test: ', a.__getitem__(3))
# print('len test: ', a.__len__())
# print('contains test: ', a.__contains__(64))
# print('iter test: ')
# for k in a:
#     print(k, end=' ')
# print()
# print('reversed test: ')
# print(a.__reversed__())
# print('index test: ',a.__index__(64))
# print('count test: ',a.__count__(4))