def PowerSum(n):

    # what should be the limit?
    upperLimit = (n + 1) * 9 ** n

    # initual number of the sequence
    num = 0

    # sum of the sum of powers
    sum = 0

    # loop for every single number within the limit
    while num <= upperLimit:

        # length of the number
        numS = str(num)

        # avoid 1 = 1^n, not a sum
        if len(str(numS)) == 1:
            num += 1
            continue

        # "ab" = a^n + b^n
        elif len(str(numS)) == 2 and num == int(numS[0]) ** n + int(numS[1]) ** n:
            sum += num

        # "abc" = a^n + b^n + c^n
        elif len(str(numS)) == 3 and num == int(numS[0]) ** n + int(numS[1]) ** n + int(numS[2]) ** n:
            sum += num

        # "abcd" = a^n + b^n + c^n + d^n
        elif len(str(numS)) == 4 and num == int(numS[0]) ** n + int(numS[1]) ** n + int(numS[2]) ** n + int(numS[3]) ** n:
            sum += num

        # "abcde" = a^n + b^n + c^n + d^n + e^n    
        elif len(str(numS)) == 5:
            if num == int(numS[0]) ** n + int(numS[1]) ** n + int(numS[2]) ** n + int(numS[3]) ** n  + int(numS[4]) ** n:
                sum += num

        # "abcdef" = a^n + b^n + c^n + d^n + e^n + f^n     
        elif len(str(numS)) == 6:
            if num == int(numS[0]) ** n + int(numS[1]) ** n + int(numS[2]) ** n + int(numS[3]) ** n  + int(numS[4]) ** n  + int(numS[5]) ** n:
                sum += num

        num += 1

    return sum