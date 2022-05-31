from typing import List, Any

from Node import Node
from MinHeapNode import MinHeapNode


class GraphTemplate:
    nodes: List[Node]

    # __minPriorityQueue

    def __init__(self, min_heap):
        self.adList = {}
        self.nodes = []
        self.is_directed = True
        self.min_prio_heap = min_heap

    # Implement method for adding a node
    def add_node(self, append_node):
        # Don't double add nodes, check if already in graph
        if append_node in self.adList:
            return
        else:
            self.adList[append_node] = append_node.adjNodes
            self.nodes.append(append_node)

    # Implement method for removing a node
    def remove_node(self, delete_node):
        # If Node is not in graph anyway skip
        if delete_node not in self.adList:
            return
        # Remove node from graph and delete all edges containing removed node
        # Edges are still contained in node.adjList -> if added again, edges are re-added too
        else:
            self.adList.pop(delete_node)
            self.nodes.remove(delete_node)
            for node in self.adList:
                for element in self.adList[node]:
                    if element[0] == delete_node:
                        self.adList[node].remove(element)

    def add_edge(self, node1, node2, weight):
        # Check if Graph contains both nodes, if not let user know and return
        if node1 not in self.nodes or node2 not in self.nodes:
            return input("Graph does not contain both nodes, cant connect, check contained nodes! Press Enter to "
                         "continue")
        # Add edge with node function, only add if node does not connect to itself
        b = node1.add_edge_node(node2, weight, self.adList)
        if b is True:
            self.min_prio_heap.push(MinHeapNode(node1, node2, weight))

    # Print all nodes contained in the graph
    def get_all_nodes(self):
        for node in self.nodes:
            print(node.label, "is contained in graph")

    # Print adjacent list of graph (control purpose only)
    def print_adList(self):
        for n in self.adList:
            if self.adList[n] is not None:
                for e in self.adList[n]:
                    print(n.label, " is connected to", e[0].label, ", weight:", e[1])

    # Transfer BST to dot language code and output as txt check at http://magjac.com/graphviz-visual-editor/
    def printGraph(self, mst):
        f = open("MSTcode.txt", "w")
        f.write("digraph MST{\n")
        for node in self.adList:
            for edge in self.adList[node]:
                if mst is not None:
                    if ([node, edge[0], edge[1]]) in mst:
                        f.write(f"{node.label} -> {edge[0].label} [label={edge[1]}, color=red];\n")
                    else:
                        f.write(f"{node.label} -> {edge[0].label} [label={edge[1]}];\n")
                else:
                    f.write(f"{node.label} -> {edge[0].label} [label={edge[1]}];\n")
        f.write("}")
        f.close()

    # build second graph - mst graph with kruskal algorithm
    def kruskal(self):

        def find(index, nodes_list, search_node):
            if parent[index] == search_node:
                return search_node
            return find(nodes_list.index(parent[index]), nodes_list, parent[index])

        def apply_union(parent_list, rank_list, nodes_list, x, y):
            xroot = find(nodes_list.index(x), nodes_list, x)
            yroot = find(nodes_list.index(y), nodes_list, y)
            count_x = 0
            count_y = 0
            for element in parent_list:
                if element == xroot:
                    count_x += 1
                if element == yroot:
                    count_y += 1

            if count_x < count_y:
                parent_list[nodes_list.index(xroot)] = parent_list[nodes_list.index(yroot)]
            elif count_x > count_y:
                parent_list[nodes_list.index(yroot)] = parent_list[nodes_list.index(xroot)]
            else:
                parent_list[nodes_list.index(yroot)] = parent_list[nodes_list.index(xroot)]
                rank_list[nodes_list.index(xroot)] += 1

        #  Applying Kruskal algorithm
        result = []
        all_edges = []
        i, e = 0, 0

        # Generate List and sort according to edge weight
        for node in self.adList:
            print(node)
            for element in self.adList[node]:
                all_edges.append([node, element[0], element[1]])
                all_edges = sorted(all_edges, key=lambda item: item[2])

        parent = []
        rank = []

        # generate parent and rank list:
        for node in self.nodes:
            parent.append(node)
            rank.append(0)

        # Use Lemma to define runtime:
        while e < len(self.nodes) - 1:
            if i < len(all_edges):
                u, v, w = all_edges[i]
                i = i + 1
                x = find(self.nodes.index(u), self.nodes, u)
                y = find(self.nodes.index(v), self.nodes, v)

                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    apply_union(parent, rank, self.nodes, x, y)
            else:
                break

        return result


class Dijkstra:
    nodes: List[Node]

    # __minPriorityQueue

    def __init__(self, min_heap):
        self.adList = {}
        self.nodes = []
        self.is_directed = True
        self.min_prio_heap = min_heap

    # Add Nodes to Graph
    def add_node(self, append_node):
        # Don't double add nodes, check if already in graph
        if append_node in self.adList:
            return
        else:
            self.adList[append_node] = append_node.adjNodes
            self.nodes.append(append_node)

    # Remove nodes from graph
    def remove_node(self, delete_node):
        # If Node is not in graph anyway skip
        if delete_node not in self.adList:
            return
        # Remove node from graph and delete all edges containing removed node
        # Edges are still contained in node.adjList -> if added again, edges are re-added too
        else:
            self.adList.pop(delete_node)
            self.nodes.remove(delete_node)
            for node in self.adList:
                for element in self.adList[node]:
                    if element[0] == delete_node:
                        self.adList[node].remove(element)

    # Adding edges to the graph
    def add_edge(self, node1, node2, weight):
        # Check if Graph contains both nodes, if not let user know and return
        if node1 not in self.nodes or node2 not in self.nodes:
            return input("Graph does not contain both nodes, cant connect, check contained nodes! Press Enter to "
                         "continue")
        # Add edge with node function, only add if node does not connect to itself
        b = node1.add_edge_node(node2, weight, self.adList)
        if b is True:
            self.min_prio_heap.push(MinHeapNode(node1, node2, weight))

    # Print all nodes contained in the graph
    def get_all_nodes(self):
        for node in self.nodes:
            print(node.label, "is contained in graph")

    # Print adjacent list of graph (control purpose only)
    def print_adList(self):
        for n in self.adList:
            if self.adList[n] is not None:
                for e in self.adList[n]:
                    print(n.label, " is connected to", e[0].label, ", weight:", e[1])

    # Transfer BST to dot language code and output as txt check at http://magjac.com/graphviz-visual-editor/
    def printGraph(self, mst):
        f = open("MSTDijkstra.txt", "w")
        f.write("digraph MST{\n")
        for node in self.adList:
            for edge in self.adList[node]:
                if mst is not None:
                    if ([node, edge[0], edge[1]]) in mst:
                        f.write(f"{node.label} -> {edge[0].label} [label={edge[1]}, color=red];\n")
                    else:
                        f.write(f"{node.label} -> {edge[0].label} [label={edge[1]}];\n")
                else:
                    f.write(f"{node.label} -> {edge[0].label} [label={edge[1]}];\n")
        f.write("}")
        f.close()

    # Build graph for Dijkstra
        def dijkstra(self):
            print(" ")
