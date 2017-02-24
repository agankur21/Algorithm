class Solution(object):

    def get_start_index(self, height, start, end, step):
        max_height = 0
        for current_index in range(start, end, step):
            if max_height == 0:
                if height[current_index] <= height[current_index + step]:
                    continue
                else:
                    return current_index
        return end

    def get_maximum_height_index(self, height):
        max_height_index = 0
        for current_index in range(len(height)):
            if height[current_index] > height[max_height_index]:
                max_height_index = current_index
        return max_height_index

    def get_up_slope_volume(self, height, start, end, step):
        max_height_index = start
        volume = 0
        for current_index in range(start, end+step, step):
            if height[current_index] >= height[max_height_index]:
                for limit_iterator in range(max_height_index + step, current_index,step):
                    volume += height[max_height_index] - height[limit_iterator]
                max_height_index = current_index
        return volume

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Get a list of all the maxima

        if len(height) <= 2:
            return 0
        else:
            max_height_index = self.get_maximum_height_index(height)
            start_left = self.get_start_index(height, 0, max_height_index,1)
            start_right = self.get_start_index(height,len(height)-1,max_height_index,-1)
            return self.get_up_slope_volume(height,start_left,max_height_index,1) + self.get_up_slope_volume(height,start_right,max_height_index,-1)



if __name__ == '__main__':
    solution = Solution()
    print solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
