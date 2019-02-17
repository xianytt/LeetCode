# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left=[1 for i in range(n)]
        right=[1 for i in range(n)]
        k=1
        for i in range(n):
            left[i]=k
            k*=nums[i]
        print(left)
        k=1
        for i in range(n-1,-1,-1):
            right[i]=k
            k*=nums[i]
        print(right)
        for i in range(0,n):
            left[i]*=right[i]
        return left
if __name__ == "__main__":
    solu = Solution()
    print(solu.productExceptSelf([1,2,3,4]))
    