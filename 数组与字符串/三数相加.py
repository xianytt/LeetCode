# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    实现思路：
    将传入的数组进行排序
    遍历一次数组，判断剩余数组中是否存在两个数使之和为0 （遍历是滑去相同的数）判断的时候可以使用二分的思想
    判断结果是否重复

    优化：将情况细化。提取排除特例
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  #存放最终结果
        nums.sort()
        for a in range(len(nums)-2):
            if a==0 or nums[a-1]<nums[a]:   #滑去重复的数值
                left = a+1
                right = len(nums)-1
                while(left<right):
                    sum = nums[a] + nums[left] + nums[right]
                    if sum == 0:  #找到三数和为0
                        result.append([nums[a], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left<right and nums[left-1]==nums[left]:#滑去重复的数值
                            left += 1
                        while left<right and nums[right]==nums[right+1]:
                            right -= 1
                    elif sum < 0:  #若是和小于0则需要加一个更大的数
                        left += 1
                    else:
                        right -= 1
        return result

'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l < 3:
            return []

        nums.sort()

        ret = []
        #三数相同，只能是0
        if nums.count(0) >= 3:
            ret.append([0,0,0])

        #同正、同负，无结果
        if nums[0] >= 0 or nums[-1] <= 0:
            return ret

        #二数相同
        prev = None
        doubles = []
        for x in nums:
            if prev is not None and prev == x and x not in doubles[-1:]:
                doubles.append(x)
            prev = x

        for x in doubles:
            if x == 0:
                continue
            sval = -x*2
            if sval in nums:
                if sval > 0:
                    ret.append([x, x, sval])
                else:
                    ret.append([sval, x, x])

        #各不相同
        nums = list(set(nums))
        nums.sort()
        print nums

        neg_len = abs(nums[0])
        pos_len = abs(nums[-1])
        max_len = max(neg_len, pos_len)+1
        negmaps = [False]*max_len #负数
        posmaps = [False]*max_len #正数
        for x in nums:
            if x < 0:
                negmaps[-x] = True
            elif x > 0:
                posmaps[x] = True

        # 包含0
        if 0 in nums:
            for x in xrange(1, max_len):
                if negmaps[x] and posmaps[x]:
                    ret.append([-x, 0, x])

        # 不包含0
        sep = None
        for i in xrange(len(nums)):
            if nums[i] >= 0:
                sep = i
                break

        # 两负一正
        for i in xrange(sep):
            for j in xrange(sep-1, i, -1):
                sval = -(nums[i]+nums[j])
                if sval > pos_len:
                    break
                if posmaps[sval]:
                    ret.append([nums[i], nums[j], sval])

        # 两正一负
        if nums[sep] == 0:
            sep += 1
        for i in xrange(sep, len(nums)):
            if nums[i]*2 > neg_len:
                break
            for j in xrange(i+1, len(nums)):
                sval = nums[i]+nums[j]
                if sval > neg_len:
                    break
                if negmaps[sval]:
                    ret.append([-sval, nums[i], nums[j]])

        return ret
'''

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([-1, 0, 0, 0]))