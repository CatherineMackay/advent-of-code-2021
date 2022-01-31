#### Advent of Code - Day 7 - Part 1
# The Treachery of Whales - how much fuel must they spend to align to that position?

### Quick func to find median - I am trying to avoid using libraries
def get_median(file: list[int]):
    l = len(file)
    # to find odd/even do n % 2 which gives the remainder after division, so if =0 it is even
    if (l % 2) == 0:
        median = file[int((l / 2))]
    else:
        median = (
            file[((l + 1) // 2)] - (file[((l + 1) // 2)] - file[((l - 1) // 2)]) // 2
        )
    return median


### import data
with open("cat/day-07/input.txt", "r") as rawFile:
    file = [int(i) for i in rawFile.readline().strip().split(",")]
    ### find horizontal number which produces the min total fuel = median
    ### First sort the numbers to order them so finding the median is accurate.
    file.sort()
    crabs = [{"position": int(i), "fuel": 0} for i in file]
    med = get_median(file)
    ### Calc distance of each number from median =fuel consumption
    for crab in crabs:
        crab["fuel"] = abs(crab["position"] - med)
    ### sum all these fuels.
    totalFuel = sum(crab["fuel"] for crab in crabs)
    print(totalFuel)
