# Graph Class

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
    # Add a node of Class Node
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            # insert node as key in the dictionary with empty values
            self.edges[node] = []
    # Add an edge of Class Edge with attribute source and destination
    # Taken from Node names
    # g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        # other wise use source name (equal Node Name) as key and append
        # Node name of destination
        self.edges[src].append(dest)
    # return list of destinations - values in the dictionary given the node key
    def childrenOf(self, node):
        return self.edges[node]
    # return True or False if node name is in the source edges
    def hasNode(self, node):
        return node in self.edges
    # get node by name
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    # print string with source and destination
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline

# Graph object inherits all attributes and function from Class Digraph
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        # plus it calculates its reverse
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

# buildCityGraph argument graphType: digraph or graph
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

# Build a Digraph
print(buildCityGraph(Digraph))
# Build a Graph
# any place I can get to I can go the other way
print(buildCityGraph(Graph))
