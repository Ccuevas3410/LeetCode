class MyQueue:
    def __init__(self):
        self.queue_list = []
    def enqueue(self,element):
        self.queue_list.append(element)

    def dequeue(self):
        if len(self.queue_list) < 1:
            return None
        return self.queue_list.pop(0)
    def is_empty(self):
        return len(self.queue_list) == 0

    def front(self):
        if len(self.queue_list) < 1:
            return None
        return self.queue_list[0] 

    def back(self):
        if len(self.queue_list) < 1:
            return 0
        return self.queue_list[-1] 

queue  = MyQueue()

for x in range(5):
    queue.enqueue(x)

print(queue.front())

print(queue.back())



