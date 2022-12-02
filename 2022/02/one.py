import sys

rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']

def run():
    lines = get_input()
    sum = 0
    round = 0
    for line in lines:
        line = line.strip()
        round += 1
        print("---- Round %d ----" % round)
        value = calc_value(line)
        sum += value
        print("Sum so far: %d" % sum)

    print("------")
    print("FINAL SCORE: %d" % sum)

def get_input():
    filename = "input.txt"
    if(len(sys.argv) > 1):
        filename = sys.argv[1]
    lines = open(filename, 'r').readlines()
    return lines

def calc_value(line):
    opponents_move = line[0]
    your_move = line[2]
    score = get_game_result_Value(your_move, opponents_move) + get_move_value(your_move)
    return score

def get_move_value(move):
    move_points = 1 if move in rock else 2 if move in paper else 3
    print("Move points: %d" % move_points)
    return move_points

def get_game_result_Value(your_move, opp_move):
    if(opp_move in rock):
        print("Opponent played Rock")
        return calc(your_move, scissors, rock)
    elif(opp_move in paper):
        print("Opponent played Paper")
        return calc(your_move, rock, paper)
    else:
        print("Opponent played Scisors")
        return calc(your_move, paper, scissors)

def calc(your_move, loose, draw):
    points = 0 if your_move in loose else 3 if your_move in draw else 6 
    print("You played %s for %s points." % (get_move_name(your_move), points))
    return points

def get_move_name(move):
    return "Rock" if move in rock else "Paper" if move in paper else "scissors"

run()
