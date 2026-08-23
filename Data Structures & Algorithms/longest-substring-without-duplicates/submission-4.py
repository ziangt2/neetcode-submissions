class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = {}
        result = 0

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0) + 1

            while hashmap.get(s[i],0)>1:
                
                hashmap[s[l]] = hashmap.get(s[l],0) - 1
                l +=1
            result = max(result, i+1-l)

        return result

