# medium level
# Time complexity : o(n)
# Space complexity : o(1)

class Solution:
    def rotate(self, nums: List[int], k: int) ->None:
        n = len(nums)
        k %= n  # array of length n after n rotation is the same in starting so if the k is greater than n we only do extra
        def reverse(l, r):
            while(l < r):
                nums[l], nums[r] = nums[r] , nums[l] 
                l += 1
                r -= 1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)  
            
           
            
            


           

        """
        Do not return anything, modify nums in-place instead.
        """
        