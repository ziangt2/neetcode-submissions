class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        result = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
            while i - l - max(count.values()) +1 > k:

                count[s[l]] -= 1
                l += 1
            result = max(result, i -l+1)

        return result
                