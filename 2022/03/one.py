import sys

def get_item_value(char):
    if(ord(char) > 64 and ord(char) < 91):
        return ord(char) - 38
    elif(ord(char) > 96 and ord(char) < 123):
        return ord(char) - 96

def find_first_match(line):
    if(type(line) == type(None) or line == ''):
        return 
    first_end = int(len(line)/2)
    compartment_1 = line[:first_end]
    compartment_2 = line[first_end:]
    for x in compartment_1:
        #print("Comp 1: %s" % x)
        for y in compartment_2:
            #print("Comp 1: %s, 2; %s" % (x, y))
            if(x == y):
                return x

def get_input():
    filename = "input.txt"
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
    lines = open(filename, 'r').readlines()

    sum_value = 0
    for l in lines:
        item = find_first_match(l)
        item_value = get_item_value(item)
        print("Match: %s; value: %d" % (item, item_value))
        sum_value += item_value

    print("Total value: %d" % sum_value)

    
def main():
    lines = get_input()
    matching = find_first_match(lines)
    print("Matching: %s" % matching)



main()
