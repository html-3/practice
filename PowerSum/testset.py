from function import PowerSum

# hypothetical list to test the function
testset = [
            1,
            2,
            3,
            4,
            5,
            6
          ]

          # Correct outputs
          # 0
          # 0
          # 1301
          # 19316
          # 443839
          # 548834

# testing every input in the list
for i in testset:
    print(PowerSum(i))