# Given a collection of sticks with different lengths. To combine any two sticks, there's a cost involved, which is equal to the sum of their lengths.

# Connect all the sticks into a single one with the minimum possible cost. Remember, once two sticks are combined, they form a single stick whose length is the sum of the lengths of the two original sticks.

# Examples
# Input: [2, 4, 3]
# Expected Output: 14
# Justification: Combine sticks 2 and 3 for a cost of 5. Now, we have sticks [4,5]. Combine these at a cost of 9. Total cost = 5 + 9 = 14.
# Input: [1, 8, 2, 5]
# Expected Output: 30
# Justification: Combine sticks 1 and 2 for a cost of 3. Now, we have sticks [3, 8, 5]. Combine 3 and 5 for a cost of 8. Now, we have sticks [8,8]. Combine these for a cost of 16. Total cost = 3 + 8 + 16 = 27.
# Input: [5, 5, 5, 5]
# Expected Output: 40
# Justification: Combine two 5s for a cost of 10. Do this again for another cost of 10. Now, we have two sticks of 10 each. Combine these for a cost of 20. Total cost = 10 + 10 + 20 = 40.

# Time Complexity:
# Heap Construction: Constructing a heap from an array has a worst-case time complexity of (O(n log n)), where (n) is the number of elements (sticks) in the array.

# Heap Operations:

# pop operation: Takes (O(log n)) time because in the worst case we might need to rearrange the heap after removing the smallest element.
# push operation: Also takes (O(log n)) time, as we might need to rearrange the heap after adding an element.
# Since we pop two elements and push one element back in each iteration of the loop, and this is done until there's only one element left in the heap, we do these operations roughly (n-1) times.

# So, for (n-1) iterations with 2 pops and 1 push per iteration, the time complexity becomes (O(3(n-1) log n)), which simplifies to (O(n log n)).

# Overall Time Complexity: Combining heap construction and operations, the time complexity remains (O(n log n)).
# Space Complexity:
# Heap Storage: We store all (n) sticks in the heap, so the space complexity is (O(n)).

# Auxiliary Space: We use constant extra space for variables, so the auxiliary space complexity is (O(1)).

# Overall Space Complexity: Combining heap storage and auxiliary space, the space complexity is (O(n) + O(1)), which simplifies to (O(n)).

import heapq

class Solution:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            
            combined = first + second
            cost += combined
            
            heapq.heappush(sticks, combined)
        return cost

sol = Solution()
print(sol.connectSticks([1, 2, 3, 4]))  # Expected: 19
print(sol.connectSticks([3, 4, 5]))     # Expected: 19
print(sol.connectSticks([5, 2, 9, 12])) # Expected: 51
