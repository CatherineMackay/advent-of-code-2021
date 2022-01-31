#### Advent of Code - Day 5 - Part 1
# Hydrothermal Venture. At how many points do at least two lines overlap?

### to capture the decreasing values in range func eg x1=8 and x2=3
def decreasing(i, j):
    if i > j:
        step = -1
    else:
        step = 1
    return step


### make a function that stores every position inbetween two locations making sure either x1 = x2 or y1 = y2 to proceed
def check_line(position: list[int]):
    x1 = int(position[0])
    x2 = int(position[2])
    y1 = int(position[1])
    y2 = int(position[3])
    line = []
    if y1 == y2:
        for i in range(x1, x2, decreasing(x1, x2)):
            line.append([i, y1])
        line.append([x2, y2])
    elif x1 == x2:
        for j in range(y1, y2, decreasing(y1, y2)):
            line.append([x1, j])
        line.append([x2, y2])
    return line


with open("cat/day-05/input.txt", "r") as rawFile:
    ### clean data by stripping out "->" and replacing with comma seperation
    points = []
    ### find all the points where there is a vent in a huge list
    line = rawFile.readline()
    while line:
        line = line.strip().replace(" -> ", ",").split(",")
        points.extend(check_line(line))
        line = rawFile.readline()

    ### cycle through each position and only keep if there is more than two of them
    ### create dictionary adding the point as the key and increment value if found multiple times
    dangerPositions = {}
    for point in points:
        if str(point) in dangerPositions:
            dangerPositions[str(point)] += 1
        else:
            dangerPositions[str(point)] = 1

    ### find how many times there is a position with more than two vents
    print(len([x for x in dangerPositions.values() if x > 1]))
