class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        base = strs[0]
        if(len(strs) == 0):
            return prefix
        for i in range(len(base)):            #iterating in the ch of base word
            for words in strs[1:]:            # doing vertical scan in the words of string  using slicing ([1:]) which basically leaves the 1st word and start from the 1st index
                if(i == len(words) or base[i] != words[i]):         #edge case
                    return prefix
                
            prefix += base[i]
        
        return prefix                      #edge case if the base word is empty string

        # Time complexity : O(M*N)
        # Space complexity : O(1)

            

        

        