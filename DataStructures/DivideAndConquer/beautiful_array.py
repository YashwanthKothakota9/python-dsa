# Given a positive integer N, construct a beautiful array of size N containing the number [1, N] .

# An array is beneficial if it follows the conditions below.

# If for any three indices i, j, k (with i < j < k), A[j] * 2 is not equal to A[i] + A[k].
# Examples
# Example 1
# Input: 4
# Expected Output: [2, 1, 4, 3]
# Justification: In this array, no combination of i, j, k (where i < j < k) exists such that 2 * A[j] = A[i] + A[k].
# Example 2
# Input: 3
# Expected Output: [1, 3, 2]
# Justification: Similar to example 1, this array also satisfies the condition for a smaller size.
# Example 3
# Input: 8
# Expected Output: [1, 5, 3, 7, 2, 6, 4, 8] (or any other permutation that satisfies the condition)
# Justification: In this array, for every i, j, k (where i < j < k), 2 * A[j] is never equal to A[i] + A[k]. This output ensures that all integers from 1 to 8 are used, and the condition is met for all possible triplets.

# To solve the problem, a divide-and-conquer strategy, which focuses on the inherent properties of odd and even numbers, can be used. The fundamental approach is to construct two separate arrays, one consisting entirely of odd numbers and the other of even numbers. The reason for this segregation is rooted in the basic arithmetic property that the sum of an odd and an even number is always odd. Therefore, by ensuring one array contains only odds and the other only evens, we prevent the formation of any triplet i, j, k (with i < j < k) for which A[j] * 2 = A[i] + A[k].

# To recursively generate these subarrays for smaller sizes, create two smaller beautiful arrays - one for N/2 (even elements) and the other for (N+1)/2 (odd elements). In this recursive process, the base case occurs when N equals 1, yielding a single-element array [1].

# To merge these small subarrays, transform the elements of the odd array by multiplying each by 2 and subtracting 1, thereby preserving their odd nature. Simultaneously, elements of the even array are doubled, maintaining their even status. This transformation is key to maintaining the distinctiveness of the odd and even arrays. Finally, these transformed arrays are concatenated. This final step combines the odd and even elements in such a way that the resulting array maintains the 'beautiful' property for the entire set, adhering to the condition that no triplet of indices i, j, k (with i < j < k) in the array can satisfy A[j] * 2 = A[i] + A[k].


from typing import List


class Solution:
    def beautifulArray(self, N:int)->List[int]:
        if N==1:
            return [1]
        
        odd = self.beautifulArray((N+1)//2)
        even = self.beautifulArray(N // 2)
        
        return [2 * x -1 for x in odd] + [ 2 * x for x in even]


solution = Solution()
print("Beautiful Array for N = 4:", solution.beautifulArray(4))
print("Beautiful Array for N = 3:", solution.beautifulArray(3))
print("Beautiful Array for N = 8:", solution.beautifulArray(8))

# Tc: O(nlogn) Sc: O(nlogn)