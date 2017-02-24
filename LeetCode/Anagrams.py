def add_str( anagram_dict, str):
    sorted_str = "".join(sorted(str))
    if sorted_str in anagram_dict:
        anagram_dict[sorted_str].append(str)
    else:
        anagram_dict[sorted_str] = [str]


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagram_dict = {}
    for str in strs:
        add_str(anagram_dict, str)
    return anagram_dict.values()


if __name__ == '__main__':
    print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])