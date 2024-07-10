def find_length(str_in,k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    letter_freq_map = {}
    for window_end in range(len(str_in)):
        print("WE: "+str(window_end))
        right_char = str_in[window_end]
        if right_char not in letter_freq_map:
            letter_freq_map[right_char] = 0
        letter_freq_map[right_char] += 1
        print("Map: "+str(letter_freq_map))
        max_repeat_letter_count = max(max_repeat_letter_count,letter_freq_map[right_char])
        print("MAX_RCount: "+str(max_repeat_letter_count))
        if window_end-window_start+1 - max_repeat_letter_count > k:
            left_char = str_in[window_start]
            letter_freq_map[left_char] -= 1
            window_start += 1
            print("WS: "+str(window_start))
            print("Map: "+str(letter_freq_map))
        max_length = max(max_length, window_end-window_start+1)
        print("ML: "+str(max_length))
        print("--------------------------")
    return max_length

def main():
    print("Length of longest substring after replacement: "+str(find_length("aabccbb",2)))

main()