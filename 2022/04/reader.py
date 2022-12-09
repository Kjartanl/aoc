import sys

def get_input(filename):
    filename = "input.txt"
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
    lines = open(filename, 'r').readlines()
    return lines


