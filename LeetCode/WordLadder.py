class Solution(object):
    def get_adjacent_elements(self, element, elements_covered, elements_present):
        next_element_list = list(element)
        out = set()
        for i in range(len(next_element_list)):
            next_element_list = list(element)
            for j in range(ord('a'), ord('z') + 1):
                next_element_list[i] = chr(j)
                next_element = "".join(next_element_list)
                if next_element in elements_present and next_element not in elements_covered:
                    out.add(next_element)
        return out

    def bfs(self, source_word, target, word_list):
        elements_covered = {source_word}
        elements_present = set(word_list)
        prev_layer = {source_word}
        next_layer = set()
        parent = {source_word: None}
        target_reached = False
        while len(prev_layer) > 0:
            if target in prev_layer:
                target_reached = True
                break
            for element in prev_layer:
                adjacency_set = self.get_adjacent_elements(element, elements_covered, elements_present)
                for word in adjacency_set:
                    # Elements covered include layer elements (elements of prev layer) and layers before that
                    next_layer.add(word)
                    if word not in parent:
                        parent[word] = []
                    parent[word].append(element)
            elements_covered = elements_covered.union(next_layer)
            prev_layer = next_layer
            next_layer = set()
        if target_reached:
            return parent
        else:
            return None

    def get_all_paths(self, current_word, temp, out, parent_dict):
        if parent_dict[current_word] is None:
            new_list = list(temp)
            new_list.reverse()
            out.append(new_list)
        else:
            for word in parent_dict[current_word]:
                temp.append(word)
                self.get_all_paths(word, temp, out, parent_dict)
                temp.pop()

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        parent_dict = self.bfs(beginWord, endWord, wordList)
        out = []
        if parent_dict is not None:
            temp = [endWord]
            self.get_all_paths(endWord, temp, out, parent_dict)
        return out


if __name__ == '__main__':
    sol = Solution()
    print sol.bfs("hit", 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
