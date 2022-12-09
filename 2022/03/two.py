import sys

def get_item_value(char):
    if(ord(char) > 64 and ord(char) < 91):
        return ord(char) - 38
    elif(ord(char) > 96 and ord(char) < 123):
        return ord(char) - 96

def find_common(first, second, third):
    for item in first:
        if(second.find(item) > -1 and third.find(item) > -1):
            return item

def main():
    filename = "input.txt"
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
    lines = open(filename, 'r').readlines()

    group_numbers = range(int(len(lines) / 3))
    sum_value = 0
    for group in group_numbers:
        line_nr = group*3
        first = lines[line_nr]
        second = lines[line_nr + 1]
        third = lines[line_nr + 2]
        common_badge = find_common(first, second, third)
        value = get_item_value(common_badge)
        print("Group: %d; Common badge: %s; value: %d" % (line_nr, common_badge, value))
        sum_value += value
    print("Total value: %d" % sum_value)
    
main()
