class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findindex(first:bool):
            low = 0
            high = len(nums) - 1
            index = -1
            while(low <= high):
                mid = (low + high)//2
                if(nums[mid] == target):
                    index = mid
                    if(first):
                        high = mid - 1
                    else:
                        low = mid + 1
                elif(nums[mid] < target):
                    low = mid + 1
                else:
                    high = mid - 1
            return index
        return [findindex(True), findindex(False)]

    # Time complexity = O(logn)
    # Space complexity = O(1)


    

      

        

        