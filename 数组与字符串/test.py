#encoding = 'utf-8'
'''
    @author:xianyt
    @date:2018/
    @func:
'''
# import Pillow

if __name__ == "__main__":
    # class A(object):
    #     pass
    #
    #
    # class B(A):
    #     pass
    #
    #
    # b = B()
    # print(isinstance(B, A))
    # l = ['a']
    # l.append(['b', 'c'])
    # print(l)
    # dict2 = {[1,2]:'a'}

    # nums = set([1,2,3,4])
    # print(len(nums))
    n = int(input())
    s = 0
    for i in range(1,n+1):
        s += i * i
    print(s)