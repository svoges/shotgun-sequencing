import networkx as nx

def create_graph(file):
    graph = nx.Graph()
    reads = []
    reads_file = read_file(file)
    graph.add_nodes_from(reads_file)
    print_nodes(graph)
    return graph


def read_file(file):
    contents = open(file, 'r')
    fragments = []
    for line in contents:
        line = line.strip('\n')
        fragments.append(line)
    return fragments

def print_nodes(graph):
    print graph.nodes()


def assemble(graph):
    return "something"

def test():
    return "success"
