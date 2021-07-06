## Prompt
#### Medium
---

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

    This is not a sum so it is not included.
    1 = 1^4

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

[Link Project Euler](https://projecteuler.net/problem=30)

## Analyze the problem

First, lets define a model.

```
"abc..." = a^n + b^n + c^n + ...
```
For `n > 0`: a, b, and c belong to the set `0 <= x <= 9`, because the length of each digit can only be one.

But what should be the limit? When should the program stop adding digits and checking them?

The rate of growth of the number in the right and the number in the left are different. So much that:
```
Left:
a * 10^k + b * 10^(k-1) + c * 10^(k-2) + ...

Right:
a^n + b^n + c^n + ...
```
If the maximum value a digit can possibly have is 9. Then:
```
9 * 10^k + 9 * 10^(k-1) + 9 * 10^(k-2) + ... = 9^n + 9^n + 9^n + ...

9 * (10^k + 10^(k-1) + 10^(k-2) + ...) = k * 9^n 
```
The growth in the left side is greater than in the right side, so the limit should be when the left side becomes greater than the right side of the equation.
Testing for different values of `k`:
```
For n = 1: (10^k + 10^(k-1) + 10^(k-2) + ...) = k
    k = 1: 1 > 1
    k = 2: 11 > 1  <-- True

For n = 2: (10^k + 10^(k-1) + 10^(k-2) + ...) = k * 9
    k = 1: 1 > 9
    k = 2: 11 > 18
    k = 3: 111 > 27  <-- True

For n = 3: (10^k + 10^(k-1) + 10^(k-2) + ...) = k * 81
    k = 1: 1 > 81
    k = 2: 11 > 162
    k = 3: 111 > 243
    k = 4: 1111 > 324  <-- True 

For n = 4: (10^k + 10^(k-1) + 10^(k-2) + ...) = k * 729
    k = 1: 1 > 729
    k = 2: 11 > 1458
    k = 3: 111 > 2187
    k = 4: 1111 > 2916
    k = 5: 11111 > 3645  <-- True

For n = 5: (10^k + 10^(k-1) + 10^(k-2) + ...) = k * 6561
    k = 1: 1 > 6561
    k = 2: 11 > 13122
    k = 3: 111 > 19683
    k = 4: 1111 > 26244
    k = 5: 11111 > 32805
    k = 6: 111111 > 39366  <-- True 
```
This means that whatever exponent `n` there is a maximum length `k` that the digits can't reach. Defined by:
```
k = n + 1

Limit:
(n + 1) 9^n
```
Also, `n = 1` should be excluded, for obvious reasons. 

## Algorithm design