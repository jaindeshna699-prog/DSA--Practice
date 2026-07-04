# Time complexity : o(n)
# Space complexity : o(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # do not return anything, modify nums in place  instead.
        index = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if(nums[i] < nums[i+1]):
                index = i
                break
        if(index == -1):
            self.reverse(nums, 0)
            return
        for i in range(n-1, index, -1):
            if(nums[i] > nums[index]):
                self.swap(nums, i, index)
                break
        self.reverse(nums, index + 1)
        
    def reverse(self, nums, start):
            i, j = start, len(nums)-1
            while(i < j):
                self.swap(nums, i, j)
                i += 1
                j -= 1
    def swap(self, nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp 


                
        