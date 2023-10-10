#Question1: Largest Elevment in an Array
# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the largest element in the array.

#BF Approach:
from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    
    arr.sort()
    return arr[-1]

#Optimal approach:
def largestElement(arr: [], n: int) -> int:
    largest = a[0]
    for i in range(0,n):
        if arr[i]>largest:
        largest = arr[i]
    return largest


#Question2: Find Second Smallest and Second Largest Element in an array
# Example 1:
# Input: [1,2,4,7,7,5]
# Output: Second Smallest : 2
# 	Second Largest : 5
# Explanation: The elements are as follows 1,2,3,5,7,7 
# and hence second largest of these is 5 and second smallest is 2

#BF Approach:
from sys import *
from collections import *
from math import *
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    a.sort()
    return [a[-2],a[1]]

#Optimal Approach:
def secondLargest(n:int,a: [int] ):
    largest = a[0]
    slargest = -1
    for i in range(1,n):
        if (a[i]>largest)
            slargest = largest
            largest = a[i]
        else:
            if (a[i] < largest and a[i] > slargest):
                slargest = a[i]
    return slargest
            
def secondSmallest(n:int,a: [int] ):
    smallest = a[0]
    ssmallest = float('inf')
    for i in range(n):
        if (arr[i] < smallest):
            ssmallest = smallest
            smallest = arr[i]
        elif (arr[i] < ssmallest and arr[i] != smallest):
            ssmallest= arr[i]
    return ssmallest
    
    

def getSecondOrderElements(n: int,  a: [int]) -> [int]:    
#if array size is lesser than 2, return the array
    if (len(arr)<2):
        return 


# Question3 Check if array is sorted:
# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: True.
# Explanation: 
# The given array is sorted i.e Every element in the array is smaller than
# or equals to its next values, So the answer is True.

#Optimal Approach
def isSorted(n: int,  a: [int]) -> int: 
    for i in range(1,n): #Iterating through the array
        if a[i]< a[i-1]: #Checking if array in a specific index is lesser than the previous index array
            return 0 #If it is, return 0 or false
    return 1 #returning 1 as the array is sorted

#Question4 Leetcode 26. Remove Duplicates from Sorted Array
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#Optimal Approach using two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l +=1
        return l

#Question5 Left Rotate an array by one
# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 2,3,4,5,1
# Explanation: 
# Since all the elements in array will be shifted 
# toward left by one so ‘2’ will now become the 
# first index and and ‘1’ which was present at 
# first index will be shifted at last.
def rotateArray(arr: [], n: int) -> []:
    if len(arr) == 0 or len(arr) == 1:
        return arr
    first = a[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[n-1] = first
    return arr
        

#Part2 Right Rotate an array by one:
a = [1,2,3,4,5]
if len(a) == 0 or len(a) == 1:
    print(a)
temp = a[len(a)-1]
for i in range(len(a)-2, -1, -1):
    a[i+1] = a[i]
a[0] = temp
print(a)


#Question6 Leetcode189 Rotate Array to right by k places
# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
        #Creating a function for reverse
        def reverse(self, nums, start, end):
         while (start < end):
            nums[start], nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
            
        def rotate(self, nums: List[int], k: int) -> None:
         k = k % len(nums)
         self.reverse(nums, 0, len(nums) - 1)
         self.reverse(nums, 0, k - 1)
         self.reverse(nums, k, len(nums) - 1)
         
# Rotate Array to left by k places
#Creating a function for reverse
        def reverse(self, nums, start, end):
         while (start < end):
            nums[start], nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        def rotate(self, nums: List[int], k: int) -> None:
         k = k % len(nums)
         self.reverse(nums, 0, k-1)
         self.reverse(nums, k, len(nums) - 1)
         self.reverse(nums, 0, len(nums) - 1)
        
#Question 7 Leetcode 283. Move Zeroes
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

#BF Approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz = [] #Created a empty arrray non-zeros where I'll be storing all the non-zeros from the original array

        for i in range(len(nums)): #looping through the array to find non-zeros
            if nums[i] !=0:
                nz.append(nums[i]) # appending it to the nz array
        for i in range(len(nz)): #looping through the nz array
            nums[i] = nz[i] #adding it back to the orginal array so first few spots will be filled up with non-zeros

        for i in range(len(nz), len(nums)): #looping through the array starting from non zero position till the end of the nums array
            nums[i] = 0 #adding zeros to the end
            
#Optimal Approach - Two pointers
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
        return nums
    
# Question8 Linear Search in an Array
# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
# Example 1:
# Input: arr[]= 1 2 3 4 5, num = 3
# Output: 2
# Explanation: 3 is present in the 2nd index

def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    for i in range(len(arr)): #Iterate through the array
        if arr[i] == num: #Compare to see if num[i] is equal to the target
            return i #return i (index)
    return -1 
    pass

#Question9 Union of two sorted arrays
# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
# The union of two arrays can be defined as the common and distinct elements in the two arrays NOTE: Elements in the union should be in ascending order.

# Example 1:
# Input:
# n = 5,m = 5.
# arr1[] = {1,2,3,4,5}  
# arr2[] = {2,3,4,4,5}
# Output:
#  {1,2,3,4,5}

#BF Approach:
def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    combine = set()
    union =[]


    for i in range(len(a)):
        combine.add(a[i])
    for i in range (len(b)):
        combine.add(b[i])
    
    
    for vals in combine:
     union.append(vals)
    
    union.sort()
    
    return union
    pass

#Question10 Leetcode 268 Missing Number:
#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.

#Optimal Approach:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        lenOfNums = len(nums) #Finding the length of the list nums

        total = (lenOfNums*(lenOfNums+1))//2 #To find the sum of N natural numbers we use: (N*(N+1))/2

        totalSum = sum(nums) #Finding the sum of the nums 

        difference = total - totalSum #Subtracting Total - totalSum to get the difference

        return difference
    
#Question11 Leetcode 485 Max Consecutive ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 #count variable to count the number of 1s, initially setting it to zero
        maximum = 0 #max number of 1s aka the answer

        for i in range(len(nums)): #Traversing through the array
            if nums[i] ==1: #checking to see if index value is equal to 1
                count +=1 #if it is, increase count by 1
            else:
                count = 0 #else reset count back to 0
            maximum = max(maximum, count) #Calculate max 
        return maximum
    
#Question12 Leetcode 136 Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:

# Input: nums = [2,2,1]
# Output: 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0 #set a variable single to return the answer
        for i in range(len(nums)): #traverse through the list
            single = single ^ nums[i] #use XOR method For example, if nums is [2,2,1], XOR for that would be 2^2^1 which is 0^1, 0 XOR any numeber, is the number itself
        return single

         


        
#Question13 Leetcode 1 Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j]==target:
                    return [i,j]
        return []
        

