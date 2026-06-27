# Time complexity : o(n)
# Space complexity : o(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if(count == 0):
                count = 1
                el = nums[i]
            elif(nums[i] == el):
                count += 1
            else:
                count -= 1
        count1 = 0
        for i in range(len(nums)):
            if(nums[i] == el):
                count1 += 1
        if(count1 > len(nums)//2):
            return el
    

        
        

        