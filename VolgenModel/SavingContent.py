__author__ = 'nnyegaard'


def SaveToDiskFirstTime(data, name):
    """
    TODO: Write doc string
    """
    try:
        with open(name, "r") as file:
            pass
    except IOError as e:
        with open(name) as file:
            file.write(name+"txt", "w")





if __name__ == '__main__':
    print "Simple test:"
    SaveToDiskFirstTime("test123", "test")