# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
import copy
if __name__ == "__main__":
    a = [1,2,3,[4,5]]

    b = a #赋值，传对象的引用
    c = copy.copy(a)  #对象拷贝，浅拷贝
    d = copy.deepcopy(a)     #对象拷贝，深拷贝

    a.append(5)   #修改a的对象的时候，b也会随之发生变化
    a[3].append(6)   #浅拷贝会受到影响

    print(a)
    print('--------')
    print(b)
    print('--------')
    print(c)
    print('--------')
    print(d)