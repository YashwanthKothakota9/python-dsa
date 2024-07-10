def longest_substring_with_no_repeating_chars(str_in):
    window_start = 0
    max_length = 0
    char_index_map = {}
    for window_end in range(len(str_in)):
        print("WE: "+str(window_end))
        right_char = str_in[window_end]
        print("R: "+right_char)
        if right_char in char_index_map:
            window_start = max(window_start,char_index_map[right_char]+1)
            print("WS: "+str(window_start))
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end-window_start+1)
        print("CM: "+str(char_index_map))
        print("ML: "+str(max_length))
    return max_length

def main():
    print("Length of longest substring: "+str(longest_substring_with_no_repeating_chars("aabccbb")))

main()