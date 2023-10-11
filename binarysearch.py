# Basics of Binary Search:
# Binary search is only applicable in a sorted search space. The sorted search space does not necessarily have to be a sorted array.
# It can be anything but the search space must be sorted.
# In binary search, we generally divide the search space into two equal halves and then try to locate which half contains the target.
# According to that, we shrink the search space size.


# Question1 Leetcode 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # using two pointers:

        left = 0  # initilize pointer left at 0th index
        # initilize pointer right at last index of the array
        right = len(nums)-1
        while left <= right:  # if left is lesser than right (which is obvious)
            mid = ((left+right)//2)  # find the mind point of the array
            if nums[mid] == target:  # if the target is at the mid point, return the midpoint
                return mid
            elif target > nums[mid]:  # if target is greater than the midpoint
                left = mid + 1  # move the left pointer to mid pointer + 1 which is one point after the mid value
            else:  # if target is lesser than the midpoint
                # move the right pointer to mid pointer -1 which is one point before the mid value
                right = mid - 1
        return -1  # returning -1 if target is not found


# Question2.1: Implement Lower Bound
# What is Lower Bound?
# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
# The lower bound is the smallest index, ind, where arr[ind] >= x.
# But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

# What is Upper Bound?
# The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.
# The upper bound is the smallest index, ind, where arr[ind] > x.
# But if any such index is not found, the upper bound algorithm returns n i.e. size of the given array.
# The main difference between the lower and upper bound is in the condition.
# For the lower bound the condition was arr[ind] >= x and here, in the case of the upper bound, it is arr[ind] > x.

# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
# Example 1:
# Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
# Result: 1
# Explanation: Index 1 is the smallest index such that arr[1] >= x.

# Example 2:
# Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] >= x.

# 1. BF Approach TC: O(n)
def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(len(arr)):  # Traverse through the array
        if arr[i] >= x:  # Check if the index value is greater than or equal to the value of x
            return i  # return index
    # if x value is greater than the values in the array, return n (length of array)
    return n

# 2. Optimal Approach


def lowerBound(arr: [int], n: int, x: int) -> int:
    left = 0  # pointer at index 0
    right = len(arr) - 1  # pointet at last index
    ans = n  # storing length of the array to ans
    while left <= right:  # this is defnitely true right?
        mid = ((left+right)//2)  # finding mid pointer
        if arr[mid] >= x:  # if mid value is greater than or equal to x
            ans = mid  # possible answer
            right = mid - 1  # reduce right pointer to mid - 1
        else:
            left = mid + 1  # move the left pointer to mid + 1
    return ans  # if out of bounds, return the size of the array which is stored in ans

# Question2.2 Upperbound

# Approach1 BF:
# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.
# Example 1:
# Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
# Result: 3
# Explanation: Index 3 is the smallest index such that arr[3] > x.


def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    for i in range(len(arr)):
        if arr[i] > x:
            return i
    return n
    pass

# Approach2 Optimal:


def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    left = 0
    right = len(arr) - 1
    ans = n
    while left <= right:
        mid = ((left+right)//2)
        if arr[mid] > x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

# Question 3 Leetcode 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        ans = len(nums)

        while left <= right:
            mid = ((left+right)//2)
            if nums[mid] >= target:
                ans = mid

                right = mid - 1
            else:
                left = mid + 1
        return ans
