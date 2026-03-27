import time
class stack:
    def __init__(self,size):
        self.stack=[0]*size
        self.top=-1
        self.size=size
    def isempty(self):
        return self.top==-1
    def isfull(self):
        return self.top==self.size-1
    def push(self,element):
        if self.isfull():
            print("stack overflow")
        else:
            self.top=self.top+1
            self.stack[self.top]=element
            print("pushed element is:",element)
    def pop(self):
        if self.isempty():
            print("underflow condition")
        else:
            popped=self.stack[self.top]
            self.top=self.top-1
            print("popped element is:",popped)
    def display(self):
        if self.isempty():
            print("no element in the stack")
        else:
            print("stack elements are:")
            for i in range(self.top,-1,-1):
                print(self.stack[i])
    def peek(self):
        if self.isempty():
            print("stack is empty")
        else:
            print("peek element is:",self.stack[self.top])
s=stack(5)
start=time.time()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.peek()
s.display()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.peek()
s.display
end=time.time()
print("runtime is:",end-start)
    
