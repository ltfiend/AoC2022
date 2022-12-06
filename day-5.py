#!/usr/bin/python3
import re
import numpy as np


def printTable3(data):
    for d in data:
        print(d)
    
    test = np.array(data)
    print(np.shape(test))

    for num in test:
        print(num)
    # print(f"test {test[0]}")
    print(test[0, 0])


def printTable2(data):
    for x in range(len(data)-1, -1, -1):
        print(x)
        print(data[x])

def doMovement(line, column):
    # print(column)
    moveCommand = line.split(" ")
    amount = int(moveCommand[1])
    fromStack = int(moveCommand[3])-1
    toStack = int(moveCommand[5])-1

    for x in range(amount):
        crane = column[fromStack].pop()
        column[toStack].append(crane)
    return (column)


def main():
    row = [] * 200
    column = [[] for x in range(9)]

    rownum = 0

    with open('day-5.input') as f:
        lines = f.readlines()
    input = tuple(line.replace('\n', ' ') for line in lines)

    for li in input:
        # print(li)
        if re.match('move', li):
            data = doMovement(li, column)
            printTable2(data)
        else:
            if re.match('^\s+1\s+', li):
                for x in range(len(row)):
                    #print(row[x])
                    for y in range(9):
                        #jprint(row[x][y])
                        if re.match('^\[', (row[x][y])):
                            column[y].append(row[x][y])
                                    #print('asdfqasdfasdf', column[8])
            elif re.match('^\[', li):
                row.insert(0, [li[i:i+4] for i in range(0, len(li), 4)])
                rownum += 1

    for x in range(len(data)):
        print(data[x][-1])

main()
