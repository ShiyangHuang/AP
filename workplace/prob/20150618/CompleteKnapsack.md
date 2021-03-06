# Description

Given N kind of items where the ith kind of item has infinite ones and each of them has size c[i] and value w[i] [1 <= i <= N], design an algorithm to maximize the total value of items filled into a knapsack with capacity V. So the sum of sizes in the knapsack shouldn't be bigger than V.

## Input File

1) Line 1: Number of test cases

2) Line 2: N and V

3) Line 3: N integers, each of which is the maximal size of the corresponding item for testcase#1

4) Line 4: N integers, each of which is the maximal value of the corresponding item for testcase#1

5) Line 5: blanket line

Repeat the Line 2 to Line 5 for the remaining test cases.

## Output File 

1) Line 1: Maximal values for testcase#1

2) Line 2: N integers, each of which is the amount of the corresponding item filled into the knapsack

3) Line 3: blanket line

Repeat the Line 1 to Line 3 for the remaining test cases.

## Requirement

You should implement both top-down and bottom-up dp solution. Any non-dp (e.g greedy) methods are welcome!

## Example

### Input
2
<br>
3 4
<br>
2 1 3
<br>
6 4 2
<br><br>
3 5
<br>
2 1 3
<br>
6 4 2

### Output
16
<br>
0 4 0
<br><br>
20
<br>
0 5 0




