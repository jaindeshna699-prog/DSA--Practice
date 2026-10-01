class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) <= 1):
            return s
        def expand_from_center(left, right):
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left+1 : right]
        max_string = s[0]
        for i in range(len(s)-1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)
            if len(odd) > len(max_string):
                max_string = odd
            if len(even) > len(max_string):
                max_string = even
        return max_string

        # Time complexity : O(n^2)  because for the one loop in which we are checking it is palindroem and for the loop in which we are iterating
        # Space complexity : O(1)
    
        