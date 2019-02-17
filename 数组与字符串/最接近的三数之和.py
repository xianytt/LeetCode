# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        """
        n = len(nums)
        nums.sort()
        if n==0:
            return None
        if n <= 3:
            return sum(nums)
        if  sum(nums[:3]) > target:
            return sum(nums[:3])
        if sum(nums[-3:]) < target:
            return sum(nums[-3:])
        result = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            left, right = i+1, n-1
            while left<right:
                sumthree = nums[i] + nums[left] + nums[right]  #记住当前最小的
                if sumthree == target:
                    return sumthree   #因为答案唯一
                if abs(sumthree-target) < abs(result-target):
                    result = sumthree
                if sumthree < target:
                    left += 1
                elif sumthree > target:
                    right -= 1
        return result

if __name__ == "__main__":
    solu = Solution()
    print(solu.threeSumClosest([-1, 0, 3, 6, -1], 4))  #4
    print(solu.threeSumClosest([-1, 0, 1, 2, -1, -4], 4))  #3
    print(solu.threeSumClosest([-1, 2, 1, -4], 1))   #2
    # info = [12,4,5,6,3,6,3]
    # print(sum(info[:2]))