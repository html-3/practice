from function import ReverseString

# hypothetical list to test the function.
testset = [
            "Hello World",
            "Coderbyte",
            "12345",
            "above\nbelow"
          ]
          
# testing every string in the list
for i in testset:
    print(ReverseString(i))