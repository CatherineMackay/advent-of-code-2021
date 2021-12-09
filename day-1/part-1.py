#### Advent of Code - Day 1 - Part 1 
# count the number of times a depth measurement increases

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
    previousNumber = cleanList[0]

    for number in cleanList:
        if number > previousNumber:
            counter+=1
        previousNumber = number 
        
    print(counter)
