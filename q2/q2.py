fp = "dataQ2.txt"

lines = []

with open(fp, "r") as file:
    for line in file:
        line = line.split()
        lines.append(line)


def part1():
    res = 0

    for line in lines:
        success = True
        if line[1] > line[0]:
            increasing = True
        elif line[1] < line[0]:
            increasing = False
        else:
            # neither increasing or decreasing
            continue

        for i in range(1, len(line)):
            if not (1 <= abs(int(line[i]) - int(line[i - 1])) <= 3):
                success = False
                break

            if increasing and not line[i] > line[i - 1] or not increasing and not line[i] < line[i - 1]:
                success = False
                break

        if success:
            res += 1

    print(res)


part1()
