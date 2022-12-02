file = open('input.txt', 'r')
lines = file.readlines()

max_nr = 0
curr = 0
for l in lines:
    ln = l.strip()
    if(ln == ''):
        if(curr > max_nr):
            max_nr = curr
        curr = 0
    else:
        curr += int(ln)
print('Max: ' + str(max_nr))
