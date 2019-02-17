# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。

    思路实现：
    1、判断是否是空字符集
    2、找到字符集中的最短字符串以及判断字符串中是否有空字符串
    3、使用遍历的方法判断是否相等（还有一种使用zip的方法）

'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 0:
            return ""
        #只有一个字符集
        if len(strs) == 1:
            return strs[0]
        min_length = len(strs[0])
        #判断字符集里是否存在空字符并判断字符集中最短字符串长度
        if strs[0] == "":
            return ""
        for str in strs[1:]:
            if len(str) < min_length:
                min_length = len(str)
            if str == "":
                return ""

        #匹配最短公共子序列
        for i in range(min_length):
            target = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != target:
                    if result:
                        return result
                    else:
                        return ""
            else:
                result += target
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["aba","ab"]))

