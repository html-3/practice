def DifferentChanges(n):

    # value in cents
    value = int(n * 100)

    # list of available coins
    listCoins = [0, 1, 2, 5, 10, 20, 50, 100, 200]

    # number of coins
    numberCoins = len(listCoins)

    # first axis is the value of the coin
    # second axis is the number of available coins
    # first column of every line is 1
    line = [1] + [None] * value
    solutions = [line] * numberCoins

    # first line of every line is 0
    # second line of every line is 1
    solutions[0] = [0] * (value + 1)
    solutions[1] = [1] * (value + 1)

    # correction
    solutions[0][0] = 1

    # line
    for i in range(2, numberCoins):

        # column
        for j in range(1, value + 1):
            
            if j - listCoins[i] < 0:
                solutions[i][j] = solutions[i - 1][j] + 0
            else:
                solutions[i][j] = solutions[i - 1][j] + solutions[i][j - listCoins[i]]

    return solutions[numberCoins - 1][value]
