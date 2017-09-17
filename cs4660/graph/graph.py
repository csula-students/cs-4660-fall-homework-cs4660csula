"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""
# https://stackoverflow.com/questions/39813525/how-do-i-store-this-in-an-adjacency-list-for-graphs-in-python 
from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):

     


    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph

    """
    try:
        fhand = open('mbox-short.txt')
    except:
        print('File not found, lol, what happened?')
        exit()
    count = 0
    for line in fhand:
        count = count + 1;
    print('Line count:', count)

    # Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Locations 1543-1544). Kindle Edition. 

    # fhand = open('mbox-short.txt')
    # inp = fhand.read()
    # print(len(np))
    # alternative method to read files   


    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        assert self.has_node(node1)
        assert self.has_node(node2)
        self._nodes[node1].add(node2)
        
        # https://github.com/udacity/cs101/blob/master/Lesson_11_Files,_IO,_and_Exceptions/26-Pickle_the_Crawl/supplied/graph.py

        # https://stackoverflow.com/questions/36732312/python-build-adjacency-list-from-list-of-nodes-and-edges

        # https://stackoverflow.com/questions/39813525/how-do-i-store-this-in-an-adjacency-list-for-graphs-in-python

        # Homework help with the graphs https://github.com/agore1/cs3240/blob/master/HW3/graph.py

    def neighbors(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)
            self.neighbors.sort()

        

    def add_node(self, node):
        if node in self._nodes:
            return false
        self._nodes[node] = set()
        return true
        
     # Removes a given node from a graph.
     # https://brilliant.org/wiki/graphs-intermediate/
    def remove_node(self, node):
        for node in self.nodes:
            if node in self.nodes[node]:
                self.nodes[node].remove(node)
        del self.nodes(node)
        
        # https://codereview.stackexchange.com/questions/120496/a-graph-representation-of-adjacent-matrix-in-python
    def add_edge(self, edge):
        self.edge.append(edge)
        

    def remove_edge(self, edge):
        self.edge.discard(edge)
        

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        

    def neighbors(self, node):
        

    def add_node(self, node):
        

    def remove_node(self, node):
        

    def add_edge(self, edge):
        

    def remove_edge(self, edge):
        

    def __get_node_index(self, node):
        """helper method to find node index"""
        
# This is the third class.
class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        

    def neighbors(self, node):
        

    def add_node(self, node):
        

    def remove_node(self, node):
        

    def add_edge(self, edge):
        

    def remove_edge(self, edge):
        

