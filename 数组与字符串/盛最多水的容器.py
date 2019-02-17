# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxval = 0
        while i < j:
            maxval = max(maxval, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxval
if __name__ == "__main__":
    solu = Solution()
    