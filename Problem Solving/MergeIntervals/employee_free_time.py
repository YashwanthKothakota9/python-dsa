# For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.

# Example 1:

# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
# Output: [3,5]
# Explanation: All the employees are free between [3,5].
# Example 2:

# Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
# Output: [4,6], [8,9]
# Explanation: All employees are free between [4,6] and [8,9].
# Example 3:

# Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
# Output: [5,7]
# Explanation: All employees are free between [5,7].


# Using the input Employee Working Hours = [[[1, 3], [9, 12]], [[2, 4]], [[6, 8]]]:

# Initialize result list: [].
# Initialize priority queue with the first intervals of each employee: [(1, 3), (2, 4), (6, 8)], each represented as an EmployeeInterval object containing the interval, employee index, and interval index:
# Priority queue: [(1, 3, 0, 0), (2, 4, 1, 0), (6, 8, 2, 0)]
# Set previousInterval to the interval with the earliest start time, (1, 3).
# While the priority queue is not empty:
# Remove (1, 3, 0, 0) from the queue. Priority queue: [(2, 4, 1, 0), (6, 8, 2, 0)].
# Check if there is a gap between previousInterval and the current interval (2, 4):
# No gap, update previousInterval to (2, 4).
# If employee 0 has more intervals, add next interval (9, 12) to the queue. Priority queue: [(2, 4, 1, 0), (6, 8, 2, 0), (9, 12, 0, 1)].
# Remove (2, 4, 1, 0) from the queue. Priority queue: [(6, 8, 2, 0), (9, 12, 0, 1)].
# Check if there is a gap between previousInterval and the current interval (6, 8):
# Gap found between (4, 6). Add this interval to result: result = [[4, 6]].
# Update previousInterval to (6, 8).
# Remove (6, 8, 2, 0) from the queue. Priority queue: [(9, 12, 0, 1)].
# Check if there is a gap between previousInterval and the current interval (9, 12):
# Gap found between (8, 9). Add this interval to result: result = [[4, 6], [8, 9]].
# Update previousInterval to (9, 12).
# Remove (9, 12, 0, 1) from the queue. Priority queue is now empty.
# Return result: [[4, 6], [8, 9]].


# Time Complexity
# The above algorithm’s time complexity is O(NlogK) , where ‘N’ is the total number of intervals, and ‘K’ is the total number of employees. This is because we are iterating through the intervals only once (which will take O(N)), and every time we process an interval, we remove (and can insert) one interval in the Min Heap, (which will take O(LogK)). At any time, the heap will not have more than ‘K’ elements.

# Space Complexity
# The space complexity of the above algorithm will be O(K) as at any time, the heap will not have more than K elements.

from heapq import *

class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex
    
    def __lt__(self, other):
        return self.interval.start < other.interval.start

class Solution:
    def findEmployeeFreeTime(self, schedule):
        if schedule is None:
            return
        
        n = len(schedule)
        result, minHeap = [], []
        
        # insert the first interval of each employee to the queue
        for i in range(n):
            heappush(minHeap, EmployeeInterval(schedule[i][0],i,0))
        
        previousInterval = minHeap[0].interval
        while minHeap:
            queueTop = heappop(minHeap)
            # if previousInterval is not overlapping with the next interval, insert a free 
            # interval
            if previousInterval.end < queueTop.interval.start:
                result.append(Interval(previousInterval.end,
                                    queueTop.interval.start))
                previousInterval = queueTop.interval
            else:  # overlapping intervals, update the previousInterval if needed
                if previousInterval.end < queueTop.interval.end:
                    previousInterval = queueTop.interval
            
            # if there are more intervals available for the same employee, add their next 
            # interval
            employeeSchedule = schedule[queueTop.employeeIndex]
            if len(employeeSchedule) > queueTop.intervalIndex + 1:
                heappush(minHeap, EmployeeInterval(
                        employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                        queueTop.intervalIndex + 1))
        
        return result

def print_interval(i):
    print("[" + str(i.start) + ", " + str(i.end) + "]", end='')

def main():
  sol = Solution()
  input = [[Interval(1, 3), Interval(5, 6)], [
      Interval(2, 3), Interval(6, 8)]]
  print("Free intervals: ", end='')
  for interval in sol.findEmployeeFreeTime(input): # type: ignore
      print_interval(interval)
  print()

  input = [[Interval(1, 3), Interval(9, 12)], [
      Interval(2, 4)], [Interval(6, 8)]]
  print("Free intervals: ", end='')
  for interval in sol.findEmployeeFreeTime(input): # type: ignore
      print_interval(interval)
  print()

  input = [[Interval(1, 3)], [
      Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
  print("Free intervals: ", end='')
  for interval in sol.findEmployeeFreeTime(input): # type: ignore
      print_interval(interval)
  print()


main()

            