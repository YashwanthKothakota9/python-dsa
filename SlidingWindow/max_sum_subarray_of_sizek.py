def max_sub_array_of_size_k(k, arr):
    maxSum, windowSum = 0, 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            maxSum = max(maxSum,windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum

def main():
    print("Maximum sum of subarray of size k: "+ str(max_sub_array_of_size_k(3,[2,1,5,1,3,2])))

main()
