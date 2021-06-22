# Class Queue will implement abstract data structure queue (First in - First out)
class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self,data):
        self.queue.append(data)

# this method is not efficient: array will have to realign itself (O(n) running time)
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1

    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)
