class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ans = "1"
        for i in range(1, n): # we want to calculate the result n-1 times
            current = ans[0]
            count = 1
            res = ""
            for c in ans[1:]: # it starts the loop from the second ch becz we have already store the first ch
                if c == current: # checks if the next ch is the same to previous one so tnat our count of consecutive ch would increase
                    count += 1
                else:
                    res = res + str(count) + current
                    current = c
                    count = 1
            ans = res + str(count) + current
        return ans



        


        