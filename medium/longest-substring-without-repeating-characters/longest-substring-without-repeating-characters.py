def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2:
        return 1
    char_map = {}
    left_pointer = 0
    right_pointer = 0
    s_length = len(s)
    max_length = 0

    while(left_pointer < s_length and right_pointer < s_length):
        cur_value = s[right_pointer]
        if s[right_pointer] in char_map.keys():
            left_pointer = max(left_pointer, (char_map[cur_value] + 1))

        char_map[cur_value] = right_pointer
        max_length = max(max_length, (right_pointer - left_pointer) + 1)
        right_pointer += 1

    return max_length


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
