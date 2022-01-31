#### Advent of Code - Day 2 - Part 2 
# pilot the submarine - What do you get if you multiply your final horizontal position by your final depth?

### import data from input.txt
from io import TextIOWrapper
from typing import List

with open('cat/day-02/input.txt', mode="r") as rawFile:
    file:TextIOWrapper = rawFile
### put into a list of string 
    lines:List = file.readlines()
    cleanList:List = []
    x = 0
    y = 0
    aim = 0
    for line in lines:
        cleanLine = line.strip()
        cleanList.append(cleanLine)
### split into horizontal position and depth 
# if the word starts with f (forward) then add the number to the array of horizontal movements
        if line[0] == "f":
            x+= int(line[8])
            y+= aim * int(line[8])
        if line[0] == "d":
            aim+= int(line[5])
        if line[0] == "u":
            aim-= int(line[3])
### multiply together 
    mutiply = x * y 
    print(mutiply)