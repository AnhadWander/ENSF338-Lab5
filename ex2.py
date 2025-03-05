import random
import timeit
import time


class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        self.queue = self._merge_sort(self.queue) 

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)
    
    def _merge(self, left, right):
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


class PriorityQueueSorted:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        index = self._find_insertion_index(item)
        self.queue.insert(index, item)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def _find_insertion_index(self, item):
        low, high = 0, len(self.queue)
        while low < high:
            mid = (low + high) // 2
            if self.queue[mid] < item:
                low = mid + 1
            else:
                high = mid
        return low



def generate_tasks(num_tasks=1000):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            val = random.randint(1, 100)
            tasks.append(("ENQUEUE", val))
        else:
            tasks.append(("DEQUEUE", None))
    return tasks


def run_task_list(pq_class, tasks):
    pq = pq_class()
    for action, value in tasks:
        if action == "ENQUEUE":
            pq.enqueue(value)
        else:
            pq.dequeue()

def main():
    list_of_tasks = [generate_tasks() for _ in range(100)]

    start_A = time.time()
    for tasks in list_of_tasks:
        run_task_list(PriorityQueue, tasks)
    end_A = time.time()
    print()
    print(f"PriorityQueue (mergesort) total time: {end_A - start_A:.4f} sec")
    print()

    start_B = time.time()
    for tasks in list_of_tasks:
        run_task_list(PriorityQueueSorted, tasks)
    end_B = time.time()
    print(f"PriorityQueueSorted (search + insert) total time: {end_B - start_B:.4f} sec")
    print()

if __name__ == "__main__":
    main()

'''
    5.)
        As we can clearly see, the PriorityQueueSorted class is much faster than the PriorityQueue class. This is
        because the PriorityQueueSorted class uses a search algorithm, in this case, binary Search, to find the correct
        insertion index for the new element and then inserts the element at that index. This is much faster than the
        PriorityQueue class which uses a merge sort algorithm to sort the entire list after each enqueue request. The merge
        sort algorithm has a time complexity of O(nlogn) which is much slower than the binary search algorithm which
        has a time complexity of O(logn). Therefore, the PriorityQueueSorted class is much faster than the PriorityQueue
        class.
'''
