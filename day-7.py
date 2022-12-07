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
            # print(f'0 - {x[0]} - 1 {x[1]} - 2 {x[2]}')
            if x[2] == '..':
                # if re.match('\.\.', x[2]):
                if (len(path) > 1):
                    print("pop")
                    path.pop()
            elif x[2] == '/':
                print('root', x[2])
                path = ['root']
                pathj = ''.join(path)
                if pathj in dirs:
                    pass
                else:
                    dirs[pathj] = {}
            else:
                path.append(x[2])
                print(f"path - {path}")
                pathj = ''.join(path)
                if pathj in dirs:
                    pass
                else:
                    dirs[pathj] = {}

            # dirs[pathj] = {}

                # print(path)
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
    print(f"the total is {total}")


main()
