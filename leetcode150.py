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
