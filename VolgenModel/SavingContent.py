__author__ = 'nnyegaard'


def SaveToDisk(data, name):
    """
    TODO: Write doc string
    """

    try:
        with open(name, "r") as file:
            pass
    except IOError as e:
        print "Damn!"
        with open(name, "w") as file:
            file.write("test123")
#    with open(name, "w+") as file:
#        if file.read() != "":
            # Read our data and do something
#            print
#        else:
            # Write our data
#            file.write("testtest")





if __name__ == '__main__':
    print "Simple test:"
    SaveToDisk("test123", "test")