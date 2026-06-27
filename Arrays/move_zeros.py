# Easy level 
# time complexity : o(n)
# space complexity : o(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0   #pointer tracks the next non zero element should be placed
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[i], nums[j] = nums[j], nums[i] # swap the current element with the element at index j
        
                j += 1    # move j to the next non zero element


            
       
        