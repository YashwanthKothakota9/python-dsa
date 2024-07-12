# You're presented with several piles of gifts, with each pile containing a certain number of gifts. Every second, you'll engage in the following activity:

# Pick the pile that contains the highest number of gifts. If multiple piles share this distinction, you can select any of them.
# Compute the square root of the number of gifts in the selected pile, and then leave behind that many gifts (rounded down). Take all the other gifts from this pile.
# You'll do this for "k" seconds. The objective is to find out how many gifts would still remain after these "k" seconds.
# Examples
# Input: gifts = [4, 9, 16], k = 2
# Expected Output: 11
# Justification:
# Take from third pile (16 gifts): leave (  ) = 4 gifts, take 12. Remaining gifts = [4, 9, 4]
# Take from second pile (9 gifts): leave (  ) = 3 gifts, take 6. Remaining gifts = [4, 3, 4]
# Input: gifts = [1, 2, 3], k = 1
# Expected Output: 4
# Justification:
# Take from third pile (3 gifts): leave (  ) = 1 gift (rounded down), take 2. Remaining gifts = [1, 2, 1]
# Input: gifts = [25, 36, 49], k = 3
# Expected Output: 18
# Justification:
# Take from third pile (49 gifts): leave (  ) = 7 gifts, take 42. Remaining gifts = [25, 36, 7]
# Take from second pile (36 gifts): leave (  ) = 6 gifts, take 30. Remaining gifts = [25, 6, 7]
# Take from first pile (25 gifts): leave (  ) = 5 gifts, take 20. Remaining gifts = [5, 6, 7]
# Constraints:

# 1 <= gifts.length <= 103
# 1 <= gifts[i] <= 109
# 1 <= k <= 103


import heapq

class Solution:
    def remainingGifts(self, gifts, k):
        # Create a max heap. We achieve this by inserting negative numbers into a min heap.
        # We use a list comprehension to negate each gift as we populate the max_heap.
        max_heap = [-gift for gift in gifts]
        
        # Convert the list into a heap in-place. This operation ensures the list maintains heap properties.
        heapq.heapify(max_heap)
        
        for _ in range(k):
            current = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -int(current ** 0.5))
        
        return -sum(max_heap)
    
sol = Solution()
print(sol.remainingGifts([4, 9, 16], 2))  # Expected: 11
print(sol.remainingGifts([1, 2, 3], 1))  # Expected: 4
print(sol.remainingGifts([25, 36, 49], 3))  # Expected: 18

