# Given an array of points in a 2D plane, find ‘K’ closest points to the origin.

# Example 1:

# Input: points = [[1,2],[1,3]], K = 1
# Output: [[1,2]]
# Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
# The Euclidean distance between (1, 3) and the origin is sqrt(10).
# Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
# Example 2:

# Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
# Output: [[1, 3], [2, -1]]

# The Euclidean distance of a point P(x,y) from the origin can be calculated through the following formula:sqrt(x^2+y^2) 

# This problem follows the Top ‘K’ Numbers pattern. The only difference in this problem is that we need to find the closest point (to the origin) as compared to finding the largest numbers.

# Following a similar approach, we can use a Max Heap to find ‘K’ points closest to the origin. While iterating through all points, if a point (say ‘P’) is closer to the origin than the top point of the max-heap, we will remove that top point from the heap and add ‘P’ to always keep the closest points in the heap.

from heapq import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)

class Solution:
    def findClosestPoints(self, points, k):
        maxHeap = []
        
        for i in range(k):
            heappush(maxHeap, (-points[i].distance_from_origin(), points[i]))
        
        for i in range(k, len(points)):
            distance = points[i].distance_from_origin()
            
            # If the current point is closer to the origin than the farthest point in max-heap, replace it.
            if distance < -maxHeap[0][0]:
                heappop(maxHeap)
                heappush(maxHeap, (-distance, points[i]))
        
        closestPoints = []
        
        # Extract the closest points from the max-heap.
        while maxHeap:
            closestPoints.append(maxHeap[0][1])
            heappop(maxHeap)
        
        return closestPoints
    
    @staticmethod
    def print_point(point):
        print("[" + str(point.x) + ", " + str(point.y) + "] ", end='')

def main():
  sol = Solution()
  result = sol.findClosestPoints([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest to the origin: ", end='')
  for point in result:
    Solution.print_point(point)  # Call the static method correctly


main()


# Time Complexity
# The time complexity of this algorithm is O(N*logK) as we iterating all points and pushing them into the heap.

# Space Complexity
# The space complexity will be O(K) because we need to store ‘K’ point in the heap.