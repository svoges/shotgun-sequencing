import networkx as nx

def create_graph(file):
    graph = nx.DiGraph()
    reads = read_file(file)
    # graph.add_nodes_from(reads)
    for read in reads:
        for node in reads:
            if read != node:
                distance = overlap_distance(read, node)
                graph.add_edge(read, node, weight=distance)
    return graph


# Returns an array of each of the fragments
def read_file(file):
    contents = open(file, 'r')
    fragments = []
    for line in contents:
        line = line.strip('\n')
        fragments.append(line)
    print fragments
    if not fragments:
        print "File was not able to be read"
    return fragments

def overlap_distance(x, y):
    return distance

def print_nodes(graph):
    print graph.nodes()


def assemble(graph):
    return "something"

def test():
    return "success"
