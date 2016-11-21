import heapq


class Heaps:
    def __init__(self):
        self.list_elements = []
        self.heap_size = 0

    def push_elements(self, element):
        self.list_elements[self.heap_size] = element
        self.heap_size += 1
        # TO DO : heapify
        self.heapify()

    def get_parent(self, index):
        if index > 0:
            return (index - 1) / 2

    def get_children(self, index):
        left_child_index = 2 * index + 1
        if left_child_index > self.heap_size - 1:
            left_child_index = None
        right_child_index = 2 * index + 2
        if right_child_index > self.heap_size - 1:
            right_child_index = None
        return left_child_index, right_child_index

    def heapify_up(self, index):
        parent = self.get_parent(index)
        if (self.list_elements[parent] <= self.list_elements[index]):
            return


if __name__ == '__main__':
    max_heap = []
    min_heap = []
    max_heap_count = 0
    min_heap_count = 0
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    for element in a:
        if max_heap_count == min_heap_count:
            heapq.heappush(max_heap, -1 * element)
            max_heap_count += 1
        else:
            heapq.heappush(min_heap, element)
            min_heap_count += 1
        if min_heap_count > 0 and -1 * max_heap[0] > min_heap[0]:
            max_value = -1 * max_heap[0]
            heapq.heapreplace(max_heap, -1 * min_heap[0])
            heapq.heapreplace(min_heap, max_value)
        if (max_heap_count + min_heap_count) % 2 == 0:
            print (-1.0 * max_heap[0] + min_heap[0]) / 2
        else:
            print -1.0 * max_heap[0]
