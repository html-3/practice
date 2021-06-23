from function import BinaryTree

# hypothetical list to test the function.
testset = [
            ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"],
            ["(1,2)", "(2,4)", "(7,2)"], 
            ["(1,2)", "(3,2)", "(2,12)", "(5,2)"],
            ["(2,5)", "(2,6)"],
            ["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)"],
            ["(5,6)", "(6,3)", "(2,3)", "(12,5)"],
            ["(10,20)"],
            ["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)", "(1,9)"],
            ["(10,20)", "(20,50)"]
          ]

          # true
          # true
          # false
          # false
          # true
          # true
          # true
          # false
          # true

# testing every string in the list
for i in testset:
    print(BinaryTree(i))