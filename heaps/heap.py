import math

class MinHeap:
    def __init__(self, initial_size=10):
        self.cbt = [None] * initial_size  # initialize array
        self.next_index = 0  # denotes next index where new element should go
    
    def insert(self, data):
        # Expand heap if necessary
        if self.next_index >= len(self.cbt):
            self.cbt.append(None)  # Expand array dynamically
        
        # Insert new element
        self.cbt[self.next_index] = data
        current = self.next_index
        self.next_index += 1

        # Heapify up (fix heap property)
        while current > 0:
            parent_index = (current - 1) // 2
            if self.cbt[parent_index] > self.cbt[current]:
                self.cbt[parent_index], self.cbt[current] = self.cbt[current], self.cbt[parent_index]
                current = parent_index
            else:
                break
    
    def parent(self, value):
        if value == 0:
            return -1
        return (value - 1) // 2
    
    def left_child(self, n):
        return 2 * n + 1  # Corrected formula for left child

    def right_child(self, n):
        return 2 * n + 2  # Added right child method
    
    def heapify(self, n):
        left = self.left_child(n)
        right = self.right_child(n)
        smallest = n        
        # Compare with left child
        if left < self.next_index and self.cbt[left] is not None and self.cbt[left] < self.cbt[smallest]:
            smallest = left
        # Compare with right child
        if right < self.next_index and self.cbt[right] is not None and self.cbt[right] < self.cbt[smallest]:
            smallest = right

        # Swap and continue heapifying if needed
        if smallest != n:
            self.cbt[n], self.cbt[smallest] = self.cbt[smallest], self.cbt[n]
            self.heapify(smallest)
    
    def remove(self):
        if self.next_index <= 0:
            raise ValueError('Heap underflow')
        
        min_value = self.cbt[0]
        self.next_index -= 1
        self.cbt[0] = self.cbt[self.next_index]  # Move last element to root
        self.cbt[self.next_index] = None  # Clear last element
        
        # Heapify down
        self.heapify(0)
        
        return min_value
