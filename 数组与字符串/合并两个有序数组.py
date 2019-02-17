# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[::]
        nums1.sort()

if __name__ == "__main__":
    solu = Solution()
    print(solu.merge([1,2,4,6,8,0,0,0], 5, [2,5,9], 3))