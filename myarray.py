from array import array

class ArrayList():
    def __init__(self, typecode, initializer=[]):
        self._xyu = array(typecode, initializer)

    def __len__(self):
        return self._xyu.buffer_info()[1]

    def __getitem__(self, key):
        return self._xyu[key]

    def __contains__(self, item):
        for i in self._xyu:
            if i == item:
                return True
            else:
                return False

    def __iter__(self, start, end):
        current = start
        while current < end:
            yield current
            current += 1

    def __reversed__(self):
        # for i in range(len(self._xyu)-1,0,-1)
        #     return i
        pass
    def index(self):
        pass

    def count(self, x):
        count = 0
        for i in self._xyu:
            count +=1
        return count

a = ArrayList('i')
# print(a.count(1,(1)))

print(a.__len__((1,2,2,5,4)))