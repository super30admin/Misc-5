#using sliding window to calculate biggest possible window, and moving the window till the end
#time:O(n)
#space:O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n= len(nums)
        left=0
        for i in range(n):
            if nums[i]==0:
                k-=1
            if k<0:
                if nums[left]==0:
                    k+=1
                left+=1 
        return i-left+1
        
