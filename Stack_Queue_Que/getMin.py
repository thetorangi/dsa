class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.min_below = None  # Store the min value at this point in stack

class MinStack:
    def __init__(self):
        self.head = None  # Top of the stack

    def push(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            new_node.min_below = val  # First node, so it's the min
            self.head = new_node
        else:
            new_node.min_below = min(val, self.head.min_below)  
            new_node.next = self.head  # Link new node
            self.head = new_node  # Update top pointer

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next  # Move head to next node

    def top(self) -> int:
        return self.head.value if self.head else None  # Return top value

    def getMin(self) -> int:
        return self.head.min_below if self.head else None  # Return min value
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.min_below = None  # Store the min value at this point in stack

class MinStack:
    def __init__(self):
        self.head = None  # Top of the stack

    def push(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            new_node.min_below = val  # First node, so it's the min
            self.head = new_node
        else:
            new_node.min_below = min(val, self.head.min_below)  
            new_node.next = self.head  # Link new node
            self.head = new_node  # Update top pointer

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next  # Move head to next node

    def top(self) -> int:
        return self.head.value if self.head else None  # Return top value

    def getMin(self) -> int:
        return self.head.min_below if self.head else None  # Return min value

stack = MinStack()

stack.push(10)
stack.push(20)
stack.push(5)
stack.push(15)
stack.pop()
stack.pop()

print(stack.getMin())
print(stack.top())