import random
import timeit
import matplotlib.pyplot as plt

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1
        self.size = 0
        
    def isEmpty(self):
        return (self.size == 0)
    
    def isFull(self):
        return (self.size == self.capacity)
    
    def enqueue(self, item):
        if self.isFull():
            print("enqueue None")
            return
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head - 1) % self.capacity
        self.queue[self.head] = item
        self.size += 1
        print("enqueue", item)
        
    def dequeue(self):
        if self.isEmpty():
            print("dequeue None")
            return None
        item = self.queue[self.tail]
        print("dequeue", item)
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            print("peek None")
            return None
        item = self.queue[self.tail]
        print("peek", item)
        return item

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedListQueue:
    def __init__(self, capacity=10000):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return (self.size == 0)
    
    def isFull(self):
        return (self.size == self.capacity)
    
    def enqueue(self, item):
        if self.isFull():
            print("enqueue None")
            return
        newNode = Node(item)
        if self.isEmpty():
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.head = newNode
        self.size += 1
        print("enqueue", item)
    
    def dequeue(self):
        if self.isEmpty():
            print("dequeue None")
            return None
        if self.size == 1:
            item = self.tail.value
            print("dequeue", item)
            self.head = None
            self.tail = None
            self.size -= 1
            return item
        item = self.head.value
        print("dequeue", item)
        self.head = self.head.next
        self.tail.next = self.head
        self.size -= 1
        return item

    def peek(self):
        if self.isEmpty():
            print("peek None")
            return None
        item = self.head.value
        print("peek", item)
        return item

def main():
    operations = [
        lambda q: q.dequeue(),
        lambda q: q.peek(),
        lambda q: q.enqueue(1),
        lambda q: q.peek(),
        lambda q: q.enqueue(2),
        lambda q: q.enqueue(3),
        lambda q: q.enqueue(4),
        lambda q: q.enqueue(5),
        lambda q: q.enqueue(6),
        lambda q: q.dequeue(),
        lambda q: q.peek(),
        lambda q: q.dequeue(),
        lambda q: q.enqueue(7),
        lambda q: q.enqueue(8),
        lambda q: q.peek(),
        lambda q: q.dequeue(),
        lambda q: q.dequeue(),
        lambda q: q.dequeue(),
        lambda q: q.dequeue(),
        lambda q: q.dequeue(),
        lambda q: q.peek(),
        lambda q: q.enqueue(9),
        lambda q: q.enqueue(10),
        lambda q: q.enqueue(11),
        lambda q: q.peek(),
        lambda q: q.dequeue(),
        lambda q: q.dequeue(),
        lambda q: q.enqueue(12),
        lambda q: q.enqueue(13),
        lambda q: q.enqueue(14),
        lambda q: q.dequeue(),
        lambda q: q.dequeue(),
        lambda q: q.dequeue(),
        lambda q: q.peek(),
        lambda q: q.enqueue(15),
        lambda q: q.enqueue(16),
        lambda q: q.peek(),
        lambda q: q.dequeue(),
        lambda q: q.enqueue(17),
        lambda q: q.peek()
    ]
    print("Testing ArrayQueue:")
    q1 = ArrayQueue(5)
    for op in operations:
        op(q1)
    print("\nTesting linkedListQueue:")
    q2 = linkedListQueue(5)
    for op in operations:
        op(q2)

if __name__ == "__main__":
    main()
