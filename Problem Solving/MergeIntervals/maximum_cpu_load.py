# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

# Example 1:

# Jobs: [[1,4,3], [2,5,4], [7,9,6]]
# Output: 7
# Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the jobs are running at the same time i.e., during the time interval (2,4).
# Example 2:

# Jobs: [[6,7,10], [2,4,11], [8,12,15]]
# Output: 15
# Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.
# Example 3:

# Jobs: [[1,4,2], [2,4,1], [3,6,5]]
# Output: 8
# Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4].

# To solve this problem, we'll use a priority queue to keep track of overlapping tasks and their CPU loads. The priority queue helps us efficiently manage which tasks are currently running and their cumulative load. We'll first sort the tasks by their start times. As we iterate through the tasks, we'll remove any tasks from the queue that have already ended before the current task's start time, ensuring we only consider the relevant tasks. This approach allows us to dynamically calculate the current CPU load and update the maximum load observed.

# This method works well because it leverages sorting and a priority queue to maintain an efficient and dynamic set of tasks. By sorting the tasks initially, we ensure we process them in the correct order. Using a priority queue allows us to efficiently manage and update the set of overlapping tasks and their loads. This ensures that our algorithm is both efficient and scalable, handling overlapping tasks without excessive complexity.

# Time Complexity
# The time complexity of the above algorithm is O(NlogN), where ‘N’ is the total number of jobs. This is due to the sorting that we did in the beginning. Also, while iterating the jobs, we might need to poll/offer jobs to the priority queue. Each of these operations can take O(logN) . Overall our algorithm will take O(NlogN).

# Space Complexity
# The space complexity of the above algorithm will be O(N), which is required for sorting. Also, in the worst case, we have to insert all the jobs into the priority queue (when all jobs overlap) which will also take O(N) space. The overall space complexity of our algorithm is O(N).

from heapq import * # type: ignore

class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpuLoad = cpu_load

setattr(Job, '__lt__', lambda self, other: self.end < other.end)

class Solution:
    def findMaxCPULoad(self, jobs):
        
        jobs.sort(key = lambda x: x.start)
        
        max_cpu_load, current_cpu_load = 0, 0
        min_heap = []
        
        for j in jobs:
            # remove all the jobs that have ended
            while len(min_heap) > 0 and j.start >= min_heap[0].end:
                current_cpu_load -= min_heap[0].cpuLoad
                heappop(min_heap)
            
            # add the current job into min_heap
            heappush(min_heap, j)
            current_cpu_load += j.cpuLoad
            max_cpu_load = max(max_cpu_load, current_cpu_load)
        
        return max_cpu_load

def main():
  sol = Solution()
  print("Maximum CPU load at any time: " + 
            str(sol.findMaxCPULoad([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + 
            str(sol.findMaxCPULoad([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + 
            str(sol.findMaxCPULoad([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))

main()