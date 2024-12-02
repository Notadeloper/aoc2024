fp = "dataQ2.txt"

lines = []

with open(fp, "r") as file:
    for line in file:
        line = list(map(int, line.split()))
        lines.append(line)


def part1():
    res = 0

    for line in lines:
        if checkValidLine(line):
            res += 1

    print(res)


def part2():
    res = 0

    for line in lines:
        valid = False
        for i in range(len(line)):
            if checkValidLine(line[:i] + line[i + 1:]):
                valid = True
                break
        if valid:
            res += 1

    print(res)


def checkValidLine(line):
    if line[1] > line[0]:
        increasing = True
    elif line[1] < line[0]:
        increasing = False
    else:
        return False

    for i in range(1, len(line)):
        if not (1 <= abs(line[i] - line[i - 1]) <= 3):
            return False

        if increasing and not line[i] > line[i - 1] or not increasing and not line[i] < line[i - 1]:
            return False

    return True


part2()
