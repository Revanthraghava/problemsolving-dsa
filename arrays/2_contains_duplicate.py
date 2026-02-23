class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

# LeetCode 217 - Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
#
# Pattern: HashSet for duplicate detection
# Time: O(n)
# Space: O(n)