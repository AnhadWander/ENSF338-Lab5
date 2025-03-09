import random
import timeit
import matplotlib.pyplot as plt

def push(stack, item):
    stack.append(item)

def pop(stack):
    if stack:
        stack.pop()

def push_l(stack, item):
    return {'data': item, 'next': stack}

def pop_l(stack):
    return stack['next'] if stack else None

def create_tasks():
    return [('push', random.randint(1, 100)) if random.random() < 0.7 else ('pop',) for i in range(10000)]

def performance(stack_type, tasks):
    if stack_type == 'array':
        stack = []
        def run_tasks():
            for task in tasks:
                if task[0] == 'push':
                    push(stack, task[1])
                else:
                    pop(stack)
        return timeit.timeit(run_tasks, number=1)

    elif stack_type == 'linked_list':
        stack = None
        def run_tasks():
            nonlocal stack
            for task in tasks:
                if task[0] == 'push':
                    stack = push_l(stack, task[1])
                else:
                    stack = pop_l(stack)
        return timeit.timeit(run_tasks, number=1)

task_lists = [create_tasks() for i in range(100)]


arr_stack = [performance('array', tasks) for tasks in task_lists]
link_stack = [performance('linked_list', tasks) for tasks in task_lists]


print("Average Array Stack time:", sum(arr_stack) / len(arr_stack))
print("Average Linked List Stack time:", sum(link_stack) / len(link_stack))

plt.figure(figsize=(10, 10))
plt.plot(arr_stack, label='Array Stack')
plt.plot(link_stack, label='Linked List Stack')
plt.xlabel('Task List Index')
plt.ylabel('Time (seconds)')
plt.title('Performance of Stack Implementations')
plt.legend()
plt.savefig('Performance.jpeg')


""" The Array Stack has lower time as compared to the Linked List Stack becuase the 
append and pop operations have O(1) complexity."""
