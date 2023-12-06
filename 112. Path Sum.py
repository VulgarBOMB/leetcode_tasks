class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.helper(root, targetSum, summ=0)

    def helper(self, root: TreeNode, target: int, summ: int):
        if root is None:
            return False

        summ += root.val
        if root.left is None and root.right is None:
            print(summ)
            if summ == target:
                return True
            else:
                return False
        left_result = self.helper(root.left, target, summ) if root.left is not None else False
        right_result = self.helper(root.right, target, summ) if root.right is not None else False
        return left_result is True or right_result is True


targetSum = 22
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2) # 2
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

a = Solution()
print(a.hasPathSum(root, targetSum))

# def insert_level_order(arr, root, i, n):
#     if i < n:
#         if arr[i] is not None:
#             temp = TreeNode(val=arr[i])
#             root = temp
#
#             root.left = insert_level_order(arr, root.left, 2*i+1, n)
#             root.right = insert_level_order(arr, root.right, 2*i+2, n)
#         else:
#             root = None
#     return root
#
#
# def print_tree(node):
#     if not node:
#         return "None"
#     left_str = print_tree(node.left)
#     right_str = print_tree(node.right)
#     return f"TreeNode{{val: {node.val}, left: {left_str}, right: {right_str}}}"
#
#
# n = len(arr)
# root = insert_level_order(arr, None, 0, n)
# print(print_tree(root))
