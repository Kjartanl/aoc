import sys

def move_last_to_42(l):
    start = l[0:41]
    mid = l[-1]
    print(mid)
    end = l[41:-1]
    return start + mid + end

def move_first_to_42(l):
    start = l[1:42]
    mid = l[0:1]
    print(mid)
    end = l[42:]
    return start + mid + end

def move_from_end(l, x):
    start = l[-x:]
    end = l[0:-x]
    return start + end

def move_from_back_to_front(two):
    three = two
    for x in range(9, 1, -1):
        three = move_from_end(three, x)
        print("-- 3. (move " + str(x) + "):" + three)
    return three

def shift_consonants_right(three):
    vowels = ('a', 'e', 'i','o','y','æ','ø','å', 'A', 'E', 'I','O','Y','Æ','Ø','Å')
    string_pos_backwards = range(len(three) - 1, 0, -1) 

    for pos in string_pos_backwards:
        character = three[pos]
        if(character in vowels):
            continue
        sec_a = three[0:pos]
        sec_c = three[pos:pos+1]
        sec_b = three[pos+1:pos+2]
        sec_d = three[pos+2:]
        three = sec_a + sec_b + sec_c + sec_d
        print("--4. " + three)
    return three
        
def main():
    line = open('original.txt', 'r').readline().strip()
    print("0: " + line)

    one = move_last_to_42(line)
    print("1: " + one)

    two = move_first_to_42(one)
    print("2: " + two)

    three = move_from_back_to_front(two)
    print("3: " + three)

    done = shift_consonants_right(three)
    print("#############")
    print("Done!: " + done)

main()

