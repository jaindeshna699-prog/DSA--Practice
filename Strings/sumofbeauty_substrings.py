class Solution:
    def beautySum(self, s: str) -> int:
        
        sum = 0
        
        for i in range(len(s)): # staring index of substring

            freq = [0]*26  # freq array of size 26
            for j in range(i, len(s)):  # last index of substring
                 
                freq[ord(s[j]) - 97] += 1 # to map all the characters at their corrcet position and increase their frequency
                max_freq = -inf
                min_freq = inf
                for diff in freq: #frequency of individual character in current substring
                    if diff > 0:
                        max_freq = max(max_freq, diff)
                        min_freq = min(min_freq, diff)
                        beauty = max_freq - min_freq
                sum += beauty
                    
        return sum
                
                


                
                
        


        