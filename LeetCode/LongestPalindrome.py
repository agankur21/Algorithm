import numpy as np


def greatest_palindrome_size_odd(s, center):
    right = center + 1
    left = center - 1
    size = 1
    optimum_right = optimum_left = center
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            size += 2
            optimum_left = left
            optimum_right = right
            right += 1
            left -= 1
        else:
            break
    return size, optimum_left, optimum_right


def greatest_palindrome_size_even(s, left, right):
    size = 0
    if left < 0 or right >= len(s) or s[left] != s[right]:
        return size, -1, -1
    else:
        optimum_left = left
        optimum_right = right
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                size += 2
                optimum_left = left
                optimum_right = right
                left -= 1
                right += 1
            else:
                break
        return size, optimum_left, optimum_right


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # A palindrome contains a lot of palindromes : key is centre => with right centre expand both ways
    max_size = 0
    max_right = 0
    max_left = 0
    for i in range(0, len(s)):
        size1, l1, r1 = greatest_palindrome_size_odd(s, i)
        size2, l2, r2 = greatest_palindrome_size_even(s, i, i + 1)
        # Store variables or not
        if max_size >= max(size1, size2):
            continue
        else:
            if size1 > size2:
                max_size = size1
                max_left = l1
                max_right = r1
            else:
                max_size = size2
                max_left = l2
                max_right = r2
    return s[max_left:max_right + 1]


def insert_dummy_characters(s):
    # Objective is to insert # at the starting and between each character of the s
    expanded_s = '#' + "#".join(s) + '#'
    return expanded_s


def filter_dummy_characters(s):
    return filter(lambda x : x != "#",s)

def longestPalindromeManacher(s):
    # There are two variable R and C.. objective is to update them at each iteration
    expanded_string = insert_dummy_characters(s)
    right_limit = current_palindrome_center = 0
    palindrome_length = np.zeros(len(expanded_string),dtype='int32')
    for i in range(len(expanded_string)):
        i_mirror = current_palindrome_center - (i - current_palindrome_center)
        if right_limit > i and i_mirror >= 0:
            palindrome_length[i] = min(palindrome_length[i_mirror], right_limit - i)
        while i + 1 + palindrome_length[i] < len(expanded_string) and i - 1 - palindrome_length[i] >= 0 and \
                        expanded_string[i + 1 + palindrome_length[i]] == expanded_string[i - 1 - palindrome_length[i]]:
            palindrome_length[i] += 1
        # Update the centre and right_limit of there has been limit breached
        if i + palindrome_length[i] > right_limit:
            current_palindrome_center = i
            right_limit = i + palindrome_length[i]
    max_arg = np.argmax(palindrome_length)
    substring=expanded_string[max_arg- palindrome_length[max_arg]:max_arg+ palindrome_length[max_arg]+1]
    return filter_dummy_characters(substring)


if __name__ == '__main__':
    # print longestPalindrome("babad")
    # print longestPalindrome("cbbd")
    print longestPalindromeManacher("babab")
