# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
'''
    在默认的情况下创建多个对象的ID不相同，如果想要设置为单例模式，可以通过__new__()方法中的__instance
'''
'''
    第一种实现单例模式
    1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
    2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
'''

print('---------第一种-------------')
class Single(object):
    __instance=None
    def __new__(cls):
        if cls.__instance==None:
            # 如果__instance为空说明这次是第一次创建实例
            # 通过父类的__new__创建实例
            cls.__instance==object.__new__(cls)
            return cls.__instance
        else:
            #返回上一个对象的引用
            return cls.__instance
a = Single()
b = Single()
print(id(a)==id(b))


'''
    方式二
    共享属性；所属单例就是所有引用（实例、对象）拥有相同的状态和行为
    同一个类的所有实例天然拥有相同的行为
    只需要保证同一个类的所有实例具有相同的状态
    所有实例共享属性的最简单最直接的方法就是__dict__属性属性指向同一个字典（dict）
'''
print('---------第二种-------------')
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__=cls._state
class MyClass2(Borg):
    a = 1
one = MyClass2()
two = MyClass2()
print(id(one)==id(two))



'''
    本质上上算上方式1
    使用元类_metaclass__的高级python用法
'''
print('---------第三种(python2)-------------')
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance


class MyClass3(object):
    __metaclass__ = Singleton2
one = MyClass3()
two = MyClass3()

print(id(one) == id(two))



print('---------第三种(python3)-------------')


class Singleton3(type):
    def __new__(cls, name, bases, attrs):
        attrs["instance"] = None
        return super(Singleton3, cls).__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton3, cls).__call__(*args, **kw)
        return cls.instance


class MyClass4(metaclass=Singleton3):
    pass

one = MyClass4()
two = MyClass4()

print(id(one) == id(two))

'''
    使用高级装饰器
    这是一种更pythonic，更elegant的方法
    单例类本身根本不知道自己是单例的，因为他本身（自己的代码）并不是单例
'''
print('---------第四种-------------')
def singleton(cls):
    instance = {}
    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

one = MyClass4()
two = MyClass4()


print(id(one) == id(two))