class array_stack:
    def __init__(self):
        self.data=[]
    def len(self):
        return len(self.data)
    def is_empty(self):
        return len(self.data)==0
    def push(self,value):
        self.data.append(value)
    def pop(self):
        x=self.data[-1]
        self.data.remove(self.data[-1])
        return x
        
        
s=array_stack()
s.push(100)
s.push('hello world')
print(s.data)
