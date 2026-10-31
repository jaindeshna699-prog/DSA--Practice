class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        current= []
        result = []
        def backtrack(start, total):
            if total == n and len(current) == k:
                result.append(current.copy())
            if total > n:
                return
            if total < n and len(current) == k:
                return
            
            for i in range(start, 10):
                current.append(i)
                backtrack(i+1, total + i)
                current.pop()
        backtrack(1,0)
        return result



        