# https://adventofcode.com/2015/day/1#part1
# https://adventofcode.com/2015/day/1#part2

with(open("input/day-1.txt")) as file:
    data = list(file.readlines()[0])
    print(data.count("(") - data.count(")"))  # for part 1

    # find the position where -1 is reached
    level = 0
    basement_found = False
    for i in range(len(data)):
        level = level + (1 if data[i] == "(" else -1)
        if level == -1:
            print(i + 1)
            basement_found = True
            break
    if not basement_found:
        print(i + 1)
