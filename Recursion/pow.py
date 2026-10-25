class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        ans = 1
        while power > 0:
            if power%2 == 1: 
                ans *= x
            x *= x  # squaring the base
            power //= 2  # making the power half
        if n < 0:
            ans = 1/ans
        return ans
# Time complexity = O(logN) because everytime whenever we get even power we are doing half of it
# Space complexity = O(1)
                