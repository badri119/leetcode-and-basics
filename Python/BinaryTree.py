# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:  # or root is None or if not root
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        # or:
        # root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result
        res = []

        # Define a helper function for inorder traversal
        def helper(root):
            # Base case: If the current node is None, return to the caller
            if root is None:
                return

            # Traverse the left subtree recursively
            helper(root.left)

            # Append the value of the current node to the result list
            res.append(root.val)

            # Traverse the right subtree recursively
            helper(root.right)

        # Call the helper function with the root of the tree to start traversal
        helper(root)

        # Return the final result after the traversal is complete
        return res


# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root):
            if root is None:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res


# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root):
            if root is None:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res


# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize an empty list to store the final result.
        result = []

        # Create a deque (double-ended queue) to facilitate the breadth-first traversal of the binary tree.
        queue = deque()

        # Check if the root node exists.
        if root:
            # If the root exists, append it to the queue.
            queue.append(root)

        # Continue the process until the queue is empty.
        while queue:
            # Initialize an empty list to store the values at the current level.
            value = []

            # Iterate through all the nodes at the current level.
            for i in range(len(queue)):
                # Remove the leftmost node from the queue.
                node = queue.popleft()

                # Append the value of the current node to the 'value' list.
                value.append(node.val)

                # If the left child of the current node exists, add it to the queue.
                if node.left:
                    queue.append(node.left)

                # If the right child of the current node exists, add it to the queue.
                if node.right:
                    queue.append(node.right)

            # Append the 'value' list containing the values at the current level to the 'result' list.
            result.append(value)

        # Return the final result, which is a list of lists representing the values at each level of the binary tree.
        return result


# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            value = []

            for i in range(len(queue)):
                node = queue.popleft()
                value.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(value)
        # similar to previous question but in the final resultant array, reverse the array.
        return result[::-1]


# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        if root:
            queue.append(root)

        while queue:
            val = []

            for i in range(len(queue)):
                node = queue.popleft()
                val.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(res) % 2 == 1:
                val = val[::-1]

            res.append(val)

        return res


# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        queue = deque()

        if root:
            queue.append(root)

        count = 0

        while queue:
            for i in range(len(queue)):
                count += 1
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count


# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:  # if both are empty return True
            return True
        if p is None or q is None:  # if either one is empty return False
            return False
        if p and q and p.val == q.val:  # recursively call if p and q have values and p.val==q.val
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determines if 'subRoot' is a subtree of 'root'.

        Parameters:
        - root: The root of the main tree.
        - subRoot: The root of the potential subtree.

        Returns:
        - bool: True if 'subRoot' is a subtree of 'root', False otherwise.
        """
        # If 'subRoot' is None, it is considered a subtree of any tree.
        if subRoot is None:
            return True
        # If 'root' is None and 'subRoot' is not, 'subRoot' cannot be a subtree.
        if root is None:
            return False

        # Check if the current 'subRoot' is the same as the current 'root'.
        if self.sameTree(root, subRoot):
            return True

        # Recursively check in the left and right subtrees.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        """
        Checks if two trees are identical.

        Parameters:
        - root: The root of the first tree.
        - subRoot: The root of the second tree.

        Returns:
        - bool: True if the trees are identical, False otherwise.
        """
        # If both nodes are None, they are considered identical.
        if root is None and subRoot is None:
            return True
        # if eiter of them is None
        if root is None or subRoot is None:
            return False
        # If both nodes exist and have the same value, check their left and right subtrees.
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        # Nodes are not identical.


# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr is not None:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr

# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Recursion
        # Creating helper function where left is the left boundary and right is the right boundary
        def valid(node, left, right):
            if node is None:  # if node(tree) is empty, return true
                return True
            # comparing node.val to left and right boundary where val should be greater than left and lesser than right
            if not (node.val > left and node.val < right):
                return False
            # for node.left: two boundaries are, the left regular boundary and the right boundary is the node.val
            # for node.right, the left boudary is node.val and right boundary is right
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        # call the helper function and add the boundaries which are negative infinity and positive infinity
        return valid(root, float("-inf"), float("inf"))


# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Guessing this is the BF approach using BFS
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        vals = []

        if root:
            queue.append(root)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        vals.sort()
        # trick here, since the array is sorted, I am using the value K and subtracting -1 from the array so I'll get the index of the value
        return vals[k-1]


# Using Inorder Traversal
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def helper(root):
            if root is None:
                return
            helper(root.left)

            result.append(root.val)

            helper(root.right)
        helper(root)
        return result[k-1]
