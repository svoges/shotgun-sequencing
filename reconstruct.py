import networkx as nx
import matplotlib.pyplot as plt

def create_graph(file):
    graph = nx.DiGraph()
    reads = read_file(file)
    # graph.add_nodes_from(reads)
    for read in reads:
        for node in reads:
            if read != node:
                x_index = max(0, len(read) - len(node))
                distance = overlap_distance(read[x_index:], node)
                if distance > 0:
                    # graph.add_edge(read, node, weight=distance)
                    graph.add_weighted_edges_from([(read, node, distance)])
    return graph

def draw_graph(graph):
    pos=nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    plt.show()


# Returns an array of each of the fragments
def read_file(file):
    contents = open(file, 'r')
    fragments = []
    for line in contents:
        line = line.strip('\n')
        fragments.append(line)
    if not fragments:
        print "File was not able to be read"
    return fragments

def overlap_distance(x, y):
    x_index = max(0, len(x) - len(y))
    x = x[x_index:]
    while x:
        if overlap(x, y):
            return len(x)
        else:
            x = x[1:]
            y = y[:-1]
    return 0


# Returns True if y is equal to the suffix of x
def overlap(x, y):
    x_index = max(0, len(x) - len(y))
    if len(x) >= len(y):
        if x[x_index:] == y:
            return True
        return False
    else:
        if x == y[:len(x)]:
            return True
        return False

# Given a graph with reads as nodes and edges weighted with the maximal overlap,
# returns the shortest common substring between all nodes
def assemble(graph):
    return "something"

def test():
    return "success"
