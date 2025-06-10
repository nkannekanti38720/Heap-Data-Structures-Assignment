# priority_queue.py

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority > other.priority  # Max-heap, higher priority tasks come first

    def __repr__(self):
        return f"Task({self.task_id}, {self.priority}, {self.arrival_time}, {self.deadline})"

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_task = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_task

    def increase_key(self, task, new_priority):
        index = self._find_task_index(task)
        if index != -1:
            self.heap[index].priority = new_priority
            self._heapify_up(index)

    def decrease_key(self, task, new_priority):
        index = self._find_task_index(task)
        if index != -1:
            self.heap[index].priority = new_priority
            self._heapify_down(index)

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] < self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] < self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def _find_task_index(self, task):
        for i, t in enumerate(self.heap):
            if t.task_id == task.task_id:
                return i
        return -1


# --- Test Case --- #
if __name__ == "__main__":
    # Create a Priority Queue
    pq = PriorityQueue()

    # Insert tasks into the priority queue
    pq.insert(Task(1, 5, '2025-06-10 09:00', '2025-06-10 12:00'))
    pq.insert(Task(2, 8, '2025-06-10 10:00', '2025-06-10 13:00'))
    pq.insert(Task(3, 3, '2025-06-10 11:00', '2025-06-10 14:00'))

    print("Priority Queue after inserts:")
    print(pq.heap)

    # Extract the task with the highest priority (task with the highest priority number)
    max_task = pq.extract_max()
    print("\nExtracted task with the highest priority:")
    print(max_task)

    # Show the current state of the priority queue after extraction
    print("\nPriority Queue after extraction:")
    print(pq.heap)

    # Test increase_key and decrease_key
    pq.increase_key(Task(3, 3, '2025-06-10 11:00', '2025-06-10 14:00'), 10)
    print("\nPriority Queue after increasing key of task 3:")
    print(pq.heap)

    pq.decrease_key(Task(2, 8, '2025-06-10 10:00', '2025-06-10 13:00'), 2)
    print("\nPriority Queue after decreasing key of task 2:")
    print(pq.heap)
