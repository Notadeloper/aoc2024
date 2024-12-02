from collections import defaultdict

fp = "dataQ1.txt"

list1 = []
list2 = []

with open(fp, "r") as file:
    for line in file:
        col1, col2 = line.split()
        list1.append(int(col1))
        list2.append(int(col2))

# PART 1


def part1():
    list1.sort()
    list2.sort()

    res = 0

    for i in range(len(list1)):
        res += abs(list1[i] - list2[i])

    print(res)


def part2():
    list2Dict = defaultdict(int)
    for num in list2:
        list2Dict[num] += 1

    res = 0

    for num in list1:
        res += num * list2Dict[num]

    print(res)


part2()
