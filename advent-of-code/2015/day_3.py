# https://adventofcode.com/2015/day/3#part1
# https://adventofcode.com/2015/day/3#part2


def update_pos(x, y, move):
    if move == "<":
        x -= 1
    elif move == ">":
        x += 1
    elif move == "^":
        y += 1
    else:
        y -= 1
    return x, y


with(open("input/day-3.txt")) as file:
    moves = file.readline()
    start = (0, 0)
    visited = set()
    visited.add(start)
    x, y = start
    # only santa - part 1
    for move in moves:
        if move == "<":
            x -= 1
        elif move == ">":
            x += 1
        elif move == "^":
            y += 1
        else:
            y -= 1
        visited.add((x, y))
    print(len(visited))  # part 1

    # santa and robo-santa
    santa_visited = set()
    santa_visited.add(start)

    robo_santa_visited = set()
    robo_santa_visited.add(start)

    santa_x, santa_y = 0, 0
    robo_santa_x, robo_santa_y = 0, 0

    i = 0
    moves_cnt = len(moves)
    if len(moves) % 2 == 1:
        moves_cnt -= 1

    while i < moves_cnt:
        move = moves[i]
        santa_x, santa_y = update_pos(santa_x, santa_y, move)
        santa_visited.add((santa_x, santa_y))
        i += 1

        move = moves[i]
        robo_santa_x, robo_santa_y = update_pos(robo_santa_x, robo_santa_y, move)
        santa_visited.add((robo_santa_x, robo_santa_y))
        i += 1

    if i == len(moves) - 1:
        move = moves[i]
        santa_x, santa_y = update_pos(santa_x, santa_y, move)
        santa_visited.add((santa_x, santa_y))

    print(len(santa_visited) + len(robo_santa_visited) - 1)  # part 2
