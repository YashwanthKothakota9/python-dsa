# Given divisor1, divisor2, uniqueCnt1, and uniqueCnt2 integers, find the smallest possible maximum integer that could be present in either array after they are filled according to the below conditions.

# You can take two arrays arr1 and arr2 which are initially empty.
# arr1 contains total uniqueCnt1 different positive integers, each of them is not divisible by divisor1.
# arr2 contains total uniqueCnt2 different positive integers, each of them is not divisible by divisor2.
# There are no common integers in both arrays.

# Example 1:

# Input: uniqueCnt1 = 2, divisor1 = 2, uniqueCnt2 = 2, divisor2 = 3
# Expected Output: 4
# Explanation: The optimal arrays could be arr1 = [1, 3] (numbers not divisible by 2) and arr2 = [2, 4] (numbers not divisible by 3). The maximum number among both arrays is 4.
# Example 2:

# Input: uniqueCnt1 = 3, divisor1 = 3, uniqueCnt2 = 4, divisor2 = 4
# Expected Output: 7
# Explanation: Possible arrays are arr1 = [1, 2, 4] and arr2 = [3, 5, 6, 7]. The highest integer used is 7.
# Example 3:

# Input: uniqueCnt1 = 1, divisor1 = 7, uniqueCnt2 = 1, divisor2 = 10
# Expected Output: 2
# Explanation: We can use arr1 = [1] (since it's not divisible by 7) and arr2 = [2] (since it's not divisible by 10). The highest integer here is 2.


# To solve this problem, the approach involves generating two sets of integers for arr1 and arr2 that adhere to their respective divisibility conditions. This process can be streamlined using a binary search method to determine the smallest possible maximum integer in an efficient manner. By setting an upper and lower bound and validating each midpoint in the binary search, we can check if it's possible to meet the conditions with the current maximum value.

# This method is both efficient and effective, as it systematically narrows down the potential maximum value without having to explicitly generate each possible combination of arrays.

class Solution:
    # Function to calculate the greatest common divisor (GCD)
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
     # Function to minimize the maximum value in the two sets based on given conditions
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        low, high = uniqueCnt1 + uniqueCnt2, divisor1*divisor2*uniqueCnt1*uniqueCnt2 # Setting initial search bounds
        lcm = (divisor1 * divisor2) // self.gcd(divisor1, divisor2) # Calculate the least common multiple (LCM)

        while low <= high:
            mid = (low + high) // 2
            countBoth = mid // lcm # Numbers divisible by both divisor1 and divisor2
            
            # Checking if the current mid can satisfy the conditions
            if (mid - countBoth >= uniqueCnt1 + uniqueCnt2) and (mid - (mid // divisor1) >= uniqueCnt1) and (mid - (mid // divisor2) >= uniqueCnt2):
                high = mid - 1 # Adjust high to find smaller max
            else:
                low = mid + 1 # Adjust low to find feasible max
        return low # The minimum possible maximum value that satisfies the conditions

solution = Solution()

# Test Example 1
print("Output for Example 1:", solution.minimizeSet(2, 3, 2, 2)) # Expected Output: 4

# Test Example 2
print("Output for Example 2:", solution.minimizeSet(3, 4, 3, 4)) # Expected Output: 7

# Test Example 3
print("Output for Example 3:", solution.minimizeSet(7, 10, 1, 1)) # Expected Output: 2


# The time complexity of the minimizeSet function primarily revolves around the binary search mechanism used to narrow down the potential maximum integer:

# Binary Search: The loop runs as long as low is less than or equal to high. Each iteration approximately halves the search space, making the time complexity logarithmic. Given that the high is initialized to divisor1 * divisor2 * uniqueCnt1 * uniqueCnt2, the number of iterations is around O(log(divisor1*divisor2*uniqueCnt1*uniqueCnt2)), which is about 40.
# GCD Calculation: The time complexity of the Euclidean algorithm to compute the GCD is O(log(min(a,b))), where a and b are the inputs to the GCD function. However, this computation is done once and hence does not significantly impact the overall complexity.
# Overall, the time complexity of the minimizeSet function is O(log(maxRange)), where maxRange is the difference between the initial high and low values, scaled logarithmically by the binary search.

# Space Complexity
# The space complexity of the solution is O(1) as the function utilizes a fixed amount of space for its variables (low, high, mid, countBoth, count1, count2, and lcm), and there are no dynamically sized data structures used.