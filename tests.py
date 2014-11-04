import reconstruct as code
import networkx as nx

def test1():
    if code.test() == "success":
        print "test 1 passes"
    else:
        print "test 1 fails"

def test2():
    test_array = code.read_file("Tests/basic_read1.txt")
    print test_array

def test3():
    print code.create_graph("Tests/basic_read2.txt")

def test4():
    code.read_file("Tests/empty_read.txt")

def test5():
    str1 = "book"
    str2 = "ook"
    if code.overlap(str1, str2) == True:
        print "Book and ook overlap!!"
    else:
        print "TEST DOES NOT PASS!!!!"

def test6():
    str1 = "hello"
    str2 = "lopez"
    distance = code.overlap_distance(str1, str2)
    print distance
    if distance == 2:
        print "overlap_distance passes"
    else:
        print "TEST DOES NOT PASS!!!!"

    str1 = "shrey"
    str2 = "shbb"
    distance = code.overlap_distance(str1, str2)
    print distance
    if distance == 0:
        print "overlap_distance passes"
    else:
        print "TEST DOES NOT PASS!!!!"

    str1 = "steffan"
    str2 = "teffan"
    distance = code.overlap_distance(str1, str2)
    print distance
    if distance == 6:
        print "overlap_distance passes"
    else:
        print "TEST DOES NOT PASS!!!!"

    str1 = "hello"
    str2 = "lopezzz"
    distance = code.overlap_distance(str1, str2)
    print distance
    if distance == 2:
        print "overlap_distance passes"
    else:
        print "TEST DOES NOT PASS!!!!"

    str1 = "ahhhello"
    str2 = "lopez"
    distance = code.overlap_distance(str1, str2)
    print distance
    if distance == 2:
        print "overlap_distance passes"
    else:
        print "TEST DOES NOT PASS!!!!"

def test7():
    graph = code.create_graph("Tests/test_graph.txt")
    assert graph.number_of_edges() == 6
    assert graph.number_of_nodes() == 4
    print graph.out_edges(data=True)

def test8():
    graph = code.create_graph("Tests/test_graph.txt")
    print code.sort_edges(graph)

def test9():
    graph = code.create_graph("Tests/greedy_test.txt")
    new_graph = code.assemble_greedy(graph)
    print new_graph.number_of_nodes()
    assert new_graph.number_of_nodes() == 3
    assert new_graph.number_of_edges() == 3

def test10():
    graph = code.create_graph("Tests/greedy_test.txt")
    new_graph = code.assemble_greedy(graph)


if __name__ == "__main__":
    # # test to see if importing reconstruct works
    # print "----Test 1----"
    # test1()
    #
    # # test to see if python reads the file correctly
    # print "----Test 2----"
    # test2()
    #
    # # test to see if nodes are being added to the graph correctly
    # print "----Test 3----"
    # test3()
    #
    # # Test error checking in read_file
    # print "---Test 4----"
    # print "Should print 'File was not able to be read'"
    # test4()
    #
    # # Test the overlap function in reconstruct
    # print "----Test 5----"
    # test5()
    #
    # # Test that the overlap_distance is correct
    # print "----Test 6----"
    # test6()
    #
    # # Test that the graph is correctly made
    # print "----Test 7----"
    # test7()
    #
    # Test the edge sorting method
    # test8()

    # Test the assemble_greedy method with 1 iteration
    # test9()

    # Test full method to see if we return the string made of substrings
