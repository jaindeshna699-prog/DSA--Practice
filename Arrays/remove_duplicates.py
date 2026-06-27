# time complexity : o(n)
# space complexity : o(1)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0   # it is a pointer tracking unique elements 
        for i in range(len(nums)):
            if(nums[i] != nums[j]):
                nums[j + 1] = nums[i]
                j += 1
        return j + 1

        