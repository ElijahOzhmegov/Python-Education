class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isCousins(root: TreeNode, x: int, y: int) -> bool:
        def find(root_: TreeNode, value: int, k=0):
            if root_ == None: return None
            if root_.val == value: return k

            check_left = find(root_.left, value, k + 1)
            if check_left is not None:
                if type(check_left) is tuple:
                    return check_left
                return check_left, root_.val

            check_right = find(root_.right, value, k + 1)
            if check_right is not None:
                if type(check_right) is tuple:
                    return check_right
                return check_right, root_.val

        x_k = find(root, x)
        y_k = find(root, y)

        if type(x_k) is int:
            x_k = (x_k, None)

        if type(y_k) is int:
            y_k = (y_k, None)

        return x_k[0] == y_k[0] and x_k[1] != y_k[1]


if __name__ == '__main__':
    l = TreeNode(2, TreeNode(4))
    r = TreeNode(3)

    tree = TreeNode(1, l, r)

    assert Solution.isCousins(tree, 4, 3) is False
    assert Solution.isCousins(tree, 2, 3) is False

    r = TreeNode(4, right=TreeNode(5))
    l = TreeNode(3, right=r)
    r = TreeNode(2, left=l)
    tree = TreeNode(1, right=r)

    assert Solution.isCousins(tree, 1, 3) is False
    assert Solution.isCousins(tree, 5, 1) is False

