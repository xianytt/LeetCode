# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''
'''
实现思路：
1）去除所有的空白字符串
2）遍历字符串
    2.1）左括号全都入栈
    2.2）遇到右括号就出栈，然后匹配是否合适
3)成功遍历则返回True
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #创建一个空栈
        s = "".join(s.split())
        #s里面没有括号
        if not s:
            return True

        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif i==')' or i==']' or i=='}':
                if not stack:  #栈中没有左元素
                    return False
                left_ele = stack.pop()
                if i==')':
                    if left_ele != '(':
                        return False
                elif i==']':
                    if left_ele != '[':
                        return False
                elif i=='}':
                    if left_ele != '{':
                        return False
            else:
                return False
        if not stack:
            return True
        else:
            return False

if __name__ == "__main__":
    solu = Solution()
    print(solu.isValid("()"))
    print(solu.isValid("()[]{}"))
    print(solu.isValid("(]"))
    print(solu.isValid("([)]"))
    print(solu.isValid("{[]}"))
    print(solu.isValid('(     )    {}'))
    print(solu.isValid(""))
    print(solu.isValid('[((('))
    print(solu.isValid(')))(('))

