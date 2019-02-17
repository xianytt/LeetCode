# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:编写一个函数，其作用是将输入的字符串反转过来。
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def reverserStr(self, s):
        '''
        :param s: str
        :return: str
        '''
        return ''.join(s[i] for i in range(len(s)-1, -1, -1))
if __name__ == "__main__":
    s = Solution()
    print(s.reverseString("A man, a plan, a canal: Panama"))
    print(s.reverserStr('abc djjh'))