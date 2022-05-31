import heapq as heap
import MinHeapNode


class MinHeap:

    def __init__(self):
        self.heap_list = []

    # Add MinHeapNode to MinHeap, sorting is based on weight
    def push(self, min_heap_node):
        heap.heappush(self.heap_list, (min_heap_node.weight, min_heap_node))
        index = self.heap_list.index((min_heap_node.weight, min_heap_node))

    # Try to get parent and child nodes (if list is too short there are no children, in this case the procedure is
    # skipped)
        try:
            min_heap_node.parent = self.heap_list[(index-1)//2]
            min_heap_node.leftChild = self.heap_list[(2*index)+1]
            min_heap_node.rightChild = self.heap_list[(2*index)+1]

        except IndexError:
            pass

    # Get min element from MinHeap
    def pull(self):
        heap.heappop(self.heap_list)

    # Get min element / root but without popping
    def get_min(self):
        return self.heap_list[0]
