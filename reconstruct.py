import networkx as nx
import time
import Queue

def create_graph(file):
    graph = nx.DiGraph()
    reads = read_file(file)
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
    # print "k: " + str(len(fragments))
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
def assemble_greedy(graph, output, printing=False):
    q = Queue.PriorityQueue()
    removed = []
    all_edges = graph.out_edges(data=True)
    # turn each edge into a Edge class and put it into the priority queue
    for edge in all_edges:
        q.put(Edge(edge[2]['weight'], edge[0], edge[1]))

    while graph.number_of_nodes() > 1:
        # while not q.empty():
        #     next_v = q.get()
        #     print str(str(next_v.weight) + ", " + next_v.first_vertex + ", " + next_v.second_vertex)
        # print "\n"

        # start_sort = time.time()
        # edge = sort_edges(graph)
        # end_sort = time.time()
        # print str(end_sort - start_sort)
        edge = q.get()
        first_vertex = edge.first_vertex
        second_vertex = edge.second_vertex
        weight = edge.weight
        if printing:
            print "=========="
            print "first vertex: " + first_vertex
            print "second vertex: " + second_vertex
            print "weight: " + str(weight)

        if weight == 0:
            print "WEIGHT IS ZERO"
            new_vertex = first_vertex + second_vertex
        else:
            new_vertex = first_vertex[:weight*-1] + second_vertex
        if printing:
            print "new_vertex: " +  new_vertex + "\n"

            print "Edges before"
            print graph.out_edges(data=True)
            print "\n"

            print "Nodes before"
            print graph.nodes()
            print "==========\n\n"
        if new_vertex not in removed:
            edges_into_first = graph.in_edges(nbunch=first_vertex, data=True)
            edges_outof_first = graph.out_edges(nbunch=first_vertex, data=True)

            edges_into_second = graph.in_edges(nbunch=second_vertex, data=True)
            edges_outof_second = graph.out_edges(nbunch=second_vertex, data=True)

            # edges into first remain the same
            for in_edge in edges_into_first:
                graph.add_weighted_edges_from([(in_edge[0], new_vertex, in_edge[2]['weight'])])
                q.put(Edge(in_edge[2]['weight'], in_edge[0], new_vertex))


            for out_edge in edges_outof_first:
                if out_edge[1] in new_vertex:
                    graph.remove_node(out_edge[1])
                    removed.append(out_edge[1] + new_vertex)
                else:
                    new_distance = overlap_distance(new_vertex, out_edge[1])
                    if new_distance >= 0:
                        graph.add_weighted_edges_from([(new_vertex, out_edge[1], new_distance)])
                        q.put(Edge(new_distance, new_vertex, out_edge[1]))

            # edges out of second remain the same
            for out_edge in edges_outof_second:
                graph.add_weighted_edges_from([(new_vertex, out_edge[1], out_edge[2]['weight'])])
                q.put(Edge(out_edge[2]['weight'], new_vertex, out_edge[1]))

            for in_edge in edges_into_second:
                if in_edge[0] in new_vertex:
                    if in_edge[0] in graph.nodes():
                        graph.remove_node(in_edge[0])
                        removed.append(out_edge[0] + new_vertex)
                else:
                    new_distance = overlap_distance(in_edge[0], new_vertex)
                    if new_distance >= 0:
                        graph.add_weighted_edges_from([(in_edge[0], new_vertex, new_distance)])
                        q.put(Edge(new_distance, in_edge[0], new_vertex))

            # if printing:
            #     print "====Edges after===="
            #     print graph.out_edges(data=True)
            #     print "====Edges after====" + "\n"
            #
            #     print "====Nodes after===="
            #     print graph.nodes()
            #     print "====Nodes after====" + "\n"
    f = open(output, 'w')
    f.write(graph.nodes()[0] + '\n')
    f.close()
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

class Edge(object):
    def __init__(self, weight, first_vertex, second_vertex):
        self.weight = weight
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        return

    def __cmp__(self, other):
        return cmp(other.weight, self.weight)
