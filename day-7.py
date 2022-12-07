#!/usr/bin/python3

import re


def part1(dirs):
    total = 0
    for i, j in enumerate(dirs):
        if 'value' in dirs[j]:
            if dirs[j]['value'] <= 100000:
                total += dirs[j]['value']
    print(f"the total is {total}")


def part2(dirs):
    print(f"the root is {dirs['root']['value']}")
    avail = 70000000 - dirs['root']['value']
    req = 30000000 - avail
    print(f"the avail is {avail}")
    print(f"the req is {req}")

    remdirs = []
    for i, j in enumerate(dirs):
        if 'value' in dirs[j]:
            num = dirs[j]['value']
            if dirs[j]['value'] >= req:
                remdirs.append(num)
    remdirs.sort()
    # print(remdirs)
    print(f"the answer to part 2 is {remdirs[0]}")


def getInput():
    with open('day-7.input') as f:
        lines = f.readlines()
    input = tuple(line.replace('\n', ' ') for line in lines)
    return input


def main():
    dirs = {}
    input = getInput()
    path = []
    for li in input:
        if re.match('^\$ cd', li):
            x = li.split(' ')
            if x[2] == '..':
                if (len(path) > 1):
                    path.pop()
            elif x[2] == '/':
                path = ['root']
            else:
                path.append(x[2])

            # initialize the dictionary key to avoid issues later
            pathj = ''.join(path)
            if pathj in dirs:
                pass
            else:
                dirs[pathj] = {}

        elif re.match('^\d+', li):
            x = li.split(' ')

            # print(f"path - {path}")
            pathj = ''.join(path)
            temppath = path.copy()

            # really want a better way to do this
            # if 'value' in dirs[pathj]:
            #     dirs[pathj]['value'] += int(x[0])
            # else:
            #     dirs[pathj]['value'] = 0
            #     dirs[pathj]['value'] += int(x[0])

            # The better way
            dirs[pathj]['value'] = dirs[pathj].get('value', 0) + int(x[0])

            for a in range(len(temppath)-1):
                temppath.pop()
                tpj = ''.join(temppath)

                dirs[tpj]['value'] = dirs[tpj].get('value', 0) + int(x[0])

        elif re.match('^\$ ls', li):
            pass

        elif re.match('^dir', li):
            pass

    part1(dirs)

    part2(dirs)



main()
