# You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

# If at any time the server can’t execute any task then it must stay idle.

# Example 1:

# Input: [a, a, a, b, c, c], K=2
# Output: 7
# Explanation: a -> c -> b -> a -> c -> idle -> a
# Example 2:

# Input: [a, b, a], K=3
# Output: 5
# Explanation: a -> b -> idle -> idle -> a




# This problem follows the Top 'K' Numbers pattern and is quite similar to Rearrange String K Distance Apart. We need to rearrange tasks such that same tasks are ‘K’ distance apart.

# Following a similar approach, we will use a Max Heap to execute the highest frequency task first. After executing a task we decrease its frequency and put it in a waiting list. In each iteration, we will try to execute as many as k+1 tasks. For the next iteration, we will put all the waiting tasks back in the Max Heap. If, for any iteration, we are not able to execute k+1 tasks, the CPU has to remain idle for the remaining time in the next iteration.



from heapq import *


class Solution:
    def scheduleTasks(self, tasks, k):
        interval_count = 0
        task_freq_map = {}
        for char in tasks:
            task_freq_map[char] = task_freq_map.get(char,0)+1
        
        maxHeap = []
        # add all tasks to the max heap
        for char,freq in task_freq_map.items():
            heappush(maxHeap, (-freq,char))
        
        while maxHeap:
            wait_list = []
            n = k+1 # try to execute as many as 'k+1' tasks from the max-heap
            while n > 0 and maxHeap:
                interval_count += 1
                freq, char = heappop(maxHeap)
                if -freq > 1:
                    # decrement the frequency and add to the waitList
                    wait_list.append((freq+1, char))
                n -= 1
            
            # put all the waiting list back on the heap
            for freq, char in wait_list:
                heappush(maxHeap, (freq,char))
            
            if maxHeap:
                interval_count += n # we'll be having 'n' idle intervals for the next iteration
        return interval_count


def main():
  sol = Solution()
  print("Minimum intervals needed to execute all tasks: " +
        str(sol.scheduleTasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(sol.scheduleTasks(['a', 'b', 'a'], 3)))


main()



# Time Complexity
# The time complexity of the above algorithm is O(N∗logN) where ‘N’ is the number of tasks. Our while loop will iterate once for each occurrence of the task in the input (i.e. ‘N’) and in each iteration we will remove a task from the heap which will take O(logN) time. Hence the overall time complexity of our algorithm is O(N∗logN).

# Space Complexity
# The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ tasks in the HashMap