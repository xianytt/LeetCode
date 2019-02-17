# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''

if __name__ == "__main__":
    s = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    result = []
    for i in range(0,len(s)-1):
        for j in range(1, len(s)):
            result.append(s[i]+s[j])
    print(result)