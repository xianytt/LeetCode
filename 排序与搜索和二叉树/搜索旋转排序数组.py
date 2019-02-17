# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''


class Solution(object):
    def ss(self, nums, l, r, target):
        if l + 1 < r:  # 保证m的左右都有值
            m = (l + r) // 2
            if nums[l] < nums[m] and nums[m] < nums[r]:
                if target < nums[m]:
                    return self.ss(nums, l, m - 1, target)
                elif target == nums[m]:
                    return m
                else:
                    return self.ss(nums, m + 1, r, target)
            elif nums[m] > nums[l]:
                if target < nums[l] or nums[m] < target:
                    return self.ss(nums, m + 1, r, target)
                elif target == nums[l]:
                    return l
                elif target > nums[l] and target < nums[m]:
                    return self.ss(nums, l, m - 1, target)
                elif target == nums[m]:
                    return m

            else:  # nums[m] < nums[r]
                if target < nums[m] or nums[r] < target:
                    return self.ss(nums, l, m - 1, target)
                elif target == nums[m]:
                    return m
                elif target > nums[m] and target < nums[r]:
                    return self.ss(nums, m + 1, r, target)
                elif target == nums[r]:
                    return r

        else:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        return self.ss(nums, 0, len(nums) - 1, target)

if __name__ == "__main__":
    solu = Solution()
    print(solu.search([7,0,1,2,3,4,5,6], 5))
    print(solu.search([6, 7, 0, 1, 2, 3, 4, 5], 0))
    