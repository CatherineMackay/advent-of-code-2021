#### Advent of Code - Day 3 - Part 1 
# What is the power consumption of the submarine?

### import data from input.txt
from typing import List
import  statistics

with open('cat/day-03/input.txt', mode="r") as rawFile:
    ### put into a list of numbers 
    cleanList:List = []
    for line in rawFile.readlines():
        cleanList.append(line.strip())
    ### calc which number is most common in each collumn 
    # for each index in range 0 to 12 take each char of that row and calc mode 
    bitG = []
    bitE = []
    for index in range(len(cleanList[0])):
        bitList = []
        for row in cleanList:
            bitList.append(int(row[index]))
        if sum(bitList) >= len(cleanList)/2:
            bitG.append(1)
            bitE.append(0)
        else:
            bitG.append(0)
            bitE.append(1)
    ### represent the gamma rate and from this calc epsilon 
    bitGstring = ''.join(map(str,bitG))
    bitEstring = ''.join(map(str,bitE))
    ### translate rates from binary
    gamma = int(bitGstring,2)
    epsilon = int(bitEstring,2)
    ### multiply gamma rate and epsilon rate = power comsumption
    power = gamma * epsilon
    print(power)
    