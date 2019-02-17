# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        # return ' '.join(w[::-1] for w in s.split())
        """
        #判断字符串是否全为空格或是只有一个字符
        if s.isspace() or len(s)==1 or not s:
            return s
        start = 0
        if s[0] == " ":
            target = False
        else:
            target = True
        result = ""
        for i in range(len(s)):
            if s[i] != " " and target:
                continue
            if s[i] == " " and target:
                if start == 0:
                    result += s[i-1::-1]
                else:
                    result += s[i - 1:start-1:-1]
                target = False
            if s[i] != " " and (not target):
                target = True
                start = i
            if s[i] == " " and (not target):
                result += " "
        if target:
            #判断单个单词
            if start == 0:
                return s[::-1]
            result += s[:start-1:-1]
        return result






if __name__ == "__main__":
    solu = Solution()
    print(solu.reverseWords("   m y boo ks         "))
    print(solu.reverseWords("   my books"))
    print(solu.reverseWords("my books  "))
    print(solu.reverseWords("my b ooks  "))
    print(solu.reverseWords("hehhhhhhe"))
    print(solu.reverseWords("a's s'a x's"))
    # st = "abc"
    # result = ""
    # result += st[1]
    # result += st[2]
    # print(result)