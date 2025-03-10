import random
import timeit
import matplotlib.pyplot as plt

# Answer to Question 5:
# The execution times for the linked list implementation were significantly 
# higher than those for the array-based queue.
#
# This is expected because linked list operations involve additional pointer 
# manipulation, particularly during dequeue operations where the list must be 
# traversed to update the tail pointer.
#
# In contrast, array operations benefit from direct indexing, which generally 
# leads to lower overhead and faster performance.




# 1. Queue Implementation  

# (a) Queue using Python array
class QueueArray:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        
        self.queue.insert(0, item)
    
    def dequeue(self):
       
        if not self.queue:
            raise IndexError("dequeue from empty queue")
        return self.queue.pop()


# (b) Queue using a singly-linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class QueueLinked:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def enqueue(self, item):
        new_node = Node(item)
        if self.head is None:  
            self.head = self.tail = new_node
        else:
            
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        
        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            return value
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        return value



def generate_tasks(num_tasks=10000, enqueue_prob=0.7):
    """
    Generates a list of 'num_tasks' tasks.
    Each task is a tuple: ("enqueue", value) with probability 0.7,
    or ("dequeue", None) with probability 0.3.
    """
    tasks = []
    for _ in range(num_tasks):
        if random.random() < enqueue_prob:
            
            tasks.append(("enqueue", random.randint(1, 100)))
        else:
            tasks.append(("dequeue", None))
    return tasks



def run_tasks_queue_array(tasks):
    """
    Runs a list of tasks on QueueArray.
    Enqueues insert at head and dequeues remove from tail.
    """
    q = QueueArray()
    for op, value in tasks:
        if op == "enqueue":
            q.enqueue(value)
        else:  
            try:
                q.dequeue()
            except IndexError:
                pass  
    return q

def run_tasks_queue_linked(tasks):
    """
    Runs a list of tasks on QueueLinked.
    Enqueues add at head and dequeues remove from tail.
    """
    q = QueueLinked()
    for op, value in tasks:
        if op == "enqueue":
            q.enqueue(value)
        else:
            try:
                q.dequeue()
            except IndexError:
                pass
    return q


def measure_performance(queue_runner, tasks):
    """
    Measures the time it takes for 'queue_runner' to process 'tasks'.
    Uses timeit with a single iteration.
    """
    timer = timeit.Timer(lambda: queue_runner(tasks))
    return timer.timeit(number=1)

num_experiments = 100
array_times = []
linked_times = []

for _ in range(num_experiments):
    tasks = generate_tasks()
    t_array = measure_performance(run_tasks_queue_array, tasks)
    t_linked = measure_performance(run_tasks_queue_linked, tasks)
    array_times.append(t_array)
    linked_times.append(t_linked)


# 5. Plotting


plt.hist(array_times, bins=20, alpha=0.5, label='QueueArray')
plt.hist(linked_times, bins=20, alpha=0.5, label='QueueLinked')
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of Execution Times for 10,000 Tasks (100 Runs)")
plt.legend()
plt.show()

avg_array = sum(array_times) / len(array_times)
avg_linked = sum(linked_times) / len(linked_times)
print("Average time for QueueArray: {:.6f} seconds".format(avg_array))
print("Average time for QueueLinked: {:.6f} seconds".format(avg_linked))
