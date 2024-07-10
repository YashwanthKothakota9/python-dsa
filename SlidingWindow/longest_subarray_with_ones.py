def length_longest_subarray_with_ones(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0
    for window_end in range(len(arr)):
        if arr[window_end]==1:
            max_ones_count += 1
        if window_end-window_start+1 - max_ones_count > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    return max_length

def main():
    print("Length of longest substring: "+str(length_longest_subarray_with_ones([0,1,1,0,0,0,1,1,0,1,1],2)))

main()