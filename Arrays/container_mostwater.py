# Time complexity : O(n)
# space complexity : O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = -1
        left, right = 0, n-1
        while(left < right):
            a = min(height[left], height[right])
            b = (right - left)
            area1 = a*b
            area = max(area, area1)
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return area


        