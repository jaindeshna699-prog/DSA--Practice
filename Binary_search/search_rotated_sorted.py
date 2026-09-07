# Time complexity = O(logn)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (low + high)//2
            if(nums[mid] == target):
                return mid
            if(nums[low] <= nums[mid]):  # identifies which part is sorted(left sorted)
                if(target <= nums[mid] and nums[low] <= target):
                    high = mid - 1
                else:
                    low = mid + 1
            else:                         # if right sorted
                if(target <= nums[high] and nums[mid] <= target):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        