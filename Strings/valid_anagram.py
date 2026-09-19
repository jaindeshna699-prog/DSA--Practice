class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1   # this is how we set elements in dict
        for ch in t:
            if ch not in hashmap:
                return False
            else:
                if(hashmap[ch] == 0): # If that ch appears one more time in t it will give a freq of 0 
                    return False
                else:
                    hashmap[ch] -= 1
        return True

 # Time Complexity = O(N)
 # Space Complexity = O(1) because even in the worst case scenario the space complexity would not more than O(26) which is considered as O(1)       