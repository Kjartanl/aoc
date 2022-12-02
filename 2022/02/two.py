import sys

rock = 'A'
paper = 'B'
scissors = 'C'

loose = 'X'
draw = 'Y'
win = 'Z'

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
    required_result = line[2]
    required_move = get_required_move(opponents_move, required_result)
    score = get_game_result_Value(required_move, opponents_move) + get_move_value(required_move)
    return score

def get_required_move(opp_move, result):
    if (result == win):
        print("Win required!")
        return rock if opp_move == scissors else scissors if opp_move == paper else paper
    elif(result == loose):
        print("Loss required!")
        return rock if opp_move == paper else scissors if opp_move == rock else paper
    else: # result should be a draw:
        print("Draw required!")
        return opp_move
        
def get_move_value(move):
    move_points = 1 if move == rock else 2 if move == paper else 3
    print("Move points: %d" % move_points)
    return move_points

def get_game_result_Value(your_move, opp_move):
    if(opp_move == rock):
        print("Opponent played Rock")
        return calc(your_move, scissors, rock)
    elif(opp_move == paper):
        print("Opponent played Paper")
        return calc(your_move, rock, paper)
    else:
        print("Opponent played Scisors")
        return calc(your_move, paper, scissors)

def calc(your_move, loose, draw):
    points = 0 if your_move == loose else 3 if your_move == draw else 6 
    print("You played %s for %s points." % (get_move_name(your_move), points))
    return points

def get_move_name(move):
    return "Rock" if move == rock else "Paper" if move == paper else "Scissors"

run()
