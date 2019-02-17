# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:反转一个单链表。
'''


class ListNode(object):
    '''
    data:节点保存的数据
    _next:保存下一个节点对象
    '''

    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        '''
        用来定义Node的字符输出
        :return: 数据的data
        '''
        return str(self.data)
        self.next = None
class Operating(object):
    def __init__(self):
        self.head = ListNode
        self.length = 0
    def isEmpty(self):
        # 判断链表是否为空
        return (self.length == 0)

    def append(self, dataOrNode):
        '''
        在末尾添加一个节点
        :param dataOrNode:
        :return:
        '''
        item = None
        # 判断输入值是否是一个节点，如果不是则创建一个节点
        if isinstance(dataOrNode, ListNode):
            item = dataOrNode
        else:
            item = ListNode(dataOrNode)

        # 如果链表为空，则创建一个链表。长度加一
        if self.isEmpty():
            self.head = item
            self.length += 1
            # print('插入成功********')
            return True
        else:
            # 遍历到链表末尾并添加至末尾，长度加一
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1
            # print('插入成功********')
            return True

    def show(self):
        '''
        输出链表
        :return:
        '''
        # 判断链表是否为空
        if self.isEmpty():
            print('链表还是空的哟*******')
        else:
            print('链表输出：', end='')
            node = self.head
            while node:
                print('{}'.format(node.data), end='->')
                node = node.next
            print('NULL')
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 链表为空
        if not head:
            return head
        # #只有一个节点
        # if head.next == None:
        #     return head
        # node = head.next
        # #存放反转的链表头结点
        # reverse_head = None
        # #遍历原链表
        # while node:
        #     if not reverse_head:
        #         reverse_head = node
        #         reverse_head.next = None
        #     else:
        #         new_node = node
        #         new_node.next = reverse_head
        #         reverse_head = new_node
        #     node = node.next
        # return reverse_head
        cur = head
        pre = None
        nxt = head.next
        while nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next
        cur.next = pre
        head = cur
        return head
if __name__ == "__main__":
    o = Operating()
    for i in range(1,6):
        o.append(i)
    o.show()
    solu = Solution()
    print(solu.reverseList(o))