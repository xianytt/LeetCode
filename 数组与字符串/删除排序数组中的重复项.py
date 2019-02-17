# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

实现思路：
首先遍历字符串
将字符串找中的不重复字符一个个嵌入到开头
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)  #len_nums实际字符串的长度, lens删除重复后的长度
        if len_nums <= 1:
            return len_nums
        lens = 1
        target = nums[0]  #标记前一个元素
        for n in range(1,len_nums):
            if target!=nums[n]:
                nums[lens] = nums[n]
                lens += 1
                target = nums[n]
        return lens



if __name__ == "__main__":
    solu = Solution()
    print(solu.removeDuplicates([1,1,2]))   #2
    print(solu.removeDuplicates([1, 1, 2, 2, 3]))
    print(solu.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))   #5
    print(solu.removeDuplicates([1, 4,4,4,4,4, 5,5,5,5,5]))  #3
    print(solu.removeDuplicates([1, 4, 6, 46]))  #4

