# problem 2 

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = [''] * len(s)
        numSt = [0] * len(s)
        idx = 0
        for c in s:
            if idx > 0 and st[idx - 1] == c:
                st[idx] = c
                numSt[idx] = numSt[idx - 1] + 1
                if numSt[idx] == k:
                    idx = idx - k
            else:
                st[idx] = c
                numSt[idx] = 1
            idx += 1
        return ''.join(st[:idx])