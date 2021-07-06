from function import DifferentChanges

# hypothetical list to test the function
testset = [
            0.01,
            0.02,
            0.03,
            0.04,
            0.05,
            0.06,
            0.10,
            0.20,
            0.50,
            1.00,
            2.00
          ]

          # Correct outputs
          # 1
          # 2
          # 2
          # 3
          # 4
          # 5
          # 11
          # 41
          # 451
          # 4563
          # 73682

# testing every input in the list
for i in testset:
    print(DifferentChanges(i))