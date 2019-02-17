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
    def getNodeNumKthLevelRec(self, root, k):
        '''
        二叉树第K层的节点个数
        如果root为空或者k<1返回0
        如果root不为空而且k==1返回1
        如果root不为空而且k>1返回root左子数的k-1层节点个数加root右子树的k-1层节点个数
        :param root:
        :param k:
        :return:
        '''
        if root == None  or  k < 1:
            return 0
        if root and k==1:
            return 1
        if root and k>1:
            return self.getNodeNumKthLevelRec(root.left, k-1) + self.getNodeNumKthLevelRec(root.right, k-1)
if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree7 = TreeNode(7)
    tree2.left = tree1
    tree3.left = tree2
    tree3.right = tree4
    tree5.left = tree3
    tree5.right = tree6
    tree6.right = tree7
    solu = Solution()
    print(solu.getNodeNumKthLevelRec(tree5,3))
    