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
        if arr[i]>largest
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



