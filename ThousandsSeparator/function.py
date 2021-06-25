def ThousandsSeparator(intInput):
    # make the interger positive
    numString = str(-intInput) if intInput < 0 else str(intInput)
    newNumString = ""

    # initial length of the original string
    length = len(numString)

    while length > 0:
        # variable length of the original string
        length = len(numString)

        # when the string is smaller than one thousand
        if length < 4:
            newNumString = numString[0:length] + newNumString
            return newNumString
        
        # standar procedure to add the commmas to the number
        newNumString = "," + numString[-3:] + newNumString
        numString = numString[0:-3]

    return newNumString
