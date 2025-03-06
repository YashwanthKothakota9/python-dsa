# There are n kids with candies. You are given a candies array containing integers, where candies[i] denotes the number of candies the ith kid has, and an integer extraCandies, represents the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving all the extraCandies to the ith kid, he/she will have the maximum number of candies among all the kids, or false otherwise.

# Note: Multiple kids can have the maximum number of candies.

# Examples
# Example 1:

# Input: candies = [7, 3, 9, 2, 4], extraCandies = 5
# Expected Output: [true, false, true, false, true]
# Justification: If you give all extraCandies to:
# Kid 1, they will have 7 + 5 = 12 candies, which is the maximum among the kids.
# Kid 2, they will have 3 + 5 = 8 candies, which is not the greatest among the kids.
# Kid 3, they will have 9 + 5 = 14 candies, which is the greatest among the kids.
# Kid 4, they will have 2 + 5 = 7 candies, which is not the greatest among the kids.
# Kid 5, they will have 4 + 5 = 9 candies, which is the greatest among the kids.
# Example 2:

# Input: candies = [5, 8, 6, 4, 2], extraCandies = 3
# Expected Output: [true, true, true, false, false]
# Justification: Giving 3 extra candies to the first, second, and third kid will make their totals 8, 11, and 9 respectively, which are the highest. Other kids can't reach these totals.
# Example 3:

# Input: candies = [1, 2, 3, 4, 5], extraCandies = 4
# Expected Output: [true, true, true, true, true]
# Justification: Giving 4 extra candies to each kid will make their totals 5, 6, 7, 8, and 9 respectively, which means they all can potentially have the highest number of candies.

# Algorithm Walkthrough
# Input: candies = [7, 3, 9, 2, 4], extraCandies = 5

# Find the maximum candies: maxCandies = 9
# Initialize result list: result = []
# For each kid:
# Kid 1: 7 + 5 = 12 >= 9 (true)
# Kid 2: 3 + 5 = 8 < 9(false)
# Kid 3: 9 + 5 = 14 >= 9(true)
# Kid 4: 2 + 5 = 7 < 9(false)
# Kid 5: 4 + 5 = 9 >= 9(true)
# Return: [true, false, true, false, true]


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = [candy + extraCandies >= maxCandies for candy in candies]
        return result


if __name__ == "__main__":
    solution = Solution()
    candies1 = [7, 3, 9, 2, 4]
    extraCandies1 = 5
    # [true, false, true, false, true]
    print(solution.kidsWithCandies(candies1, extraCandies1))

    # Example 2
    candies2 = [5, 8, 6, 4, 2]
    extraCandies2 = 3
    # [true, true, true, false, false]
    print(solution.kidsWithCandies(candies2, extraCandies2))

    # Example 3
    candies3 = [1, 2, 3, 4, 5]
    extraCandies3 = 4
    # [true, true, true, true, true]
    print(solution.kidsWithCandies(candies3, extraCandies3))


# Time Complexity
# Finding the maximum number of candies in the list takes O(n) time, where n is the number of kids.
# Checking each kid's candies after adding the extra candies also takes O(n) time.
# Therefore, the overall time complexity is O(n).
# Space Complexity
# The space complexity is O(n) due to the space required to store the result list, which has the same length as the input list of candies.
