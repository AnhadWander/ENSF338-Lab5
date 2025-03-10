import random
import time
import matplotlib.pyplot as plt

# Answer to Question 5:
# The execution times for the doubly-linked list implementation were significantly 
# lower than those for the array-based queue.
#
# This is expected because the doubly-linked list maintains both head and tail pointers, 
# allowing enqueue at the head and dequeue at the tail to be performed in O(1) time. 
# These operations involve only a few pointer updates, making them highly efficient.
#
# In contrast, the array-based queue suffers from O(n) complexity when inserting at the head 
# since every element must be shifted. This results in much higher execution times, especially 
# for large numbers of operations.
#
# The histogram confirms this: the DLLQueue consistently performs faster (clustered around ~0.002s),
# whereas the ArrayQueue takes significantly longer (clustered around ~0.006-0.008s), showing the inefficiency
# of shifting elements during enqueue operations.
#
# The performance measurements confirm that the linked list approach is superior for this 
# queue implementation, as it avoids element shifts that occur in the array-based version.

# 1. Queue Implementation  

# (a) Queue using Python array
class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        return None

# 2. Queue using a doubly-linked list
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLLQueue:
    def __init__(self):
        self.head = None  
        self.tail = None  
    
    def enqueue(self, item):
        new_node = DLLNode(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def dequeue(self):
        if self.tail is None:
            return None
        ret_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return ret_data

# 3. Function to generate random tasks
def generate_task_list(num_tasks=10000):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 1000)))
        else:
            tasks.append(("dequeue", None))
    return tasks

# 4. Function to run tasks on a queue
def run_tasks(queue_impl, tasks):
    for op, value in tasks:
        if op == "enqueue":
            queue_impl.enqueue(value)
        elif op == "dequeue":
            queue_impl.dequeue()

# 5. Measure performance  
def measure_performance(num_lists=100, num_tasks=10000):
    array_times = []
    dll_times = []
    
    for _ in range(num_lists):
        tasks = generate_task_list(num_tasks)
        
        # Measure ArrayQueue performance
        aq = ArrayQueue()
        start = time.perf_counter()
        run_tasks(aq, tasks)
        end = time.perf_counter()
        array_times.append(end - start)
        
        # Measure DLLQueue performance
        dq = DLLQueue()
        start = time.perf_counter()  
        run_tasks(dq, tasks)
        end = time.perf_counter()
        dll_times.append(end - start)
    
    return array_times, dll_times

# 6. Plotting  
def plot_results(array_times, dll_times):
    plt.figure(figsize=(10, 6))
    
    min_time = min(min(array_times), min(dll_times))
    max_time = max(max(array_times), max(dll_times))
    
    bins = 20  
    
    plt.hist(array_times, bins=bins, range=(min_time, max_time), alpha=0.5, label='ArrayQueue')
    plt.hist(dll_times, bins=bins, range=(min_time, max_time), alpha=0.5, label='DLLQueue')
    
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Execution Times for 100 Task Lists')
    plt.legend()
    plt.show()

# Main Execution
if __name__ == '__main__':
    array_times, dll_times = measure_performance(num_lists=100, num_tasks=10000)
    
    print("Average time for ArrayQueue: {:.6f} seconds".format(sum(array_times)/len(array_times)))
    print("Average time for DLLQueue: {:.6f} seconds".format(sum(dll_times)/len(dll_times)))
    
    plot_results(array_times, dll_times)
