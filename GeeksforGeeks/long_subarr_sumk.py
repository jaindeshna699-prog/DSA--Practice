class Solution:
    def longestSubarray(self, arr, k):  
        sum = 0
        max_len = 0
        hashmap = {}
        for i in range(len(arr)):
            sum += arr[i]
            if(sum == k):
                max_len = max(max_len, i + 1)
            rem = sum - k
            if rem in hashmap:
                len1 = i- hashmap[rem]
                max_len = max(max_len, len1)
            if sum not in hashmap:
                hashmap[sum] = i
        return max_len
            
            
    
# Time complexity = O(n)
# Space complexity = O(n)