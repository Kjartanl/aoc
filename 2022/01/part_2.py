import sys

# Default input file 
filename = "input.txt"
if(len(sys.argv) > 1):
    filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

currSum = 0
first = 0
second = 0
third = 0

for content in lines:
    val = content.strip()
    if(val != ''):
        currSum += int(val)
    else: 
        if(currSum > first):
            third = second
            second = first
            first = currSum
        elif(currSum > second):
            third = second
            second = currSum
        elif(currSum > third):
            third = currSum
        currSum = 0

print("Top three values: %d, %d, %d" % (first, second, third))
print("Sum: %d" % (first + second + third))
