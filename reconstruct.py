import networkx as nx

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
def assemble_greedy(graph):
    test = 1
    # while G.number_of_nodes > 1:
    while test > 0:
        edge = sort_edges(graph)[0]
        print edge

        first_vertex = edge[0]
        second_vertex = edge[1]
        new_vertex = first_vertex[:edge[2]['weight']*-1] + second_vertex
        print new_vertex

        test -= 1

# Returns the edge with the greatest weight
def sort_edges(G):
    return sorted(G.out_edges(data=True), key=lambda edge: edge[2]['weight'], reverse=True)

def shortest_substring(x, y):
    return 'something'

def test():
    return "success"
