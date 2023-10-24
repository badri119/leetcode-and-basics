# ---------------------------- Arrays and Hashigs ------------------------------

# Question17 Leetcode 217. Contains Duplicate
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
