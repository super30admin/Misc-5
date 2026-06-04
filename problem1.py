# problem 1 

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr_max = 0 
        left_ptr= 0
        # get first_max
        for right in range(len(nums)):
            if nums[right] == 0:
                k = k-1
            while(k<0):
                if nums[left_ptr] == 0:
                    k = k+1
                left_ptr += 1
            curr_max = max(curr_max,right-left_ptr+1)
        return curr_max
