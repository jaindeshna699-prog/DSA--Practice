# Time complexity : o(logx)


class Solution(object):
    def reverse(self, x):
        rev=0
        if(x<0):
            sign=-1
        else:
            sign=1
        x=abs(x)

        while(x):
            rev=rev*10+x%10
            x//=10
            if rev>2**31-1:
                return 0
        return sign*rev
        