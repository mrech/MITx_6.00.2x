'''
Consider our representation of permutations of students in 
a line from Exercise 1. (The teacher only swaps the positions 
of two students that are next to each other in line.) Let's 
consider a line of three students, Alice, Bob, and Carol 
(denoted A, B, and C). Using the Graph class created in the 
lecture, we can create a graph with the design chosen in 
Exercise 1: vertices represent permutations of the students 
in line; edges connect two permutations if one can be made 
into the other by swapping two adjacent students.
'''

# Define Class Node (Vertices who represent premutations of students)


class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

# Define Class Edge connect two permutations if one can be made into other
# by swapping two adjacent students


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

# Define Diagraph with an adjacency list implementation.
# Associate with each node a list of destination nodes


class Digraph(object):
    """edges is a dict mapping each node to a list of
    its children"""

    def __init__(self):
        # Initialize edges as an empty dictionary
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            # insert node as key in the dictionary with empty values
            self.edges[node] = []
    # Add an edge of Class Edge with attribute source and destination
    # Taken from Node names
    # g.addEdge(Edge(g.getNode('ACB'), g.getNode('ABC')))

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        # other wise use source name (equal Node Name) as key and append
        # Node name of destination
        self.edges[src].append(dest)

    # return list of destinations - values in the dictionary given the node key
    # e.g. children of ACB is ABC
    def childrenOf(self, node):
        return self.edges[node]

    # return True or False if node name is in the source edges
    def hasNode(self, node):
        return node in self.edges

    # getNode return object of Class Node base on the Node attribute name
    def getNode(self, name):
        for n in self.edges:
            # if node name
            if n.getName() == name:
                return n
        raise NameError(name)

    # print string with source and destination
    def __str__(self):
        result = ''
        # src equal dictionary keys
        for src in self.edges:
            # dest equal dictionary values
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1]  # omit final newline

# Graph object inherits all attributes and function from Class Digraph


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        # plus it calculates its reverse
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
# buildPermutationGraph


def buildPermutationGraph(graphType):
    # Instantiate
    g = graphType()
    # add nodes
    nodes = []
    nodes.append(Node("ABC"))  # nodes[0]
    nodes.append(Node("ACB"))  # nodes[1]
    nodes.append(Node("BAC"))  # nodes[2]
    nodes.append(Node("BCA"))  # nodes[3]
    nodes.append(Node("CAB"))  # nodes[4]
    nodes.append(Node("CBA"))  # nodes[5]

    for n in nodes:
        g.addNode(n)

    # list all possible permutations (bidirectional edges)
    g.addEdge(Edge(g.getNode('ACB'), g.getNode('ABC')))
    g.addEdge(Edge(g.getNode('BAC'), g.getNode('ABC')))
    g.addEdge(Edge(g.getNode('BCA'), g.getNode('BAC')))
    g.addEdge(Edge(g.getNode('CAB'), g.getNode('ACB')))
    g.addEdge(Edge(g.getNode('CBA'), g.getNode('BCA')))
    g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))

    return g


# Build a Graph
print(buildPermutationGraph(Graph))


g = buildPermutationGraph(Graph)

# Instantiate
g = Graph()
# add nodes
nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

for n in nodes:
    g.addNode(n)

# CODE FOR SUBMITION
# list all possible permutations (bidirectional edges)
g.addEdge(Edge(g.getNode('ACB'), g.getNode('ABC')))
g.addEdge(Edge(g.getNode('BAC'), g.getNode('ABC')))
g.addEdge(Edge(g.getNode('BCA'), g.getNode('BAC')))
g.addEdge(Edge(g.getNode('CAB'), g.getNode('ACB')))
g.addEdge(Edge(g.getNode('CBA'), g.getNode('BCA')))
g.addEdge(Edge(g.getNode('CAB'), g.getNode('CBA')))


# Check answers
edges = g.childrenOf(nodes[0])
for n in edges:
    n.getName()

# AUTOMATION
for i in range(len(nodes)):
    n = nodes[i].getName()
    for j in range(i+1, len(nodes)):
        # if following node names are equal to one of its children
        if nodes[j].getName() == n[1]+n[0]+n[2] or \
                nodes[j].getName() == n[0]+n[2]+n[1]:
            # addEdge
            g.addEdge(Edge(nodes[i], nodes[j]))

# Check answers
for z in range(len(nodes)):
    edges = g.childrenOf(nodes[z])
    for n in edges:
        'node[' + str(z) + ']: ' + n.getName()
