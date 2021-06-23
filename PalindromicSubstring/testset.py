from function import PalindromicSubstring

# hypothetical list to test the function.
testset = [
            "abcdefgg",
            "dogcatfish",
            "1331",
            "aracecar"
          ] 
          
          # Correct Outputs
          # none
          # none
          # 1331
          # racecar
          
# testing every string in the list
for i in testset:
    print(PalindromicSubstring(i))