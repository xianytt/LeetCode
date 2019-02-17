# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Node(object):
    '''
    data:节点保存的数据
    _next:保存下一个节点对象
    '''
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext
    def __repr__(self):
        '''
        用来定义Node的字符输出
        :return: 数据的data
        '''
        return str(self.data)
class Operating(object):
    def __init__(self):
        self.head = None
        self.length = 0
    def isEmpty(self):
        #判断链表是否为空
        return (self.length == 0)
    def append(self, dataOrNode):
        '''
        在末尾添加一个节点
        :param dataOrNode:
        :return:
        '''
        item = None
        #判断输入值是否是一个节点，如果不是则创建一个节点
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        #如果链表为空，则创建一个链表。长度加一
        if self.isEmpty():
            self.head = item
            self.length += 1
            print('插入成功********')
            return True
        else:
            #遍历到链表末尾并添加至末尾，长度加一
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1
            print('插入成功********')
            return True
    def addIndex(self, dataOrNode, index):
        '''
        在指定位置上添加节点
        :param dataOrNode:
        :param index:
        :return:
        '''
        # 判断数值不是节点,则创建节点
        if not isinstance(dataOrNode, Node):
            items = Node(dataOrNode)
        #判断链表是否存在或是指定位置大于链表长度
        if self.isEmpty() or index>=self.length:
            self.append(items)
            return True
        else:
            node = self.head
            #判断是否是插入一个头结点
            if index == 0:
                items._next = node
                self.head = items
                self.length += 1
                print('插入成功********')
                return True
            i = 0
            #找到指定位置
            while i<index:
                node = node._next
                i += 1
            #添加节点
            items._next = node._next
            node._next = items
            self.length += 1
            print('插入成功********')
            return True


    def delete(self, dataOrNode):
        '''
        删除指定节点
        :param dataOrNode:
        :return:
        '''
        #判断链表是否存在
        if self.isEmpty():
            return False
        #判断是否是节点
        if isinstance(dataOrNode, Node):
            #取出数值
            dataOrNode = dataOrNode.data
        #假如链表为空而且头节点就找到了,直接将链表设置为空
        if self.length == 1 and self.head.data == dataOrNode:
            self.head = None
            self.length = 0
            print('删除节点成功********')
            return True
        node = pre = self.head
        #头结点就找到了
        if node.data == dataOrNode:
            self.head = node._next
            self.length -= 1
            print('删除节点成功*******')
            return True
        while node:
            #找到需要删除的节点
            if dataOrNode == node.data:
                pre._next = node._next
                self.length -= 1
                print('删除节点成功********')
                return True
            pre = node
            node = node._next
        else:
            print('没有找到该节点')
            return False

    def update(self, dataOrNode, index):
        '''
        修改指定位置的数值
        :param dataOrNode:
        :param index:
        :return:
        '''
        #链表不存在或是输入位置不合理
        if self.isEmpty():
            print('链表不存在')
            return False
        if index>self.length or index<0:
            print('输入位置不合理')
            return False
        #判断输入数值是否是节点，取出数值
        if isinstance(dataOrNode, Node):
            dataOrNode = dataOrNode.data
        node = self.head
        i = 0
        while node:
            #修改数值
            if i == index:
                node.data = dataOrNode
                print('修改节点成功*********')
                return True
            i += 1
            node = node._next

    def find(self, dataOrNode):
        '''
        查找指定节点的数据
        :param dataOrNode:
        :return: 返回空或者位置
        '''
        index = 0
        #判断链表是否为空
        if self.isEmpty():
            print('链表为空**************')
            return False
        node = self.head
        # 判断是否是节点
        if isinstance(dataOrNode, Node):
            # 遍历查询
            while node:
                # 判断是否找到
                if node.data == dataOrNode.data:
                    print('数值处于链表{}*************'.format(index))
                    return index
                index += 1
                node = node._next
            else:
                #遍历完成都没有找到
                print('没有找到该节点**************')
                return False
        #不是节点
        else:
            while node:
                if dataOrNode == node.data:
                    print('数值处于链表{}位置*************'.format(index))
                    return index
                node = node._next
                index += 1
            else:
                # 遍历完成都没有找到
                print('没有找到该节点**************')
                return False

    def show(self):
        '''
        输出链表
        :return:
        '''
        #判断链表是否为空
        if self.isEmpty():
            print('链表还是空的哟*******')
        else:
            print('链表输出：',end='')
            node = self.head
            while node:
                print('{}'.format(node.data), end='-')
                node = node._next
            print()

    def clear(self):
        '''
        清除链表
        :return:
        '''
        self.head = None
        self.length = 0

if __name__ == "__main__":
    o = Operating()
    while True:
        print('链表基本操作(0:输出链表,1:添加节点，2：添加指定位置节点，3：删除节点，4：修改节点，5：查找下标位置, 其他数值:退出程序)')
        i = int(input('请输入相应操作:'))
        if i == 0:
            o.show()
        elif i == 1:
            try:
                data = int(input('请输入节点数值:'))
            except:
                print('请输入数值:')
            else:
                o.append(data)
        elif i == 2:
            try:
                data = int(input('请输入节点数值:'))
                index = int(input('请输入指定位置:'))
            except:
                print('请输入数值')
            else:
                o.addIndex(data, index)
        elif i == 3:
            try:
                data = int(input('请输入需要删除的节点数值:'))
            except:
                print('请输入数值')
            else:
                o.delete(data)
        elif i == 4:
            try:
                index = int(input('请输入需要修改的指定位置:'))
                data = int(input('请输入需要修改的数值:'))
            except:
                print('请输入数值:')
            else:
                o.update(data, index)
        elif i == 5:
            try:
                data = int(input('请输入查找节点数值:'))
            except:
                print('请输入数值:')
            else:
                o.find(data)
        else:
            o.clear()
            break




