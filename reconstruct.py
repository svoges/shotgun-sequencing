import networkx as nx
from time import sleep

def create_graph(file):
    graph = nx.DiGraph()
    reads = read_file(file)
    # graph.add_nodes_from(reads)
    for read in reads:
        for node in reads:
            if read != node:
                x_index = max(0, len(read) - len(node))
                distance = overlap_distance(read[x_index:], node)
                if distance >= 0:
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
def assemble_greedy(graph, printing=False):
    while graph.number_of_nodes() > 1:
        edge = sort_edges(graph)
        if not edge:
            print "ATTENTION: THIS SHOULD NOT HAPPEN"
        else:
            edge = edge[0]
            if printing:
                print "edge: " + str(edge) + "\n"

            first_vertex = edge[0]
            second_vertex = edge[1]
            if printing:
                print "first vertex: " + first_vertex
                print "second vertex: " + second_vertex

            if edge[2]["weight"] == 0:
                new_vertex = first_vertex + second_vertex
            else:
                new_vertex = first_vertex[:edge[2]['weight']*-1] + second_vertex
            if printing:
                print "new_vertex: " +  new_vertex + "\n"

                print "====Edges before===="
                print graph.out_edges(data=True)
                print "====Edges before====" + "\n"

                print "====Nodes before===="
                print graph.nodes()
                print "====Nodes before====" + "\n"

            edges_into_first = graph.in_edges(nbunch=first_vertex, data=True)
            edges_outof_first = graph.out_edges(nbunch=first_vertex, data=True)

            edges_into_second = graph.in_edges(nbunch=second_vertex, data=True)
            edges_outof_second = graph.out_edges(nbunch=second_vertex, data=True)

            # edges into first remain the same
            for edge in edges_into_first:
                graph.add_weighted_edges_from([(edge[0], new_vertex, edge[2]['weight'])])

            for edge in edges_outof_first:
                if edge[1] in new_vertex:
                    graph.remove_node(edge[1])
                else:
                    new_distance = overlap_distance(new_vertex, edge[1])
                    if new_distance >= 0:
                        graph.add_weighted_edges_from([(new_vertex, edge[1], new_distance)])

            # edges out of second remain the same
            for edge in edges_outof_second:
                graph.add_weighted_edges_from([(new_vertex, edge[1], edge[2]['weight'])])

            for edge in edges_into_second:
                if edge[0] in new_vertex:
                    if edge[0] in graph.nodes():
                        graph.remove_node(edge[0])
                else:
                    new_distance = overlap_distance(edge[0], new_vertex)
                    if new_distance >= 0:
                        graph.add_weighted_edges_from([(edge[0], new_vertex, new_distance)])

            if printing:
                print "====Edges after===="
                print graph.out_edges(data=True)
                print "====Edges after====" + "\n"

                print "====Nodes after===="
                print graph.nodes()
                print "====Nodes after====" + "\n"

    return graph.nodes()[0]

# Returns the edge with the greatest weight
def sort_edges(G):
    edges = G.out_edges(data=True)
    if edges:
        return sorted(edges, key=lambda edge: edge[2]['weight'], reverse=True)
    else:
        return False

def test():
    return "success"
