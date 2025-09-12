from typing import List
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left = 0
#         zeros = 0
#         max_len = 0

#         for right in range(len(nums)):
#             if nums[right] == 0:
#                 zeros += 1

#             while zeros > k:
#                 if nums[left] == 0:
#                     zeros -= 1
#                 left += 1

#             max_len = max(max_len, right - left + 1)

#         return max_len

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        slow = 0
        maxval = 0
        for i in range(n):
            if nums[i] == 0:
                k-=1
            if k<0:
                while nums[slow]!=0:
                    slow+=1
                slow+=1
                k+=1
            maxval = max(maxval,i-slow+1)
        return maxval
        