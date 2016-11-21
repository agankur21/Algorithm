import sys
import os

# Complete the function below.
cache={}
def ispalindrome(str):
    if str in cache:
        return cache[str]
    else:
        if len(str)==0 :
            return 1
        elif len(str)==1:
            cache[str]=1
        else:
            if (str[0] == str[-1]) and (ispalindrome(str[1:len(str)-1]) == 1):
                cache[str] = 1
                return 1
            else:
                return 0

def palindrome( str):
    #Substring size varies from 1 to len(str)
    for substr_size in range(1,len(str)+1):
        for start_index in range(0,len(str)-substr_size +1):
            sub_str=str[start_index:start_index + substr_size]
            if sub_str not in cache:
                ispalindrome(sub_str)
    values=cache.values()
    return sum([v for v in values if v is not None])



if __name__ == '__main__':
    print palindrome("malayalam")