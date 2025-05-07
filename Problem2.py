# Problem 2 : Remove All Adjacent Duplicates in String II
# Time Complexity : O(n) where n is the length of the s string 
# Space Complexity : O(n) where n is the length of the s string 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None

# Your code here along with comments explaining your approach

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # definc stack which store the character from string and countStack which will store the frequency of the character in the string
        stack = []
        countStack = []

        # loop through each character in string
        for c in s:
            # check if stack is empty or the top element of the stack is not equal to character c
            if not stack or stack[-1] != c:
                # if it is then append the character c to stack and append 1 to countStack
                stack.append(c)
                countStack.append(1)
            else:
                # else pop the top count value from countStack and add 1 to it
                newCount = countStack.pop() + 1
                # check if the new count is equal to k and if it is then pop the character from the stack
                if newCount == k:
                    stack.pop()
                else:
                    # else append the newCount to the countStack
                    countStack.append(newCount)
        # define result variable which will store the characters of the result string
        result = []
        # loop through the stack
        while stack:
            # pop the top character and count from the stack and countStack respectively
            ch = stack.pop()
            cnt = countStack.pop()
            # append the cnt times character to the result array
            result.extend([ch] * cnt)
        # convert the result array to string and reverse the string
        return ''.join(reversed(result))
