class MyQueue:

    def __init__(self):
        self.d=[]
        

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        if(self.d!=[]):
            k=self.d[0]
            self.d.remove(self.d[0])
            return k


    def peek(self) -> int:
        return self.d[0]
        

    def empty(self) -> bool:
        if len(self.d)==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()