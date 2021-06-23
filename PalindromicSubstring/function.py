def PalindromicSubstring(stringInput):
  
  # length of the main string
  strLength = len(stringInput)

  # preset max length and starting index of the LPS
  maxLength = 0
  startIndex = 0
  
  # nested for loops where 
  # i is the beginning of the string
  # j is iterates through i and strLenght
  for i in range(strLength):
    for j in range(i, strLength):
      # check if the substring is a palindrome
      # check = 1: is a palindromic
      # check = 0: is not palindromic
      check = 1
      
      # for loop to check is half of the substring is 
      # simetrical to its other half
      for k in range(0, (j - i) // 2 + 1):
        # single diference causes to loose palindromic status
        if (stringInput[i + k] != stringInput[j - k]):
          check = 0

      # checks if substring is palindromic and the longest
      if check != 0 and (j - i + 1) > maxLength:
        # saves its values
        startIndex = i
        maxLength = j - i + 1

  # sets end index of LPS for clarity
  endIndex = startIndex + maxLength
  
  # if LPS is only two or less characters, returns 'none'
  if maxLength <= 2:
    return "none"

  # output
  return stringInput[startIndex:endIndex]
