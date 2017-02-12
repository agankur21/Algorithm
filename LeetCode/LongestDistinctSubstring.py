def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_substr_length = 0
    char_set = {}
    window_start = 0
    for char_index in range(len(s)):
        char = s[char_index]
        if char not in char_set or char_set[char] < window_start:
            char_set[char] = char_index
            max_substr_length = (char_index + 1 - window_start) if max_substr_length < (char_index + 1 - window_start) else max_substr_length
        else:
            window_start = char_set[char] + 1
            char_set[char] = char_index
    return max_substr_length


print lengthOfLongestSubstring("abcabcbb")