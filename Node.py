
class Node:

    def __init__(self, label):
        self.label = label
        self.adjNodes = []
        self.parent = self
        self.distance = None

    # Implement method for adding a connection
    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge_node(self, v2, e, adList):
        # Check if edge is to itself if yes, don't connect:
        if self.label == v2.label:
            print("Cant connect node to itself!")
            return False
        # Check if edge is already existent if yes don't connect:
        # Implement function to change weight??
        if adList[self]:
            for element in adList[self]:
                if element[0] == v2:
                    return False

        # Add edge
        self.adjNodes.append([v2, e])
        adList[self] = self.adjNodes
        return True

    # Implement method for removing a connection
    def remove_edge(self, v2, adList):
        for e in self.adjNodes:
            if e[0] == v2:
                temp = self.adjNodes
                temp.remove(e)
                self.adjNodes = temp

    # Implement methods for manipulating the parent and distance??
    @staticmethod
    def get_parent(node):
        return node.parent

    @staticmethod
    def set_parent(node, parent):
        node.parent = parent

