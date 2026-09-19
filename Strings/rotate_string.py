class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False
            # Checking every possible rotation
        for i in range(len(s)):
            # one rotation
            s = s[1:] + s[0]
            if(s == goal):
                return True

        return False
            