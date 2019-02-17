# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

    你可以假设数组是非空的，并且给定的数组总是存在众数。
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
        n = len(nums)/2
        for key,value in count.items():
            if value >= n:
                return key

    def majorityElement2(self, nums):
        return sorted(nums)[len(nums) / 2]
if __name__ == "__main__":
    solu = Solution()
    print(solu.majorityElement([3,2,3]))
    print(solu.majorityElement([2,2,1,1,1,2,2]))
    