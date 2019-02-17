# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Solution(object):
    #判断字符串是否是回文字符串
    def palindrome(self, s):
        '''
        :type s:str
        :param s:
        :return: Boolean
        '''
        temp = reversed(list(s))  #返回的是迭代器，要显示的话必须List()
        if list(temp) == list(s):
            return True
        else:
            return False
        # print(list(s).reverse())   #列表的翻转没有返回值



if __name__ == "__main__":
    s = Solution()
    print(s.palindrome('bb'))