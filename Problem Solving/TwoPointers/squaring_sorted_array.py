# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]


# approach could be to use two pointers starting at both ends of the input array. At any step, whichever pointer gives us the bigger square, we add it to the result array and move to the next/previous number. Please note that we will be appending the bigger square (as opposed to the previous approach) because the two pointers are moving from larger squares to smaller squares. For that, we will be inserting the squares at the end of the output array.

# Tc: O(N) Sc: O(N)

class Solution:
    def makeSquares(self, arr):
        n = len(arr)
        
        squares = [0 for x in range(n)]
        
        highestSquareIdx = n-1
        
        left, right = 0, n-1
        
        while left < right:
            leftSquare = arr[left] * arr[left]
            rightSquare = arr[right] * arr[right]
            
            if leftSquare > rightSquare:
                squares[highestSquareIdx] = leftSquare
                left += 1
            else:
                squares[highestSquareIdx] = rightSquare
                right -= 1
            
            highestSquareIdx -= 1
        
        return squares


def main():
  sol = Solution()
  # Test the makeSquares method with example inputs
  print("Squares: " + str(sol.makeSquares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(sol.makeSquares([-3, -1, 0, 1, 2])))


main()