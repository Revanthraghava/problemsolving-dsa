# LeetCode 1929 - Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/
from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*(2*n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
    
# Create result array of size 2n
# Copy nums into first half and second half using index offset