# 2540. Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2024-03-09

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0  # initalized two pointers
        j = 0
        while i < len(nums1) and j < len(nums2):  # looping till the end
            if nums1[i] == nums2[j]:  # if nums are equal
                return nums1[i]  # return either nums1 or nums 2
            # if nums1 [i] is lesser than nums2[j], increasement to next value
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1  # elese increment j to next value
        return -1  # if there are no common values, return -1
