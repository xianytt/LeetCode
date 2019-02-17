# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def preorderTraversalRec(self, root):
        '''
        前序遍历
        根节点-左节点-右节点
        :return:
        '''
        if root== None:
            return
        print(root.val, end='->')
        self.preorderTraversalRec(root.left)
        self.preorderTraversalRec(root.right)
    def inorderTraversalRec(self, root):
        '''
        中序遍历
        左节点-根节点-右节点
        :return:
        '''
        if root== None:
            return
        self.inorderTraversalRec(root.left)
        print(root.val, end='->')
        self.inorderTraversalRec(root.right)
    def postorderTraversalRec(self, root):
        '''
        中序遍历
        左节点-根节点-右节点
        :return:
        '''
        if root== None:
            return
        self.postorderTraversalRec(root.left)
        self.postorderTraversalRec(root.right)
        print(root.val, end='->')
if __name__ == "__main__":
    tree2 = TreeNode(2)
    tree1 = TreeNode(1)
    tree1.right = tree2
    tree3 = TreeNode(3)
    tree3.left = tree1
    tree4 = TreeNode(4)
    tree3.right = tree4
    solu = Solution()
    print('前序遍历：', end='')
    solu.preorderTraversalRec(tree3)
    print()
    print('中序遍历：', end='')
    solu.inorderTraversalRec(tree3)
    print()
    print('后序遍历：', end='')
    solu.postorderTraversalRec(tree3)