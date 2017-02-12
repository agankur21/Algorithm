# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):

    def generate_valid_parenthesis(self,value,positive_left,negative_left,str,out):
        if positive_left == 0 and negative_left ==0:
            out.append(str)
        elif value < 0:
            return None
        else:
            if positive_left > 0:
                self.generate_valid_parenthesis(value + 1, positive_left - 1, negative_left, str + "(", out)
            if negative_left > 0 and value > 0:
                self.generate_valid_parenthesis(value-1,positive_left,negative_left-1,str+")",out)




    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #We have n opening braces and n closing braces...
        #Objective is to decide which sequence work
        out=[]
        self.generate_valid_parenthesis(0,n,n,"",out)
        return out


if __name__ == '__main__':
    solution = Solution()
    print solution.generateParenthesis(3)