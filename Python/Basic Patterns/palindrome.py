# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# https://leetcode.com/problems/palindrome-number/description/
# 9. Palindrome Number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        left = 0
        right = len(x)-1

        while left <= right:
            if x[left] == x[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# BF Approach:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""  # removing all alpha numering characters
        for c in s:  # traversing through the string
            if c.isalnum():  # converting the string to alpha numerics (basically removing spaces, special characters and colons)
                string += c.lower()  # adding it to string variable and converting it to lower case
        # comparing original string with reverse of that string
        return string == string[::-1]

# Optimal Approach:


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for c in s:
            if c.isalnum():
                string += c.lower()
        left = 0
        right = len(string)-1
        while left <= right:
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
