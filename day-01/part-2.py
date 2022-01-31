#### Advent of Code - Day 1 - Part 2 
# count the number of times the sum of measurements in this sliding window increases

### import data from input.txt
from io import TextIOWrapper
from typing import List

with open('./day-1/input.txt', mode="r") as rawFile:
    file:TextIOWrapper = rawFile
    ### put into a list of numbers 
    lines:List = file.readlines()
    cleanList:List = []
    for line in lines:
        cleanLine = line.strip()
        cleanLineInt = int(cleanLine)
        cleanList.append(cleanLineInt)
    ### iterate through list applying logic 
    counter = 0 
    previousSlidingWindow = sum(cleanList[0:3])
    # find the length of numbers when creating sliding windows (aka there are less than 3 numbers left including itself)
    stop = len(cleanList) - 1
    for index in range(0, stop, 1):
        slidingWindow = sum(cleanList[index: index + 3])
        if slidingWindow > previousSlidingWindow:
            counter+=1
        previousSlidingWindow = sum(cleanList[index: index + 3])
     
    print(counter)
