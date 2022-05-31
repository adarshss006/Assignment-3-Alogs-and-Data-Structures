from Graph import GraphTemplate
from Node import Node
from MinHeap import MinHeap


def main():
    min_heap = MinHeap()
    graph = GraphTemplate(min_heap)

    # Kruskal Algo
    # Instantiating nodes
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")

    # Add nodes to Graph
    graph.add_node(a)
    graph.add_node(b)
    graph.add_node(c)
    graph.add_node(d)
    graph.add_node(e)
    graph.add_node(f)
    graph.add_node(g)

    # Add edges with source and destination nodes and weight
    graph.add_edge(a, b, 0.5)
    graph.add_edge(a, d, 11)
    graph.add_edge(c, d, 1)
    graph.add_edge(a, e, 0)
    graph.add_edge(a, c, 3)
    graph.add_edge(c, d, -4.1)
    graph.add_edge(c, e, 2)
    graph.add_edge(e, b, 0.7)
    graph.add_edge(e, g, -1)
    graph.add_edge(e, f, 7)
    graph.add_edge(d, f, 11)

    print("\n")
    graph.remove_node(e)
    kruskal = graph.kruskal()
    graph.printGraph(None)

    # Transfer BST to dot language code and output as txt using printGraph()
    # Check at http://magjac.com/graphviz-visual-editor/
    graph.printGraph(kruskal)
    """
    while 1:
        ch = input("1.Add a node for Kruskal Algorithm\n2.Remove node for kruskal algorithm\n3.Add edge for kruskal "
                   "algorithm\n4.Print Tree\n5.Exit")
        if ch == "1":
            val = input("Enter name of node")
            x = Node(val) 
            graph.add_node(x)
            print("Node " + val + " added")
        elif ch == "2":
            val = input("Enter name of node to be removed")
            graph.remove_node(val)
            print("Node " + val + " removed")
        elif ch == "3":
            fr = input("Enter source node")
            to = input("Enter destination node")
            w = input("Enter weight")
            graph.add_edge(fr, to, w)
        elif ch == "4":
            kruskal = graph.kruskal()
            graph.printGraph(kruskal)
        elif ch == "5":
            print("Exiting program...")
            exit(0)
        else:
            print("Invalid Entry!Try Again!")
            continue
    """


if __name__ == "__main__":
    main()
