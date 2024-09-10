# Numbers can be regarded as the product of their factors.

# For example, 8 = 2 x 2 x 2 = 2 x 4.

# Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

# Example 1:

# Input: n = 8
# Output: [[2, 2, 2], [2, 4]]
# Example 2:

# Input: n = 20
# Output: [[2, 2, 5], [2, 10], [4, 5]]

# We can use backtracking to find all the factors of a given number n.

# We will start by iterating through all integers from start (2 by default) to the square root of n+1. If the current integer i divides n, we will add i to the list of current factors curr and appends this list along with the corresponding factor of n/i to the list of all factors (result). Then we can recursively call the function with n/i as the new input, i as the new start value, and curr and result as the current factors and results. After each recursive call, we have to pop the last element from curr to backtrack and find other factors.

class Solution:
    def getAllFactors(self, n, start, curr, result):
        # Iterate through all integers i from start to the square root of n + 1
        # This loop is used to find all the factors of the input number n
        for i in range(start, int(n**0.5)+1):
            # If n is divisible by i, add i to the curr list of factors
            # curr is used to store the current factors being calculated
            if n % i == 0:
                # Found a factor, append it to the list of factors
                curr.append(i)
                # Append the current factors and the corresponding factor of n // i to the result list
                result.append(list(curr + [n//i]))
                # Recursively call the function with n // i as the new input, i as the new start value, and curr and result as the current factors and results
                self.getAllFactors(n//i, i, curr, result)
                curr.pop()  # Pop the last element from curr to backtrack and find other factors
        return result

    def getFactors(self, n):
        return self.getAllFactors(n, 2, [], [])


sol = Solution()
print(sol.getFactors(8))  # expected: [[2, 2, 2], [2, 4]]
print(sol.getFactors(12))  # expected: [[2, 2, 3], [2, 6], [3, 4]]
# expected: [[2, 2, 2, 2], [2, 2, 4], [2, 8], [4, 4]]
print(sol.getFactors(16))
print(sol.getFactors(20))  # expected: [[2, 2, 5], [2, 10], [4, 5]]
print(sol.getFactors(1))  # expected: []


# Time Complexity
# We can't have more than O(n) factors of a number n. This means that getAllFactors can be called a maximum of O(n) times recursively. The for loop iterates a maximum of O(sqrt(n)). This means that the overall time complexity is O(n*sqrt(n)) or O(n^1.5)

# Space Complexity
# Ignoring the space needed for the output array, the space complexity will be O(logn) as we need to save only one factor while in the recursion, and our recursion tree won't get bigger than O(logn) steps.
