# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。



    切片求和
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #nums为空
        if len(nums) == 0:
            return None
        #nums里面只有三个或是以下整数
        sum = 0
        if len(nums) <= 3:
            for i in nums:
                sum += i
            return sum
        nums.sort()
        mint = abs(nums[0]-target) #最接近的值
        t = 0  #最接近Target的数值下标
        second = -1#判断特殊情况，最接近target的数值有两个
        for i in range(1, len(nums)):
            if mint > abs(nums[i]-target):
                mint = abs(nums[i]-target)
                t = i
                continue
            if mint == abs(nums[i]-target) and i != 1:
                if len(nums)-1 != i:
                    if abs(nums[i-2]-target) < abs(nums[i+1]-target):
                        second = i-2
                        three = i
                    else:
                        second = i+1
                        three = i

        #首部
        if t == 0:
            sum = nums[0] + nums[1] + nums[2]
            return sum
        #尾部
        if t == len(nums)-1:
            sum = nums[t] + nums[t-1] + nums[t-2]
            return sum
        if second == -1:
            sum = nums[t-1] + nums[t] + nums[t+1]
            return sum
        else:
            sum = nums[t] + nums[second] + nums[three]
            return sum



if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))  #2
    print(s.threeSumClosest([-4, 4, 6, 8], 0))  #6
    print(s.threeSumClosest([-4, -6], 0))  #-2
    print(s.threeSumClosest([4,5,6,7,8, -8], 4))  #1
    print(s.threeSumClosest([-34, -623, -3, 3, 5], 0))  #5
    print(s.threeSumClosest([0, 2, 1, -3], 1))