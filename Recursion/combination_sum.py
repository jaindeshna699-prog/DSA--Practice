class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current = []
        def backtrack(start, total):
            if total == target:
                result.append(current.copy())
            if total > target:# if it exceeds we do not need to add further elements because adding a number would only increase the total
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, total + candidates[i])# i is taken because we can select one element multiple times
                current.pop()
        backtrack(0,0)
        return result

        
        