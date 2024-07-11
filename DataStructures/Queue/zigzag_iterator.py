# Given two 1d vectors, implement an iterator to return their elements alternately.

# For example, given two 1d vectors:

# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next() repeatedly until hasNext() returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

# i = ZigzagIterator([1, 2, 3, 4], [5, 6])
# print(i.next())  # returns 1
# print(i.next())  # returns 5
# print(i.next())  # returns 2
# print(i.next())  # returns 6
# print(i.next())  # returns 3
# print(i.next())  # returns 4
# print(i.hasNext())  # returns False


from collections import deque

class Solution:
    def __init__(self,v1,v2) -> None:
        self.queue = deque([(len(v),iter(v)) for v in (v1,v2) if v])
    def next(self):
        length, iter = self.queue.popleft()
        value = next(iter)
        if length > 1:
            self.queue.append((length-1, iter))
        return value
    def hasNext(self):
        return bool(self.queue)
    

def main():
    i = Solution([1, 2, 8, 9, 0], [3, 4, 5, 6])
    while i.hasNext():
        print(i.next()) 

main()
