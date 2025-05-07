# Problem 1 : Max Consecutive Ones III
# Time Complexity :
'''
Two pointer with left pointer incrementing by one position - O(n) where n is the length of the nums
Two pointer with left pointer moving to next 0th positon - O(2n) where n is the length of the nums
'''
# Space Complexity :
'''
Two pointer with left pointer incrementing by one position - O(1)
Two pointer with left pointer moving to next 0th positon - O(1)
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Your code here along with comments explaining your approach

# Two pointer approacher with left pointer incrementing by one position
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # define variable left which will store starting index of sliding window
        left = 0
        # define count variable which will store the number of zero for the sliding window
        count = 0
        # define maxLength which will store the length of the sliding window
        maxLength = 0
        # loop through nums list
        for right in range(len(nums)):
            # check if the element at right position in nums is 0 and if it is then increment the value of count
            if nums[right] == 0:
                count += 1
            # check if the count is greater than k
            if count > k:
                # if it is then check if the element at left position in nums is 0 and if it is then decrement the value of count
                if nums[left] == 0:
                    count -= 1
                # increment the left
                left += 1
            # get the maximum value between maxLength and (right - left + 1)
            maxLength = max(maxLength, right - left + 1)
        # return maxLength
        return maxLength

# Two pointer approacher with left pointer incrementing till next 0th value
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # define variable left which will store starting index of sliding window
        left = 0
        # define count variable which will store the number of zero for the sliding window
        count = 0
        # define maxLength which will store the length of the sliding window
        maxLength = 0
        # loop through nums list
        for right in range(len(nums)):
            # check if the element at right position in nums is 0 and if it is then increment the value of count
            if nums[right] == 0:
                count += 1
            # check if the count is greater than k
            if count > k:
                # loop till left is less than right and the element at left position in nums is not equal to 0
                while left < right and nums[left] != 0:
                    # if it is then increment the left
                    left += 1
                # increment the left and decrement the count
                left +=1 
                count -= 1
            # get the maximum value between maxLength and (right - left + 1)
            maxLength = max(maxLength, right - left + 1)
        # return maxLength
        return maxLength
