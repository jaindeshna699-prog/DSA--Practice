class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        for i in range(1<<n):
            subset = []   #binary representation of i
            for j in range(n):
                if i & 1<<j: #comparing the binary representation of i and j with & operator
                    subset.append(nums[j])
            result.append(subset)
        return result

# TIme complexity = O(n.2**n) we have total of 2**n subsets of length n
# Space complexity = O(n.2**n)

