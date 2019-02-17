# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            if i in count.keys():
                count.pop(i)
            else:
                count[i] = 1
        return list(count.keys())[0]

    def singleNumber2(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res
if __name__ == "__main__":
    solu = Solution()
    print(solu.singleNumber([2,2,1]))
    