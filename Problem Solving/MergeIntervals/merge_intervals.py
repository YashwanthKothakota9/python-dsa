# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

# To solve this problem, we will sort the list of intervals by their start times. This helps in easily identifying overlapping intervals. After sorting, we can iterate through the intervals, merging them if they overlap. We will maintain a list to store the merged intervals. As we iterate, we compare the current interval with the last interval in the merged list. If they overlap, we merge them by extending the end time. Otherwise, we add the current interval to the merged list.

# This approach works because sorting brings overlapping intervals next to each other. This allows us to handle overlapping intervals in a single pass through the list. Sorting the intervals first is key to simplifying the merging process. The overall

# Tc: O(NlogN) Sc: O(N)

from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end

def print_interval(i: Interval) -> None:
    print(f"[{i.start}, {i.end}]", end='')

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key = lambda x: x.start)
        
        mergedIntervals: List[Interval] = []
        start: int = intervals[0].start
        end: int = intervals[0].end
        for i in range(1, len(intervals)):
            interval: Interval = intervals[i]
            if interval.start <= end:
                end = max(interval.end, end)
            else:
                mergedIntervals.append(Interval(start, end))
                start = interval.start
                end = interval.end
        
        mergedIntervals.append(Interval(start, end))
        return mergedIntervals

def main() -> None:
  sol: Solution = Solution()
  print("Merged intervals: ", end='')
  for i in sol.merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    print_interval(i)
  print()

  print("Merged intervals: ", end='')
  for i in sol.merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    print_interval(i)
  print()

  print("Merged intervals: ", end='')
  for i in sol.merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    print_interval(i)
  print()


main()


