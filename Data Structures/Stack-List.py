class Stack:
    def __init__(self):
        self.stack_list =[]

    def is_empty(self):
        return self.size() == 0

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        if self.is_empty():
            return 0
        self.stack_list.pop()
    def top(self):
        if self.is_empty():
            return 0
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)



myStack = Stack()

for i in range(5):
    myStack.push(i)

for i in range(5):
    print(myStack.top())
    myStack.pop()

