class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        open_brackets = 0
        min_add_required = 0
        for ch in s:
            if ch =='(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1

                else:
                    min_add_required += 1
        return min_add_required + open_brackets
            

