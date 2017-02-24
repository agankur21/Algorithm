class Solution(object):
    """
    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return all possible palindrome partitioning of s.

        For example, given s = "aab",
        Return

        [
          ["aa","b"],
          ["a","a","b"]
        ]
    """

    def is_palindrome(self,str,start,end):
        for i in range(start,(start+end)/2 + 1):
            if str[i] != str[end-i+start]:
                return False
        return True


    def backtrack(self,str,outlist,templist,start):
        if start== len(str):
            outlist.append(list(templist))
        else:
            for i in range(start,len(str)):
                if self.is_palindrome(str,start,i):
                    templist.append(str[start:i+1])
                    self.backtrack(str,outlist,templist,i+1)
                    templist.pop()


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]

        """
        outlist=[]
        templist=[]
        self.backtrack(s,outlist,templist,0)
        return outlist

if __name__ == '__main__':
    solution=Solution()
    print solution.partition("aab")

