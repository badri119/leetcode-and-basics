# ---------------------------- Arrays and Hashigs ------------------------------

# Leetcode 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# BF Approach (Sorting)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:  # Edge case when length of the array is 1
            return False
        nums.sort()  # Sort array
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:  # check if i is equal to i-1
                return True  # they are the same, so return true
        return False  # return false

# Optimal Approach (Hashset)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashing = set()  # create a hashset
        for i in range(len(nums)):
            if nums[i] in hashing:
                return True
            hashing.add(nums[i])
        return False


# Leetcode 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# BF Approach: O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):  # Traversing through the array
            for j in range(i+1, len(nums)):  # traversing again from i+1
                # checking to see if the sum of the two indices is equal to the target
                if nums[i]+nums[j] == target:
                    return [i, j]  # returning the index

# Optimal Approach:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newmap = {}  # initalize the new map
        for i in range(len(nums)):  # Traverse through the array
            difference = target - nums[i]  # checking to see the difference
            if difference in newmap:  # if the difference exists in the hashmap
                return [newmap[difference], i]  # return the indices
            newmap[nums[i]] = i  # if not, add it to the hashmap
        return


# Leetcode 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# BF Approach O(n logn) + O(n logn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds = sorted(s)
        sortedt = sorted(t)
        if sorteds == sortedt:
            return True
        return False

# Optimal Approach (Hashmap):


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

# Leetcode 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Brute Foce:


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for word in strs:
            # Sort the characters in the word to get a unique key for anagrams
            sorted_word = "".join(sorted(word))

        # If the sorted word is not in the dictionary, add it with an empty list
            if sorted_word not in dicts:
                dicts[sorted_word] = []

        # Append the original word to the anagram group
            dicts[sorted_word].append(word)

    # Convert the dictionary values (anagram groups) to a list
        result = list(dicts.values())

        return result

# Optimal Approach:


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Approach with two arrays:


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # store length of array to n
        # prefix array and multiply with size of the array
        prefix_vals = [1] * n
        # postfix array and multiply with size of the array
        postfix_vals = [1] * n
        result = [1] * n  # result array and multiply with size of the array

        prefix = 1  # initially prefix will be 1
        for i in range(n):  # traverse through the array
            # Store the product of all elements to the left of the current element
            prefix_vals[i] = prefix
        # Update the prefix for the next element
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            # Store the product of all elements to the right of the current element
            postfix_vals[i] = postfix
        # Update the postfix for the next element
            postfix = postfix * nums[i]

        for i in range(n):
            # Calculate the final result by multiplying prefix and postfix
            result[i] = prefix_vals[i] * postfix_vals[i]
        return result

# Approach with 1 array:


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result list with all elements set to 1
        res = [1] * (len(nums))

        # Calculate prefix products
        prefix = 1
        for i in range(len(nums)):
            # Store the product of all elements to the left of the current element
            res[i] = prefix
            # Update the prefix product for the next element
            prefix = prefix * nums[i]

        # Initialize postfix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # Update each result element by multiplying it with the corresponding postfix product
            res[i] = res[i] * postfix
            # Update the postfix product for the next element
            postfix = postfix * nums[i]

        # The result list now contains the product of all elements except self at each index
        return res


# 1572. Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals. (https://leetcode.com/problems/matrix-diagonal-sum/description/)

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
 
class Solution:
    def diagonalSum(self, mat: List[List[int]) -> int:
        # Initialize a variable to store the sum of diagonal elements.
        sum = 0

        # Iterate through the rows of the matrix.
        for i in range(len(mat)):
            # Add the main diagonal element to the sum.
            sum = sum + mat[i][i]

            # Add the anti-diagonal element to the sum (opposite diagonal).
            sum = sum + mat[i][len(mat) - 1 - i]

        # If the matrix size is odd, subtract the value in the center from the sum.
        return sum - (mat[len(mat) // 2][len(mat) // 2] if len(mat) % 2 else 0)

   
# 2133. Check if Every Row and Column Contains All Numbers (https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/)
# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

class Solution:
    def checkValid(self, matrix: List[List[int]) -> bool:
        # Initialize dictionaries to keep track of values in rows and columns.
        row = collections.defaultdict(set)  # Dictionary to track values in each row.
        column = collections.defaultdict(set)  # Dictionary to track values in each column.

        # Iterate through the entire matrix.
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                # Check if the current value is already present in the corresponding row or column.
                if (matrix[r][c] in row[r] or matrix[r][c] in column[c]):
                    return False  # Return False if the value is a duplicate.

                # If the value is not a duplicate, add it to the respective row and column.
                row[r].add(matrix[r][c])  # Add the value to the row.
                column[c].add(matrix[r][c])  # Add the value to the column.

        return True  # If all values pass the uniqueness check, return True (the matrix is valid).



# 36. Valid Sudoku (https://leetcode.com/problems/valid-sudoku/description/)
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]) -> bool:
        # Initialize dictionaries to keep track of values in rows, columns, and 3x3 boxes.
        row = collections.defaultdict(set)  # Dictionary to track values in each row.
        column = collections.defaultdict(set)  # Dictionary to track values in each column.
        box = collections.defaultdict(set)  # Dictionary to track values in each 3x3 box.

        # Iterate through the entire Sudoku board.
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue  # Skip empty cells (denoted by ".").

                # Check if the current value is already present in the corresponding row, column, or box.
                if (board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in box[(r // 3, c // 3)]):
                    return False  # Return False if the value violates Sudoku rules.

                # If the value is not a duplicate, add it to the respective row, column, and box.
                row[r].add(board[r][c])  # Add the value to the row.
                column[c].add(board[r][c])  # Add the value to the column.
                box[(r // 3, c // 3)].add(board[r][c])  # Add the value to the 3x3 box.

        return True  # If all values pass the Sudoku rules, return True (Sudoku is valid).


#Leetcode 128 Longest Consecutive Sequence:
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

#BF Approach:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # Check if the input array is empty
    if not nums:
        return 0
    
    # Sort the input array
    nums.sort()
    
    # Initialize variables to keep track of longest consecutive sequence and current sequence length
    longest = 1  # Initialize the length of the longest consecutive sequence as 1
    current = 1  # Initialize the current sequence length as 1
    
    # Iterate through the sorted array to find the longest consecutive sequence
    for i in range(1, len(nums)):
        # Check if the current number is not equal to the previous number
        if nums[i] != nums[i - 1]:
            # Check if the current number is part of a consecutive sequence
            if nums[i] == nums[i - 1] + 1:
                current += 1  # Increment the current sequence length
            else:
                longest = max(longest, current)  # Update the longest sequence if needed
                current = 1  # Reset the current sequence length
    
    # Return the maximum of longest sequence and current sequence length
    return max(longest, current)
    
#Optimal Approach: 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set from the input list 'nums' to efficiently check for presence of elements
        numSet = set(nums)
        # Initialize a variable to store the length of the longest consecutive sequence found
        longest = 0

        # Iterate through each number in the set
        for n in numSet:
            # Check if it's the potential start of a sequence (i.e., the previous number is not present)
            if (n - 1) not in numSet:
                # Initialize a variable to keep track of the length of the current sequence
                length = 1
                
                # Check for consecutive numbers after the potential start of the sequence
                while (n + length) in numSet:
                    length += 1  # Increment the length as long as consecutive numbers are found
                    
                # Update the 'longest' variable with the maximum sequence length encountered
                longest = max(length, longest)
        
        # Return the length of the longest consecutive sequence found
        return longest


# ---------------------------- Two Pointers ------------------------------

# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

#BF Approach: (Cheating Approach)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "" #removing all alpha numering characters
        for c in s: #traversing through the string
            if c.isalnum(): #converting the string to alpha numerics (basically removing spaces, special characters and colons)
                string += c.lower() #adding it to string variable and converting it to lower case
        return string == string[::-1] #comparing original string with reverse of that string
        
#Optimal Approach:
def isPalindrome(s):
    # Initialize pointers for the start and end of the string
    left, right = 0, len(s) - 1

    # Loop until the pointers meet or cross
    while left < right:
        # Move the left pointer until it points to an alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move the right pointer until it points to an alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters ignoring case after converting them to lowercase
        if s[left].lower() != s[right].lower():
            return False
        
        # Move the pointers to continue checking the string
        left += 1
        right -= 1

    # If the entire string is traversed without any mismatches, it's a palindrome
    return True
    

# 167. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

#BF Approach:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                    
#Optimal Approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize left pointer to the beginning of the list
        left = 0
        # Initialize right pointer to the end of the list
        right = len(numbers) - 1

        # Loop until the pointers meet or cross
        while left < right:
            # Calculate the sum of the elements at pointers' positions
            current_sum = numbers[left] + numbers[right]

            # Check if the current sum is greater than the target
            if current_sum > target:
                # Decrement the right pointer to move towards smaller values
                right -= 1
            # Check if the current sum is less than the target
            elif current_sum < target:
                # Increment the left pointer to move towards larger values
                left += 1
            else:
                # If the current sum equals the target, return the indices
                # (Add 1 to indices as the question expects 1-based index)
                return [left + 1, right + 1]
                

#Leetcode 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

#BF Approach:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []  # Initialize an empty list to store the unique triplets that sum up to zero
        n = len(nums)  # Get the length of the input array

        # Loop through the array to find possible triplets
        for i in range(n - 2):
            # Loop through the array from the element after 'i' up to the second-to-last element
            for j in range(i + 1, n - 1):
                # Loop through the array from the element after 'j' up to the last element
                for k in range(j + 1, n):
                    # Check if the sum of elements at indices i, j, and k equals zero
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Create a sorted triplet from the elements at indices i, j, and k
                        triplets = sorted([nums[i], nums[j], nums[k]])
                        # Check if the sorted triplet is not already in the result list
                        if triplets not in result:
                            # If not present, add the sorted triplet to the result list
                            result.append(triplets)
        return result



#Optimal Approach:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Initialize an empty list to store the unique triplets that sum up to zero
        nums.sort()  # Sort the input array to efficiently find triplets

        for i in range(len(nums)):
            # Skip iterations if the current number is positive
            if nums[i] > 0:
                break

            # Skip duplicate values of 'nums[i]' to avoid redundant calculations
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1  # Set the left pointer to the element after 'i'
            right = len(nums) - 1  # Set the right pointer to the last element

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]  # Calculate the sum of three elements

                if threeSum > 0:
                    right -= 1  # Decrement 'right' if the sum is greater than zero
                elif threeSum < 0:
                    left += 1  # Increment 'left' if the sum is less than zero
                else:
                    res.append([nums[i], nums[left], nums[right]])  # Add the triplet to the result list
                    left += 1  # Move 'left' pointer to the right
                    right -= 1  # Move 'right' pointer to the left

                    # Skip duplicates of 'nums[left]' to avoid redundant solutions
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res  # Return the list of unique triplets that sum up to zero

 
#11. Container With Most Water (https://leetcode.com/problems/container-with-most-water/description/)
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

#BF Approach:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0  # Initialize the variable to store the maximum area found

        # Nested loop to iterate through all possible pairs of walls
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                # Calculate the area between the current pair of walls
                current_area = min(height[i], height[j]) * (j-i)
                
                # Update the maximum area found so far
                max_area = max(max_area, current_area)
        
        return max_area  # Return the maximum area

#Optimal Approach:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the maximum area variable to store the maximum area found
        max_area = 0
        
        # Initialize left pointer to the beginning of the list
        left = 0
        
        # Initialize right pointer to the end of the list
        right = len(height) - 1
        
        # Loop until the left pointer is less than the right pointer
        while left < right:
            # Calculate the current area using the minimum height between the two pointers
            # and the distance between the pointers
            current_area = min(height[left], height[right]) * (right - left)
            
            # Update the maximum area found so far
            max_area = max(max_area, current_area)

            # Move the pointer with the smaller height towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # Return the maximum area found
        return max_area

# 42. Trapping Rain Water (https://leetcode.com/problems/trapping-rain-water/description/)
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.

#O(n) space complexity solution (initializing two extra arrays)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        n = len(height)
        left_max = [0] * n  # Array to store maximum height encountered from the left for each element
        right_max = [0] * n  # Array to store maximum height encountered from the right for each element
        water = 0

        # Compute the maximum height encountered from the left for each element
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Compute the maximum height encountered from the right for each element
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate the trapped water for each position using precomputed left_max and right_max values
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water
        

#O(1) space complexity solution:
class Solution:
    def trap(self, height: List[int]) -> int:
        # Check if the height list is empty
        if not height:  # Equivalent to 'if height == []' or 'if len(height) == 0'
            return 0

        left = 0  # Pointer for the left side
        right = len(height) - 1  # Pointer for the right side
        leftMax = height[left]  # Initialize leftMax with the height of left boundary
        rightMax = height[right]  # Initialize rightMax with the height of right boundary
        water = 0  # Initialize total trapped water

        # Continue until pointers meet
        while left < right:
            # If the left boundary is lower than the right boundary
            if leftMax < rightMax:
                left += 1  # Move the left pointer towards the right
                leftMax = max(leftMax, height[left])  # Update the leftMax if a higher wall is found
                water += leftMax - height[left]  # Add trapped water between the boundaries

            # If the right boundary is lower than or equal to the left boundary
            else:
                right -= 1  # Move the right pointer towards the left
                rightMax = max(rightMax, height[right])  # Update the rightMax if a higher wall is found
                water += rightMax - height[right]  # Add trapped water between the boundaries

        return water  # Return the total trapped water


# ---------------------------- Sliding Window ------------------------------