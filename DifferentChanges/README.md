## Prompt
#### Medium
---

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1 × £1 + 1 × 50p + 2 × 20p + 1 × 5p + 1 × 2p + 3 × 1p

How many different ways can £2 be made using any number of coins?

[Link Project Euler](https://projecteuler.net/problem=31)

## Analyze the problem

Initially, the possibility of painstakingly form all the possible change combinations sounds reasonable, however, doing so is not only suboptimal but also bruttish. 

Lets step back for a second, the prompt asks for the maximum number of different ways a given value can be broken by smaller coins. These smaller values can, by themselves be broken into even smaller coins. This reasoning made explicit that a solution can be reached by creating a recursive function, but beyond that, the problem can be solved with **dynamic programming**.

Dynamic programming (or DP) is a method of solving problems that require maximizing or minimize certain quantities and contain overlapping subproblems. In this case the requirements are met because the combinations must be maximized and the problems depend on the quantity that will be divided and on the differente coins.

To better illustrate this relationship, a table with the result of the smaller problems will be presented.

| Coins / Value | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| [0]  | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| [0, 1] | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| [0, 1, 2] | 1 | 1 | 2 | 2 | 3 | 3 | 4 |
| [0, 1, 2, 5] | 1 | 1 | 2 | 2 | 3 | 4 | 5 |
| [0, 1, 2, 5, 10] | 1 | 1 | 2 | 2 | 3 | 4 | 5 |

Obtaining the subsolutions by brute-forcing, many conclusions can be reached:

- There is only one change combination for the value zero.
- If there are no coins, there can only be zero combinations for any value.
- If there is only the one cent coin, there can only be one combination for any value.
- There exists a relationship between the solutions.

That relationship is:

solution(coins, value) = solution(coins - 1, value) + solution(coins, value - last coin size)

For example, the solution for the coin set [0, 1, 2] and the value 3 is:

```
solution(2, 3) = solution(1, 3) + solution(2, 1)

solution(1, 3) = solution(0, 3) + solution(1, 2) = 0 + 1
solution(2, 1) = solution(1, 1) + solution(1, 1) = 1 + 1

solution(2, 3) = 3
```
As demonstrated, the solutions come from subproblems, which invites dinamic programming.


## Algorithm design

The algorith is designed with a bottom-up dinamic programming aproach. Where smaller problems are solved first to reach the final, or maximum value.
1. The `list` of coins and size of the value in cents are declared
2. The array that contains all the values is formed (as shown in the table above) made from `lists`.
3. A `for` loop nested within another `for` loop is used to iterate over all the cells of the array.
4. An `if` statement is set to avoid out of index and wrong values for the array.