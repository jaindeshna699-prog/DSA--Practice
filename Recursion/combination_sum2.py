class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        current = []
        result = []
        def backtrack(start, total):
            if total == target:
                result.append(current.copy())
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue # this step will skip the duplicates
                current.append(candidates[i])
                backtrack(i+1, total+candidates[i])
                current.pop()
        backtrack(0,0)
        return result
        