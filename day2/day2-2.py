def open_and_parse():
    file = open("input", "r")

    moves = []
    op_moves = []

    for line in file:
        moves.append(line[0])
        op_moves.append(line[2])

    file.close()

    return((op_moves, moves))

def compute_score(my, op):
    score = 0
    win = getWinning(op)
    loose = getLosing(op)
    match my:
        case 'X':
            score = score_moves(loose) + wins_score(loose, op)
        case 'Y':
            score = score_moves(op) + wins_score(op, op)
        case 'Z':
            score = score_moves(win) + wins_score(win, op)
    return score

def score_moves(move):
    if move == "A":
        return 1
    elif move == "B":
        return 2
    elif move == "C":
        return 3

def wins_score(my_2, op):
    if my_2 == op:
        return 3
    elif my_2 == "A" and op == "B":
        return 0
    elif my_2 == "A" and op == "C":
        return 6
    elif my_2 == "B" and op == "A":
        return 6
    elif my_2 == "B" and op == "C":
        return 0
    elif my_2 == "C" and op == "A":
        return 0
    elif my_2 == "C" and op == "B":
        return 6
    else:
        return 0

def getWinning(op_move):
    match op_move:
        case "A":
            print("OP : Rock, me : Paper -> Win")
            return "B"
        case "B":
            print("OP : Paper, me : Scissors -> Win")
            return "C"
        case "C":
            print("OP : Scissors, me : Rock -> Win")
            return "A"
        
def getLosing(op_move):
    match op_move:
        case "A":
            print("OP : Rock, me : Scissors -> loose")
            return "C"
        case "B":
            print("OP : Paper, me : Rock -> loose")
            return "A"
        case "C":
            print("OP : Scissors, me : Paper -> loose")
            return "B"


def main():
    (moves, op_moves) = open_and_parse()
    tmp = 0
    for i in range(len(moves)):
        tmp += compute_score(moves[i], op_moves[i])
    print(tmp)

if __name__ == "__main__":
    main()
