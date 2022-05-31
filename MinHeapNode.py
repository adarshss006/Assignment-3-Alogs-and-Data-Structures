class MinHeapNode:

    # Only for storing information - MinHeapMode is created whenever a edge is created
    def __init__(self, node1, node2, weight):
        self.edge = [node1, node2]
        self.weight = weight
        self.parent = None
        self.leftChild = None
        self.rightChild = None

