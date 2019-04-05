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

# Weighted graph
# weighting edges higher for moves that are harder to make.
# EG in the student permutations:
# 1. A large student who is difficult to move around in line
# 1. weight heavily all edges that involve moving that student (valid for both directions)
# 2. A sticky spot on the floor which is difficult to move onto and off of
# 2. weight heavily all edges that involve moving thorugh that point (valid for both directions)


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.weight = weight
        # invoking the __init__ of the parent class
        Edge.__init__(self, src, dest)

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() +\
            ' (' + str(self.getWeight()) + ')'

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


# Instantiate
g = Digraph()
# add nodes
nodes = []
nodes.append(Node("A"))  # nodes[0]
nodes.append(Node("B"))  # nodes[1]

for n in nodes:
    g.addNode(n)

# list all possible permutations (unidirectional edges and its weights)
e = WeightedEdge(g.getNode('A'), g.getNode('B'), 3)
print(e)
