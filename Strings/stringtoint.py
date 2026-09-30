class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:  # if we have a empty string
            return 0
        int_max = 2**31 - 1
        int_min = -2**31
        i = 0
        n = len(s)
        while i < n and s[i] == " ": # for empty space
            i += 1
        if(i == n):
            return 0
        sign = 1        # check for sign
        if(s[i] == "+"):
            i +=  1
        elif(s[i] == "-"):
            sign = -1
            i += 1
        res = 0
        while i < n and s[i].isdigit(): # read the digits
            digit = int(s[i])
            res = res*10 + digit
            if(sign * res < int_min):
                return int_min
            if(sign *res > int_max):
                return int_max
            i += 1
        return sign*res



        

