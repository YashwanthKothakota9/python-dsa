# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
# Example 2:

# Intervals: [[6,7], [2,4], [13, 14], [8,12], [45, 47]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.
# Example 3:

# Intervals: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

# To solve this problem, we need to check if any of the given meeting times overlap. The best way to do this is by first sorting the intervals based on their start times. Once sorted, we can then iterate through the list and compare each interval with the previous one to see if there is any overlap.

# This approach works efficiently because by sorting the intervals, we ensure that if there is an overlap, it will be between consecutive intervals. This reduces the problem to a simpler check, making the solution both effective and easy to understand.


# Time Complexity
# The time complexity of the above algorithm is O(N*logN), where ‘N’ is the total number of appointments. Though we are iterating the intervals only once, our algorithm will take O(N * logN) since we need to sort them in the beginning.

# Space Complexity
# The space complexity of the above algorithm will be O(N), which we need for sorting.

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendAllAppointments(self, intervals):
        intervals.sort(key = lambda x : x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                # please note the comparison above, it is "<" and not "<="
                # while merging we needed "<=" comparison, as we will be merging the two
                # intervals having condition "intervals[i][start] == intervals[i - 1][end]" but
                # such intervals don't represent conflicting appointments as one starts right
                # after the other
                return False
        return True

def main():
  sol = Solution()
  print("Can attend all appointments: " + 
            str(sol.canAttendAllAppointments([Interval(1, 4), Interval(2, 5), Interval(7, 9)])))
  print("Can attend all appointments: " + 
            str(sol.canAttendAllAppointments([Interval(6, 7), Interval(2, 4),Interval(8, 12)])))
  print("Can attend all appointments: " + 
            str(sol.canAttendAllAppointments([Interval(4, 5), Interval(2, 3), Interval(3, 6)])))


main()

