class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        hashmap = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            rem = sum - k
            if rem in hashmap:
                count += hashmap[rem]
            if sum in hashmap:
                hashmap[sum] += 1
            else:
                hashmap[sum] = 1
        return count
# Time complexity O(N)
#Space complexity O(N)