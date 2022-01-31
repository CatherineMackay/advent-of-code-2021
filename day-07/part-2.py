#### Advent of Code - Day 7 - Part 2
# The Treachery of Whales - how much fuel must they spend to align to that position?

### Quick func to find mean - I am trying to avoid using libraries
def get_mean(file: list[int]):
    l = len(file)
    mean = round(sum(file) / l)
    return mean


def get_addition(number: int):
    addition = 0
    for i in range(number):
        addition += i
    addition += number
    return addition


### import data
with open("cat/day-07/input.txt", "r") as rawFile:
    file = [int(i) for i in rawFile.readline().strip().split(",")]
    ### find horizontal number which produces the min total fuel = median
    ### First sort the numbers to order them so finding the median is accurate.
    file.sort()
    crabs = [{"position": int(i), "fuel": 0} for i in file]
    print(get_mean(file))
    mean = get_mean(file)
    ### Calc distance of each number from new mean position then factorial it  =fuel consumption
    for crab in crabs:
        crab["fuel"] = get_addition(abs(crab["position"] - (mean - 1)))
    ### sum all these fuels.
    totalFuel = sum(crab["fuel"] for crab in crabs)
    print(totalFuel)
