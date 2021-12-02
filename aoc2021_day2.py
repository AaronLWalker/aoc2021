#question 1
f = open("day2.txt", "r").readlines()
f = [i.strip('\n').split(' ') for i in f]
depth, horizontal = 0, 0
for i in f:
    depth += int(i[1]) if i[0] == 'down' else False
    depth -= int(i[1]) if i[0] == 'up' else False
    horizontal += int(i[1]) if i[0] == 'forward' else False
depth * horizontal

#question 2
f = open("day2.txt", "r").readlines()
f = [i.strip('\n').split(' ') for i in f]
depth, horizontal, aim = 0, 0, 0
for i in f:
    aim   += int(i[1]) if i[0] == 'down' else False
    aim   -= int(i[1]) if i[0] == 'up' else False
    horizontal += int(i[1]) if i[0] == 'forward' else False
    depth += aim*int(i[1]) if i[0] == 'forward' else False
depth * horizontal
