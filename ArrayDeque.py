class ArrayDeque:
    def __init__(self):
        self._data=[]
        self._front=0
    def length(self):
        return len(self._data)
    def is_empty(self):
        return len(self.data)==0
    def first(self):
        return self._data[self._front]
    def add_first(self,e):
        self._data.insert(self._front,e)
    def add_last(self,e):
        self._data.append(e)
    def delete_first(self):
        value=self._data.pop(self._front)
        return value
    def delete_last(self):
        value=self._data.pop()
        return value
    
    
    
deq=ArrayDeque()

deq.add_first(199)
deq.add_first(1212)
deq.add_first(19)
deq.add_first(12)
deq.add_first(99)
deq.add_first(2)
print(deq._data)

deq.add_last(19876)
deq.add_last(78)
deq.add_last(876)
deq.add_last(176)
print(deq._data)
