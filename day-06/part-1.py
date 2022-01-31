#### Advent of Code - Day 6 - Part 1
# Count those Lantern fish like your life depends on it.

### for each value if 0 change to 6 and append an 8 on the end
### if not 0 count down by 1
def each_day(today):
    tomorrow = []
    count = 0
    for age in today:
        if age != 0:
            newAge = age - 1
            tomorrow.append(newAge)
        else:
            tomorrow.append(6)
            count += 1
    babies = [8] * count
    tomorrow.extend(babies)
    return tomorrow


### import data and start the clock
days = 80
rawFile = open("cat/day-06/input.txt", "r")
data = [int(line) for line in rawFile.readline().split(",")]
for n in range(days):
    data = each_day(data)
### print length of array
print(len(data))
