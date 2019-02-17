# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

        你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''
import time
import copy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]:
                    result.extend([i,j])
                    return result


    def twoSumTest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        r = []
        num_copy = copy.deepcopy(nums)
        nums.sort()
        j = len(nums)-1
        i = 0;
        while i<j:
            if nums[i]+nums[j] > target:
                j -= 1
                continue
            elif nums[i]+nums[j] < target:
                i += 1
                continue
            else:
                a = num_copy.index(nums[i])
                b = num_copy.index(nums[j])
                if nums[i] == nums[j]:
                    num_copy.remove(nums[i])
                    b = num_copy.index(nums[j])
                    b = b+1
                r.extend([a, b])
                return r


if __name__ == "__main__":
    num = Solution()
    print(num.twoSum([2, 7, 11, 15], 9))
    print(num.twoSumTest([-1, -2, -3, -4, -5], -8))