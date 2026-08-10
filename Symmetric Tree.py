class Solution(object):
    def isSymmetric(self, root):
        def ismirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and ismirror(t1.left, t2.right) and ismirror(t1.right, t2.left))
        return ismirror(root,root)
        