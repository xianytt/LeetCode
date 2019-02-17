# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]
if __name__ == "__main__":
    solu = Solution()
    print(solu.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    print(solu.findKthLargest([3,2,1,5,6,4],2))
    