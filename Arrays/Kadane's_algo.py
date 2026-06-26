# Time complexity : o(n)
# Space complexity : o(1)
# medium level

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        max_till_now = -inf
        for c in nums:
            curr_max = max(c, curr_max + c)
            max_till_now = max(max_till_now, curr_max)
        return max_till_now


        