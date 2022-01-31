#### Advent of Code - Day 4 - Part 1
# Who wins at bingo, me vs squidy?

### Split the data input into boards and numbers called
boards = []
with open("cat/day-04/small.txt", "r") as file:
    numbersCalled = [int(num) for num in file.readline().strip().split(",")]
    lines = file.readlines()[1:]
    boards = []
    for line in lines:
        boardList = line.strip().split()
        for sublist in boardList:
            boards.append(int(sublist))
    ### Find size of board
    size = int(len(boardList))

    ### The numbers called is going to be a list that we iterate through
    ### Start itterating through the list and swap out number for "blank" if called
    for drawn in numbersCalled:
        boards = ["-" if number == drawn else number for number in boards]
        ### now as we iterate through the numbersCalled list we will slowly reduce each board to "-"
        ### we need to split into individual boards (5*5)
        for location in range(int(len(boards) / (size * size))):
            board = boards[location * size * size : (location + 1) * size * size]
            ### and check if each board has a row or column filled with "-".
            for i in range(size):
                if (
                    board[i * size : (i + 1) * size].count("-") == size
                    or board[i : size * size + i : size].count("-") == size
                ):
                    ### Find the sum of all unmarked numbers on that board
                    ### multiply that sum by the number that was just called = final score
                    print(drawn * sum([0 if v is "-" else v for v in board]))
                    exit()
