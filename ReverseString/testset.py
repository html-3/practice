from function import ReverseString

# hypothetical list to test the function
testset = [
            "Hello World",
            "Coderbyte",
            "12345",
            "above\nbelow"
          ]

          # Correct Outputs
          # dlroW olleH
          # etybredoC
          # 54321    
          # woleb
          # evoba   
          
# testing every input in the list
for i in testset:
    print(ReverseString(i))