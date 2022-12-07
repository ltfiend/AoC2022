#!/usr/bin/python3

import re


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
        # print(li)
        if re.match('^\$ cd', li):
            x = li.split(' ')
            print(f"x2 - {x[2]}")
            if x[2] == '..':
                if (len(path) > 1):
                    print("pop")
                    path.pop()
            elif x[2] == '/':
                # print('root', x[2])
                path = ['root']
            else:
                # print(f"path - {path}")
                path.append(x[2])

            pathj = ''.join(path)
            if pathj in dirs:
                pass
            else:
                dirs[pathj] = {}

        elif re.match('^\$ ls', li):
            pass

        elif re.match('^\d+', li):
            x = li.split(' ')

            # print(f"path - {path}")
            pathj = ''.join(path)
            temppath = path.copy()

            if 'value' in dirs[pathj]:
                dirs[pathj]['value'] += int(x[0])
            else:
                dirs[pathj]['value'] = 0
                dirs[pathj]['value'] += int(x[0])

            for a in range(len(temppath)-1):
                # print(temppath)
                temppath.pop()
                # print(temppath)
                # print(f"temppath - {temppath}")
                temppathj = ''.join(temppath)
                if 'value' in dirs[temppathj]:
                    dirs[temppathj]['value'] += int(x[0])
                else:
                    dirs[temppathj]['value'] = 0
                    dirs[temppathj]['value'] += int(x[0])


        elif re.match('^dir', li):
            x = li.split(' ')
            # dirs[path][x[1]]['value'] = 0
    total = 0

    for i, j in enumerate(dirs):
        if 'value' in dirs[j]:
            if dirs[j]['value'] <= 100000:
                total += dirs[j]['value']

    print(f"the root is {dirs['root']['value']}")
    avail = 70000000 - dirs['root']['value']
    req = 30000000 - avail
    print(f"the avail is {avail}")
    print(f"the total is {total}")
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


main()
