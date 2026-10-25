class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtracking(current, openbracket, closingbracket):
            if openbracket == n and closingbracket == n:
                result.append(current)
                return
            if openbracket < n:
                backtracking(current +'(', openbracket + 1, closingbracket)
                
            if closingbracket < openbracket:
                backtracking(current +')', openbracket, closingbracket+1)
        backtracking("", 0, 0)
        return result
# TIme complexity = O(N) Building a string of length 6 takes up to \(O(n)\) time in Python because strings are immutable.
# Space complexity = O(N)
                
        

        