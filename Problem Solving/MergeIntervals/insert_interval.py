# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
# Example 2:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
# Example 3:

# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

# Time Complexity
# As we are iterating through all the intervals only once, the time complexity of the above algorithm is O(N) , where ‘N’ is the total number of intervals.

# Space Complexity
# Ignoring the space needed for the result list, the algorithm runs in constant space O(1) .

# If we include the result list, the space complexity will be O(N) as we need to return a list containing all the merged intervals.

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def insert(self, intervals, new_interval):
        merged = []
        i = 0
        
        # skip (and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) and intervals[i].end < new_interval.start:
            merged.append(intervals[i])
            i+=1
        
        # merge all intervals that overlap with 'new_interval'
        while i < len(intervals) and intervals[i].start <= new_interval.end:
            new_interval.start = min(intervals[i].start, new_interval.start)
            new_interval.end = max(intervals[i].end, new_interval.end)
            i+=1
        
        # insert the new_interval
        merged.append(new_interval)
        
        # add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i+=1
        
        return merged
    
def print_interval(i):
    print(f"[{i.start}, {i.end}]")

def main():
  sol = Solution()
  intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
  print("Intervals after inserting the new interval: ",end="")
  for i in (sol.insert(intervals, Interval(4, 6))):
    print_interval(i)
  print()
  
  intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
  print("Intervals after inserting the new interval: ",end="")
  for i in (sol.insert(intervals, Interval(4, 10))):
    print_interval(i)
  print()

  intervals = [Interval(2, 3), Interval(5, 7)]
  print("Intervals after inserting the new interval: ",end="")
  for i in (sol.insert(intervals, Interval(1, 4))):
    print_interval(i)
  print()
  
main()
