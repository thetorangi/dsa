#dinner plate leetcode 1172
#the answer is not completed its just the practice

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        for i in range(len(self.stack)):
            if len(self.stack[i]) < self.capacity :
                self.stack[i].append(val)
                return None
        if len(self.stack) > 0 and len(self.stack[-1]) < self.capacity:
            self.stack[-1].append(val)
        else:
            self.stack.append([val])
        

        

    def pop(self):
        if len(self.stack) and len(self.stack[-1]) == 0:
            self.stack.pop()
        if len(self.stack) == 0 :
            return None
        else:
            return self.stack[-1].pop()

    def popAtStack(self, index: int):
        if len(self.stack[index]) != 0 :
            return self.stack[index].pop()
        else:
            return False
        

    def disp(self):
        return self.stack
# Your DinnerPlates object will be instantiated and called as such:
obj = DinnerPlates(3)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)

print("\n---------")
print(obj.disp())
print("\n---------")

# print(obj.pop())
# print(obj.pop())
# print(obj.pop())

print(obj.popAtStack(0))
obj.push(7)
obj.push(8)

print("\n---------")
print(obj.disp())
print("\n---------")
# param_2 = obj.pop()
