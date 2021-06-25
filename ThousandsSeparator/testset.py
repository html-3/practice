from function import ThousandsSeparator

# hypothetical list to test the function.
testset = [
            420,
            1000,
            -30,
            27000,
            99999999,
            123456789,
          ]

          # Correct outputs
          # 420
          # 1,000
          # 30
          # 27,000
          # 99,999,999
          # 123,456,789 

# testing every integer in the list
for i in testset:
    print(ThousandsSeparator(i))