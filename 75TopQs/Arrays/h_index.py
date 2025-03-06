# Problem Statement
# Given an integer array citations where citations[i] represents the number of times a researcher's ith paper has been cited, return the researcher's h-index.

# The h-index is defined as the maximum number h such that the researcher has h papers with at least h citations each.

# Examples
# Example 1
# Input: citations = [4, 3, 0, 1, 5]
# Expected Output: 3
# Justification: The researcher has 3 papers with at least 3 citations each.
# Example 2
# Input: citations = [10, 8, 5, 4, 3, 7, 2, 1]
# Expected Output: 4
# Justification: The researcher has 4 papers with at least 4 citations each.
# Example 3
# Input: citations = [0, 1, 2, 3, 4]
# Expected Output: 2
# Justification: The researcher has 2 papers with at least 2 citations each.
# Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
# Solution
# To solve this problem, we use an array to count the number of papers with a given number of citations. This approach helps us determine the h-index efficiently. First, we count how many papers have each citation count, capping at the total number of papers. Then, we traverse the array from the highest possible citation count to the lowest, summing the counts until the sum is at least as large as the current index. This index represents the h-index.

# This approach works well because it avoids the need to sort the array, which is the bottleneck in the traditional solution. By counting citations directly, we reduce the time complexity to O(n), making the solution faster and more scalable.

# Step-by-step Algorithm
# Initialize: Create an array papers of size n + 1 to count papers for each citation number, where n is the length of the input array citations.
# Count Papers: Iterate through each citation in citations. For each citation count c, increment the corresponding index in papers by one. If c is greater than n, increment papers[n] instead.
# Find h-index:
# Start from the highest possible citation count (n).
# Initialize a sum variable s to the count of papers with the highest citation.
# Iterate downwards through the papers array. For each index k, if s is less than or equal to k, add the count at the current index to s and move to the next lower index.
# Return the current index k when s is greater than or equal to k.
# Algorithm Walkthrough
# Input: citations = [10, 8, 5, 4, 3, 7, 2, 1]

# Step 1: Initialize papers array: [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Step 2: Count papers for each citation:
# citations = [10, 8, 5, 4, 3, 7, 2, 1]
# papers = [0, 1, 1, 1, 1, 1, 0, 1, 0, 2]
# Step 3: Find h-index:
# Start with k = 8 and s = 2 (papers[8])
# For k = 8, s = 2 + 0 = 2 (move to next)
# For k = 7, s = 2 + 1 = 3 (move to next)
# For k = 6, s = 3 + 0 = 3 (move to next)
# For k = 5, s = 3 + 1 = 4 (move to next)
# For k = 4, s = 4 + 1 = 5 (stop, since s >= k)
# Step 4: Return h = 4

# Complexity Analysis
# Time Complexity: Counting the citations takes o(n), and finding the h-index also takes O(n). Thus, the overall time complexity is O(n).
# Space Complexity: The algorithm uses O(n) additional space for the papers array.


class Solution:
    def h_index(self, citations):
        n = len(citations)
        papers = [0]*(n+1)
        # Count papers for each citation number
        for c in citations:
            papers[min(n, c)] += 1
        print(papers)
        # Find the h-index
        k = n
        s = papers[n]
        while k > s:
            k -= 1
            s += papers[k]
        return k


if __name__ == "__main__":
    sol = Solution()
    print(sol.h_index([4, 3, 0, 1, 5]))  # Output: 3
    print(sol.h_index([10, 8, 5, 4, 3, 7, 2, 1]))  # Output: 4
    print(sol.h_index([0, 1, 2, 3, 4]))  # Output: 2


class Solution2:
    def h_index(self, citations):
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i+1:
                h = i+1
            else:
                break
        return h
