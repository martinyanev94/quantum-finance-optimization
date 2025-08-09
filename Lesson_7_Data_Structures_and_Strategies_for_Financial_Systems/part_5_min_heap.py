import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def extract_min(self):
        return heapq.heappop(self.heap) if self.heap else "Heap is empty"

    def get_min(self):
        return self.heap[0] if self.heap else "Heap is empty"
