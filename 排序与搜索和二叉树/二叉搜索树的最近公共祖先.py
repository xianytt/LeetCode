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

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return

        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
    def lowestCommonAncestor2(self, root, p, q):
        if root.val > max(q.val, p.val):
            self.lowestCommonAncestor2(root.left, p, q)
        elif root.val < min(q.val, p.val):
            self.lowestCommonAncestor2(root.right, p, q)
        else:
            return root
if __name__ == "__main__":
    tree2 = TreeNode(2)
    tree1 = TreeNode(1)
    tree1.right = tree2
    tree3 = TreeNode(3)
    tree3.left = tree1
    tree4 = TreeNode(4)
    tree3.right = tree4
    solu = Solution()
    print(solu.lowestCommonAncestor(tree3, 1, 2))
    