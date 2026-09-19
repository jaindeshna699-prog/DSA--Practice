class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        hashmap_stot = {}
        hashmap_ttos = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in hashmap_stot:
                if(hashmap_stot[char_s] != char_t): #checking if the same ch which is already mapped to some ch is converting into another ch
                    return False
            else:
                hashmap_stot[char_s] = char_t
            if char_t in hashmap_ttos:
                if(hashmap_ttos[char_t] != char_s):# checking if the two different ch is mapped to the same ch
                    return False
        
            else:
                hashmap_ttos[char_t] = char_s
        return True
# Time complexity = O(N)
# Space complexity = O(N)
#-> we are using two hashmaps        



        