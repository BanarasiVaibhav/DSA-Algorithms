class Array_Queue:
    def __init__(self):
        self.data=[]
        self._size=0
        self.front=0
    def length(self):
        return len(self.data)
    def is_empty(self):
        return self._size==0
    def enqueue(self,value):
        self.data.append(value)
        self._size+=1
        return self.data
    def dequeue(self):
        x=self.data[0]
        self.data=self.data[1:]
        print(self.data)
        return x
    def first(self):
        return self.data[0]
obj1=Array_Queue()
        
obj1.enqueue(100)
obj1.enqueue(200)
obj1.enqueue(300)
obj1.length()
obj1.dequeue()
obj1.dequeue()
