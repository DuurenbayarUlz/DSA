class Heap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def heappush(self, item):
        self.heap.append(item)

        curr_index = len(self.heap) - 1
        parent_index = (curr_index - 1) // 2

        while parent_index >= 0:
            if self.heap[parent_index] > item:
                self.heap[parent_index], self.heap[curr_index] = self.heap[curr_index], self.heap[parent_index]
                curr_index = parent_index
                parent_index = (curr_index - 1) // 2
            else:
                break

        return self.heap


    def heappop(self):
        if len(self.heap) == 0: raise IndexError("Heap is empty")

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        min_elem = self.heap.pop()
        
        curr_index = 0
        while curr_index < len(self.heap):
            left_child = curr_index * 2 + 1
            right_child = curr_index * 2 + 2
            smallest = curr_index

            if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest == curr_index:
                break

            self.heap[curr_index], self.heap[smallest] = self.heap[smallest], self.heap[curr_index]
            curr_index = smallest

        return min_elem

    def peek(self):
        return self.heap[0]

heap = Heap()
elements = [3,2,1,5,6,4]

for elem in elements:
    heap.heappush(elem)

print("Heap after inserts:", heap.heap)
print("Popped:", heap.heappop())
print("Heap after pop:", heap.heap)