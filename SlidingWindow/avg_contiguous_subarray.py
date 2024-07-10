def find_average_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            result.append(windowSum/K)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result

def main():
    result = find_average_of_subarrays(5,[1,3,2,6,-1,4,1,8,2])
    print("Average of sub arrays of size k: ", result)

main()