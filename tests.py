import reconstruct as code

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

if __name__ == "__main__":
    # test to see if importing reconstruct works
    print "----Test 1----"
    test1()

    # test to see if python reads the file correctly
    print "----Test 2----"
    test2()

    # test to see if nodes are being added to the graph correctly
    print "----Test 3----"
    test3()

    # Test error checking in read_file
    print "---Test 4----"
    print "Should print 'File was not able to be read'"
    test4()
