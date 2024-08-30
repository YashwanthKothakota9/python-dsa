# Design a class that simulates a Stack data structure, implementing the following two operations:

# push(int num): Pushes the number ‘num’ on the stack.
# pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.
# Example:

# After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

# 1. pop() should return 2, as it is the most frequent number
# 2. Next pop() should return 1
# 3. Next pop() should return 2
# Constraints:

# 0 <= val <= 109
# At most 2 * 104 calls will be made to push and pop.
# It is guaranteed that there will be at least one element in the stack before calling pop.


# This problem follows the Top ‘K’ Elements pattern, and shares similarities with Top ‘K’ Frequent Numbers.

# We can use a Max Heap to store the numbers. Instead of comparing the numbers we will compare their frequencies so that the root of the heap is always the most frequently occurring number. There are two issues that need to be resolved though:

# How can we keep track of the frequencies of numbers in the heap? When we are pushing a new number to the Max Heap, we don’t know how many times the number has already appeared in the Max Heap. To resolve this, we will maintain a HashMap to store the current frequency of each number. Thus whenever we push a new number in the heap, we will increment its frequency in the HashMap and when we pop, we will decrement its frequency.
# If two numbers have the same frequency, we will need to return the number which was pushed later while popping. To resolve this, we need to attach a sequence number to every number to know which number came first.
# In short, we will keep three things with every number that we push to the heap:

# 1. number // value of the number
# 2. frequency // frequency of the number when it was pushed to the heap
# 3. sequenceNumber // a sequence number, to know what number came first



from heapq import *

class Element:
    def __init__(self, number, freq, seq_num):
        self.number = number
        self.freq = freq
        self.seq_num = seq_num
    
    def __lt__(self, other):
        # higher frequency wins
        if self.freq != other.freq:
            return self.freq > other.freq
        # if both elements have same frequency, return the element that was pushed later
        return self.seq_num > other.seq_num

class Solution:
    def __init__(self):
        self.seq_num = 0
        self.maxHeap = []
        self.freq_map = {}
    
    def push(self, num):
        self.freq_map[num] = self.freq_map.get(num, 0)+1
        heappush(self.maxHeap, Element(
            num, self.freq_map[num], self.seq_num
        ))
        self.seq_num += 1
    
    def pop(self):
        num = heappop(self.maxHeap).number
        # decrement the frequency or remove if this is the last number
        if self.freq_map[num] > 1:
            self.freq_map[num] -= 1
        else:
            del self.freq_map[num]
        return num


def main():
  sol = Solution()
  sol.push(1)
  sol.push(2)
  sol.push(3)
  sol.push(2)
  sol.push(1)
  sol.push(2)
  sol.push(5)
  print(sol.pop())
  print(sol.pop())
  print(sol.pop())


main()



# Time Complexity
# The time complexity of push() and pop() is O(logN) where ‘N’ is the current number of elements in the heap.

# Space Complexity
# We will need O(N) space for the heap and the map, so the overall space complexity of the algorithm is O(N).