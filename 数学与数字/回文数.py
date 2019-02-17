# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数一定不是回文数
        if x < 0:
            return False
        # 个位数
        if x < 10:
            return True
        temp = x
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
            if x == 0:
                break
        return res==temp
if __name__ == "__main__":
    solu = Solution()
    print(solu.isPalindrome(23))
    print(solu.isPalindrome(12121))
    