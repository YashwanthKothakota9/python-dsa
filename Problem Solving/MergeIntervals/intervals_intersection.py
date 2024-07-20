# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:

# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

# Now, if we have found that the two intervals overlap, how can we find the overlapped part?

# Again from the above diagram, the overlapping interval will be equal to:

#     start = max(a.start, b.start)
#     end = min(a.end, b.end) 
# That is, the highest start time and the lowest end time will be the overlapping interval.

# So our algorithm will be to iterate through both the lists together to see if any two intervals overlap. If two intervals overlap, we will insert the overlapped part into a result list and move on to the next interval which is finishing early.


# Time Complexity
# As we are iterating through both the lists once, the time complexity of the above algorithm is O(N+M), where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.

# Space Complexity
# Ignoring the space needed for the result list, the algorithm runs in constant space O(1).

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def merge(self, intervals_a, intervals_b):
        result = []
        i, j = 0, 0
        
        while i < len(intervals_a) and j < len(intervals_b):
            # check if intervals overlap and intervals_a[i]'s start time lies within the 
            # other intervals_b[j]
            a_overlaps_b = intervals_a[i].start >= intervals_b[j].start and intervals_a[i].start <= intervals_b[j].end
            
            # check if intervals overlap and intervals_b[j]'s start time lies within the 
            # other intervals_a[i]
            b_overlaps_a = intervals_b[j].start >= intervals_a[i].start and intervals_b[j].start <= intervals_a[i].end
            
            # store the the intersection part
            if a_overlaps_b or b_overlaps_a:
                result.append([max(intervals_a[i].start, intervals_b[j].start), min(intervals_a[i].end, intervals_b[j].end)])
            
            # move next from the interval which is finishing first
            if intervals_a[i].end < intervals_b[j].end:
                i += 1
            else:
                j += 1
        
        return result

def main():
  sol = Solution()
  intervals_a = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
  intervals_b = [Interval(2, 3), Interval(5, 7)]
  print("Intervals Intersection: ", end="")
  print(sol.merge(intervals_a,intervals_b))


  intervals_a = [Interval(1, 3), Interval(5, 7), Interval(9, 12)]
  intervals_b = [Interval(5, 10)]
  print("Intervals Intersection: ", end="")
  print(sol.merge(intervals_a,intervals_b))



main()
