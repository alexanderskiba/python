class ArrayList():
    def __init__(self, typecode, initializer=[]):
        self._xyu = array(typecode, initializer)

    def __len__(self):
        return self._xyu.buffer_info()[1]

    def __getitem__(self, key):
        return self._xyu[key]

    def count(self, x):
        return self._xyu.count(x)