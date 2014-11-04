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
    superstring = code.assemble_greedy(graph)
    assert superstring == "GCATCAGTG"
    print "test 10 passes"

def test11():
    graph = code.create_graph("Tests/greedy_test2.txt")
    superstring = code.assemble_greedy(graph)
    assert superstring == "ATGCATGCC" or superstring == "GCCATGCAT"
    print "test 11 passes"

# The code seems to be breaking when a read is the substring of another read. Let's test this out!
def test12():
    graph = code.create_graph("Tests/substring.txt")
    superstring = code.assemble_greedy(graph, printing=True)
    assert superstring == "ACCGGTTA"
    print "test 12 passes"


def reads_tester(read_file, answer_file, output_file):
    graph = code.create_graph(read_file)
    superstring = code.assemble_greedy(graph, output_file)
    if answer_file:
        answer = open(answer_file).read()
        output = open(output_file).read()
        assert answer == output
        # answer = open(answer_file, 'r').read().strip("\n")
        # assert len(answer) == len(superstring)
        # assert answer == superstring


def test_reads1():
    print "Test 1"
    reads_tester("Dataset/reads1.txt", "Dataset/answer1.txt", "Output/output1.txt")

def test_reads2():
    print "Test 2"
    reads_tester("Dataset/reads2.txt", "Dataset/answer2.txt", "Output/output2.txt")

def test_reads3():
    print "Test 3"
    reads_tester("Dataset/reads3.txt", "Dataset/answer3.txt", "Output/output3.txt")

def test_reads4():
    print "Test 4"
    reads_tester("Dataset/reads4.txt", "Dataset/answer4.txt", "Output/output4.txt")

def test_reads5():
    print "Test 5"
    reads_tester("Dataset/reads5.txt", "Dataset/answer5.txt", "Output/output5.txt")

def test_reads6():
    print "Test 6"
    reads_tester("Dataset/reads6.txt", "", "Output/output6.txt")

def test_reads7():
    print "Test 7"
    reads_tester("Dataset/reads7.txt", "", "Output/output7.txt")

def test_reads8():
    print "Test 8"
    reads_tester("Dataset/reads8.txt", "", "Output/output8.txt")

def test_reads9():
    print "Test 9"
    reads_tester("Dataset/reads9.txt", "", "Output/output9.txt")

def test_reads10():
    print "Test 10"
    reads_tester("Dataset/reads10.txt", "", "Output/output10.txt")



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
    # test10()
    # test11()

    # Test to see if a read that is a substring of another read works
    # test12()

    # Test reads from Dataset with answers
    test_reads1()
    test_reads2()
    test_reads3()
    test_reads4()
    test_reads5()

    # Test reads from Dataset without answers
    test_reads6()
    test_reads7()
    test_reads8()
    test_reads9()
    test_reads10()
    print "All tests pass"
