def PalindromicSubstring(string):
  
  strLength = len(string)

  maxLength = 0
  starIndex = 0
  

  for i in range(strLength):
    for j in range(i, strLength):
      
      check = 1
      
      for k in range(0, (j - i) // 2 + 1):
        if (string[i + k] != string[j - k]):
          check = 0

      if check != 0 and (j - i + 1) > maxLength:
        starIndex = i
        maxLength = j - i + 1

  endIndex = starIndex + maxLength
  
  if maxLength <= 2:
    return ""

  return string[starIndex:endIndex]
