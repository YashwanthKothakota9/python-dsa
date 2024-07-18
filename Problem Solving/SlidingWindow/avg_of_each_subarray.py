# Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

# Tc: O(N) Sc: O(1)

from typing import List


class Solution:
    def findAverages(self, k: int, arr: List[int]) -> List[float]:
        result: List[float] = []
        windowSum: float = 0.0
        windowStart: int = 0
        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]
            if windowEnd >= k-1:
                result.append(windowSum/k)
                windowSum -= arr[windowStart]
                windowStart += 1
        return result

def main() -> None:
  sol = Solution()
  result: List[float] = sol.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()