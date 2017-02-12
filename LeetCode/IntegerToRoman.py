# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Subscribe to see which companies asked this question

class Solution(object):
    """
    Rules:
    no two consecutive odd indexed Roman literal can
    """
    def basic_roman_map(self):
        return [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        basic_roman_map = self.basic_roman_map()
        number = num
        output_list = []
        previous_odd_flag=False
        for i in range(len(basic_roman_map)):
            quotient = number / basic_roman_map[i][0]
            if quotient == 0:
                if previous_odd_flag:
                    previous_odd_flag=False
                continue
            else:
                if i %2 == 1:
                    previous_odd_flag = True
                if quotient == 4 :
                    if previous_odd_flag is False:
                        output_list.append(basic_roman_map[i][1]+ basic_roman_map[i-1][1])
                    else:
                        output_list.append(basic_roman_map[i][1] + basic_roman_map[i - 2][1])
                        previous_odd_flag = False
                else:
                    output_list.append("".join([basic_roman_map[i][1]] * quotient))
                    if i%2 ==0:
                        previous_odd_flag = False
                number = number % basic_roman_map[i][0]
        return "".join(output_list)


if __name__ == '__main__':
    solution = Solution()
    print solution.intToRoman(54)