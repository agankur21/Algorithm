class Solution(object):

    if __name__ == '__main__':
        cache={}

    def check_for_kleene(self, p, current_index):
        if current_index < len(p) - 1 and p[current_index + 1] == '*':
            return True
        else:
            return False

    def recurse_with_memoisation_match(self,s,s_index,p,p_index):
        if (s_index,p_index) in self.cache:
            return self.cache[(s_index,p_index)]
        if s_index >= len(s) and p_index >= len(p):
            self.cache[(s_index, p_index)] =True
        elif s_index < len(s) and p_index >= len(p):
            self.cache[(s_index, p_index)] = False
        else:
            s_char=s[s_index] if s_index < len(s) else ""
            is_kleene= self.check_for_kleene(p,p_index)
            current_match= True if s_char == p[p_index] or (p[p_index]=='.' and s_char != "") else False
            if is_kleene and current_match:
                self.cache[(s_index,p_index)]= self.recurse_with_memoisation_match(s,s_index+1,p,p_index) or self.recurse_with_memoisation_match(s,s_index,p,p_index+2)
            elif is_kleene and not current_match:
                self.cache[(s_index, p_index)]= self.recurse_with_memoisation_match(s,s_index,p,p_index+2)
            elif not is_kleene and current_match:
                self.cache[(s_index, p_index)] = self.recurse_with_memoisation_match(s,s_index+1,p,p_index+1)
            else:
                self.cache[(s_index, p_index)]=False
        return self.cache[(s_index, p_index)]


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.cache={}
        return self.recurse_with_memoisation_match(s,0,p,0)


if __name__ == '__main__':
    solution = Solution()
    print solution.isMatch("ab", ".*..")
