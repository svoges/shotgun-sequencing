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
    print code.read_file("Tests/basic_read1.txt")

if __name__ == "__main__":
    # test to see if importing reconstruct works
    print "----Test 1----"
    test1()

    # test to see if python reads the file correctly
    print "----Test 2----"
    test2()

    # test to see if nodes are being added to the graph correct1
    print "----Test 3----"
    test3()
