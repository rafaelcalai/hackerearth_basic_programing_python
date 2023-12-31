# Problem
You are conducting a contest at your college. This contest consists of two problems and *n* participants. You know the problem that a candidate will solve during the contest.

You provide a balloon to a participant after he or she solves a problem. There are only green and purple-colored balloons available in a market. Each problem must have a balloon associated with it as a prize for solving that specific problem. You can distribute balloons to each participant by performing the fo llowing operation:

> 1. Use green-colored balloons for the first problem and purple-colored balloons for the second problem 
> 2. Use purple-colored balloons for the first problem and green-colored balloons for the second problem 

You are given the cost of each balloon and problems that each participant solve. Your task is to print the minimum price that you have to pay while purchasing balloons.

### Input format

 - First line: *T* that denotes the number of test cases (1≤ *T* ≤10)
 - For each test case: 
   -  First line: Cost of green and
 purple-colored balloons 
   -  Second line: that denotes the number of participants (1≤ *n* ≤10)
- Next *n* lines: Contain the status of users. For example, if the value of the **j<sup>th</sup>** integer in the **i<sup>th</sup>** row is 0, then it depicts that the **i<sup>th</sup>** participant has not solved the  problem. Similarly, if the value of the **j<sup>th</sup>** integer in the **i<sup>th</sup>** row is 1, then it depicts that the **i<sup>th</sup>** participant has solved the **j<sup>th</sup>** problem.
 
### Output format
For each test case, print the minimum cost that you have to pay to purchase balloons.


| Sample Input | Sample Output |
|--------------|---------------|
|2             | 69            |
|9 6           | 14            |
|10            |               |
|1 1           |               |
|1 1           |               |
|0 1           |               |
|0 0           |               |
|0 1           |               |
|0 0           |               |
|0 1           |               |
|0 1           |               |
|1 1           |               |
|0 0           |               |
|1 9           |               |
|10            |               |
|0 1           |               |
|0 0           |               |
|0 0           |               |
|0 1           |               |
|1 0           |               |
|0 1           |               |
|0 1           |               |
|0 0           |               |
|0 1           |               |
|0 0           |               |



Time Limit: 1s <br>
Memory Limit: 256<br>




