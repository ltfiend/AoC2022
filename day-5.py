#!/usr/bin/python3
import re


def printTable2(data):
    for x in range(len(data)-1, -1, -1):
        print(x)
        print(data[x])


def doMovement(line, column):
    print(line)
    crane = []
    moveCommand = line.split(" ")
    amount = int(moveCommand[1])
    fromStack = int(moveCommand[3])-1
    toStack = int(moveCommand[5])-1

    for x in range(amount):
        crane.append(column[fromStack].pop())
    for x in range(amount):
        # crane.append(column[fromStack].pop())
        column[toStack].append(crane.pop())
        # column[toStack].append(column[fromStack].pop())

    return (column)


def main():
    row = [] * 200
    column = [[] for x in range(9)]

    with open('day-5.input') as f:
        lines = f.readlines()
    input = tuple(line.replace('\n', ' ') for line in lines)

    for li in input:
        # print(li)
        if re.match('move', li):   # Movement Lines
            data = doMovement(li, column)
            printTable2(data)
        elif re.match('^\s+1\s+', li):
            # At the end turn the columns into arrays
            for x in range(len(row)):
                for y in range(9):  # 9 columns static
                    # Doesn't add the blank spaces to the lists
                    if re.match('^\[', (row[x][y])):
                        column[y].append(row[x][y])
        elif re.match('^\[', li):
            row.insert(0, [li[i:i+4] for i in range(0, len(li), 4)])

    print("Answer:")
    for x in range(len(data)):
        print(f"{x} - {data[x][-1]}")


main()
