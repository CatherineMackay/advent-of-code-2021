#### Advent of Code - Day 3 - Part 2
# What is the life support rating of the submarine?

### import data from input.txt
import statistics

with open("cat/day-03/input.txt", mode="r") as rawFile:
    ### put into a list of numbers
    cleanList: list = []
    oxyList: list = []
    cotwoList: list = []
    for line in rawFile.readlines():
        cleanList.append(line.strip())
        oxyList.append(line.strip())
        cotwoList.append(line.strip())
    ### calc which number is most common in each collumn
    ### save all of the rows with that number in that position
    for index in range(len(cleanList[0])):
        if len(oxyList) != 1:
            ### Create empty list to calc most common in
            bitList = []
            mostCommonO = ""
            for row in list(oxyList):
                bitList.append(int(row[index]))
            if sum(bitList) >= len(oxyList) / 2:
                mostCommonO = 1
            else:
                mostCommonO = 0
            ### remove all rows for this index that aren't the most common
            for row in list(oxyList):
                if int(row[index]) != mostCommonO:
                    oxyList.remove(row)
        if len(cotwoList) != 1:
            bitList = []
            mostCommonCo = ""
            for row in list(cotwoList):
                bitList.append(int(row[index]))
            if sum(bitList) >= len(cotwoList) / 2:
                mostCommonCo = 1
            else:
                mostCommonCo = 0
            for row in list(cotwoList):
                if int(row[index]) == mostCommonCo:
                    cotwoList.remove(row)
    ### calc the oxygen and CO2
    ### translate rates from binary
    oxygen = int(oxyList[0], 2)
    cotwo = int(cotwoList[0], 2)
    ### multiply oxygen and CO2 = life support rating
    life = oxygen * cotwo
    print(life)
