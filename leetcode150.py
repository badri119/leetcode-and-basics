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
