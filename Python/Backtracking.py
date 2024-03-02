# Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeros.

def canReahLeaf(root):
    if root is None or root.val == 0:  # if root is empty or root.val is 0  return False
        return False
    # if there are no children, return True as we reached the leaf node
    if root.left is None and root.right is None:
        return True
    if canReachLeaf(root.left):  # recurse in left
        return True
    if canReachLeaf(root.right):  # recurse in right
        return True
    return False


# Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeros. Return the values:

def canReahLeaf(root, path):
    if root is None or root.val == 0:  # if root is empty or root.val is 0  return False
        return False
    path.append(root.val)

    # if there are no children, return True as we reached the leaf node
    if root.left is None and root.right is None:
        return True
    if canReachLeaf(root.left):  # recurse in left
        return True
    if canReachLeaf(root.right):  # recurse in right
        return True
    path.pop()
    return False


# 112. Path Sum using DFS (Recursion)
# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if node is None:
                return False  # if tree is empty return false
            currSum += node.val  # add the current node to currSum
            # if the node doesn't have any childrens return true or false by checking if the currSum == targetSum
            if node.left is None and node.right is None:
                return currSum == targetSum
            return (dfs(node.left, currSum) or
                    # Do a recursion on both left side of the tree and right side of the tree
                    dfs(node.right, currSum))
        return dfs(root, 0)  # return true or false for the tree


# subsets
# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # Create resultant array to store subsets
        subset = []  # Create an array to represent the current subset being constructed

        def helper(i):  # Helper function that takes the index of the nums array
            # If index is equal to the length of nums, we've come to the end of the list
            if i == len(nums):
                # Append a copy of subset to result to avoid modifying subset further
                result.append(subset.copy())
                return

            subset.append(nums[i])  # Include nums[i] in the current subset
            helper(i + 1)  # Recurse to the next number in the array

            subset.pop()  # Exclude nums[i] and backtrack
            helper(i + 1)  # Recurse to continue without nums[i]

        helper(0)  # Call the helper function starting from index 0
        return result  # Return the resultant list of subsets


# Combinations
# https://leetcode.com/problems/combinations/description/

class Solution:
    # Define a class Solution with a method combine that takes integers n and k and returns a list of lists of integers.
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Initialize an empty list to store the final combinations.
        result = []
        # Initialize an empty list to store the current subset being constructed.
        subset = []

        # Define a helper function that takes an integer i as input.
        def helper(i):
            if len(subset) == k:  # If the length of the current subset equals k (target size),
                # add a copy of the subset to the result list.
                return result.append(subset.copy())
            if i > n:  # If i exceeds n, stop the recursion.
                return
            subset.append(i)  # Include the current integer i in the subset.
            # Recursively call the helper function with the next integer.
            helper(i+1)
            subset.pop()  # Backtrack: remove the last element from the subset.
            # Recursively call the helper function with the next integer without including i.
            helper(i+1)

        helper(1)  # Start the recursive process with the first integer.
        return result  # Return the final list of combinations.


# Combination Sum
# https://leetcode.com/problems/combination-sum/description/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the final combinations.
        result = []
        # Initialize an empty list to store the current subset being constructed.
        subset = []

        def helper(i, total):
            # Define a helper function that takes three arguments:
            # i: current index of the candidate list,
            # total: sum of elements in the current subset,

            if total == target:  # If the total sum equals the target,
                # add a copy of the subset to the result list.
                return result.append(subset.copy())

            if i == len(candidates) or total > target:
                # If we've reached the end of the candidates list or the total sum exceeds the target,
                return  # stop the recursion.

            # Include the current candidate element in the subset.
            subset.append(candidates[i])
            helper(i, total + candidates[i])
            # Recursively call the helper function with updated total and the same index.

            subset.pop()  # Backtrack: remove the last element from the subset.

            helper(i+1, total)
            # Recursively call the helper function with the next index and the same total.

        # Start the recursive process with index 0 and total 0.
        helper(0, 0)
        return result  # Return the final list of combinations.

# Subsets II
# https://leetcode.com/problems/subsets-ii/


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []  # Initialize an empty list to store the final subsets.
        # Initialize an empty list to store the current subset being constructed.
        subset = []
        # Sort the input list to handle duplicate elements properly.
        nums.sort()

        def helper(i):
            # Define a helper function that takes an index i as input.

            if i == len(nums):
                # If we've reached the end of the nums list,
                return result.append(subset.copy())
                # add a copy of the current subset to the result list.

            subset.append(nums[i])  # Include the current number in the subset.
            # Include the current number and move to the next index.
            helper(i + 1)

            subset.pop()  # Backtrack: remove the last element from the subset.

            # Skip duplicate elements to avoid generating duplicate subsets.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude the current number and move to the next index.
            helper(i + 1)

        helper(0)  # Start the recursive process with index 0.
        return result  # Return the final list of subsets.


# Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        candidates.sort()

        def helper(i, total):
            if total == target:
                return result.append(curr.copy())
            if i == len(candidates) or total > target:
                return
            curr.append(candidates[i])
            helper(i+1, total + candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, total)
        helper(0, 0)
        return result

# 79. Word Search
# https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the number of rows and columns in the board
        ROWS = len(board)
        COLS = len(board[0])

        # Initialize a set to keep track of visited cells
        seen = set()

        # Helper function to perform DFS search
        def helper(r, c, i):
            # If the entire word is found, return True
            if i == len(word):
                return True
            # Conditions for terminating the search:
            # 1. Out of bounds
            # 2. Current cell does not match the character in the word
            # 3. Current cell has been visited before
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                    board[r][c] != word[i] or (r, c) in seen):
                return False

            # Mark the current cell as visited
            seen.add((r, c))

            # Recursively search in all four directions
            result = (helper(r + 1, c, i + 1) or
                      helper(r - 1, c, i + 1) or
                      helper(r, c + 1, i + 1) or
                      helper(r, c - 1, i + 1))

            # Remove the current cell from the set of visited cells
            seen.remove((r, c))

            return result

        # Iterate through all cells in the board
        for r in range(ROWS):
            for c in range(COLS):
                # If the word is found starting from the current cell, return True
                if helper(r, c, 0):
                    return True

        # If the word is not found starting from any cell, return False
        return False


# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []  # List to store the final result
        curr = []    # List to store the current partition

        # Function to check if a substring is a palindrome
        def isPali(s, l, r):
            while l <= r:
                if s[l] != s[r]:  # If characters don't match, it's not a palindrome
                    return False
                l += 1           # Move left pointer to the right
                r -= 1           # Move right pointer to the left
            return True         # If the loop completes, substring is a palindrome

        # Recursive function to generate partitions
        def helper(i):
            # If we've processed the entire string, add current partition to result
            if i == len(s):
                return result.append(curr.copy())
            # Iterate over all possible partitions starting from index i
            for j in range(i, len(s)):
                # If the substring s[i:j+1] is a palindrome
                if isPali(s, i, j):
                    curr.append(s[i:j+1])  # Add it to the current partition
                    helper(j + 1)         # Recur with the next index
                    curr.pop()            # Backtrack by removing the last added element
        # Start the recursive process from index 0
        helper(0)
        # Return the final result
        return result

# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []  # List to store the final combinations
        # Mapping of digits to corresponding letters
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Recursive function to generate combinations
        def helper(i, curr):
            if i == len(digits):  # If we've processed all digits
                # Add the current combination to result
                return result.append(curr)
            # Iterate over letters corresponding to the current digit
            for c in mapping[digits[i]]:
                # Recur with the next digit and updated combination
                helper(i + 1, curr + c)

        # Check if the input string is not empty
        if digits:
            # Start the recursive process with index 0 and an empty string
            helper(0, "")
        return result  # Return the final list of combinations
