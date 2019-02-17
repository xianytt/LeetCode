# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if nums == list(set(nums)):
        #     return True
        # return False
        return len(nums)!=len(set(nums))


if __name__ == "__main__":
    solu = Solution()
    print(solu.containsDuplicate([1,1,2]))
    print(solu.containsDuplicate([1,2,3]))
    print(solu.containsDuplicate([3,1]))