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
        
#Question14 Leetcode 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

#Approach 1 (Bestapproach)
#This problem is a variation of the popular Dutch National flag algorithm. (I have no idea what this algorithm does)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0 #Create three pointers low mid and high, low starting at 0
        mid = 0 #mid starting at 0
        high = len(nums) - 1 #high starting at the end
# First, we will run a loop that will continue until mid <= high.
# There can be three different values of mid pointer i.e. nums[mid]
# If nums[mid] == 0, we will swap nums[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
# If nums[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
# If nums[mid] == 2, we will swap nums[mid] and nums[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
# In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
# Finally, our array should be sorted.  
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid +=1
            
            elif nums[mid] == 1:
                mid +=1
            
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1

#Approach2 
        cnt0 = 0 #Set three count variables which will count the number of 0s, 1s and 2s
        cnt1 = 0
        cnt2 = 0
        for i in range(len(nums)): #Traverse through the array and increment the count variable if a 0 is spotted
            if nums[i] == 0:
                cnt0 +=1
            elif nums[i] == 1: #Traverse through the array and increment the count variable if a 1 is spotted
                cnt1 +=1
            else:
                cnt2 +=1 #else increment the count 2 variable if a 2 is spotted
        for i in range(cnt0): #Traverse through cnt0 and add it to the original array nums so 0s will be in the beginning of the array
            nums[i] = 0
        for i in range(cnt0, cnt0 + cnt1): #Traverse through cnt1 and add it to the original array nums so 1s will be after 0s
            nums[i] = 1
        for i in range(cnt0 + cnt1, len(nums)): #Traverse through cnt2 and add it to the original array nums so 2s will be after 1s and till the end of the array
            nums[i] = 2

#Qestion15 Leetcode 169. Major Elements
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

#BF Approach TC: O(n^2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        for i in range(len(nums)): #Traverse through the array
            cnt = 0 #keep a count variable
            for j in range(len(nums)): #Traverse again
                if nums[j] == nums[i]: #compare i and j to see if they're the same
                    cnt +=1 #If they are, increment cnt by 1
            
            if cnt > (len(nums)//2): #Check to see if cnt is greater than (length of the array/2)
                return nums[i]
            
#Question16 Leetcode 53 Maximum Subarray
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#Approach1 TC: O(n^2)
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -sys.maxsize - 1 # maximum sum
        for i in range(len(nums)): #Traversing through the array
            sum = 0 #Initializing sum for now which will be 0
            for j in range(i, len(nums)): #Traversing from ith index till the length of the array
                sum += nums[j] #Incrementing sum

                maximum = max(maximum, sum) #Finding maximum subarray
        return maximum
            
    
#Approach2 Kadane's Algorithm which is pretty confusing to understand TC: O(n)
# The intuition of the algorithm is not to consider the subarray as a part of the answer if its sum is less than 0. A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.
# Here, we will iterate the given array with a single loop and while iterating we will add the elements in a sum variable. Now, if at any point the sum becomes less than 0, we will set the sum as 0 as we are not going to consider any subarray with a negative sum. Among all the sums calculated, we will consider the maximum one.
# Thus we can solve this problem with a single loop.

# Approach:
# The steps are as follows:
# We will run a loop(say i) to iterate the given array.
# Now, while iterating we will add the elements to the sum variable and consider the maximum one.
# If at any point the sum becomes negative we will set the sum to 0 as we are not going to consider it as a part of our answer.
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize-1 # maximum sum
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

            if sum>maxi:
                maxi = sum

            if sum<0:  # If sum < 0: discard the sum calculated
                sum = 0 #resetting sum back to 0
                
        return maxi   