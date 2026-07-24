class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        l = 0
        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1

        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1

            if r - l +1 > len(s1):
                left_count = s2[l]
                count2[left_count] -= 1
                l += 1
                
                if count2[left_count] == 0:
                    del count2[left_count]
            if r -l +1 == len(s1) and count1 == count2:
                return True

        return False 
