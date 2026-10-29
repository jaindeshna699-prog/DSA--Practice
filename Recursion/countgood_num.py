class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
#calculation of number of even and odd indices
        even = (n+1)//2
        odd = n//2
# we will use some permutation concept to find out how many combinations should be there
        return pow(5,even, mod)*pow(4,odd, mod)% mod
# 5  and 4 are the choices for the even and odd indices respectively

# time complexity = O(logn)
# space complexity = O(1) 


        
            

            


        